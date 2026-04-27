import asyncio
import json
import hashlib
import time
from datetime import datetime
from typing import Dict, List, Any
from fastapi import FastAPI, BackgroundTasks, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sse_starlette.sse import EventSourceResponse
from pydantic import BaseModel
import numpy as np
import os

from ml.anomaly_detection import EnsembleAnomalyDetector
from ml.vision import analyze_track_image

app = FastAPI(title="Rail Fracture Early Warning API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global state
clients = []
recent_alerts = []
track_data = {}
blockchain_tickets = []

detector = EnsembleAnomalyDetector()

class SensorData(BaseModel):
    sensor_id: str
    timestamp: float
    values: Dict[str, Any]
    health: str
    location: Dict[str, float] = None

class TicketRequest(BaseModel):
    sensor_id: str
    location: str

os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

async def broadcast_event(event_type: str, data: dict):
    message = json.dumps({"type": event_type, "data": data})
    for client in clients:
        await client.put(message)

def process_sensor_data(data: SensorData):
    vals = data.values
    vibration_features = np.array([
        vals.get("peak_freq", 200),
        vals.get("rms_accel", 0.3),
        vals.get("crest_factor", 2.5),
        vals.get("band1", 0.1),
        vals.get("band2", 0.1),
        vals.get("band3", 0.1)
    ])
    
    acoustic_features = np.array([
        vals.get("acoustic_peak", 1.0),
        vals.get("acoustic_rms", 0.5)
    ])
    
    current_temp = vals.get("temp", 25.0)
    baseline_temp = 25.0
    
    result = detector.predict(vibration_features, acoustic_features, current_temp, baseline_temp)
    
    track_data[data.sensor_id] = {
        "last_update": data.timestamp,
        "score": result["final_score"],
        "status": "NORMAL" if result["final_score"] < 60 else "ALERT",
        "location": data.location,
        "weather": {
            "temp": vals.get("temp", 25.0),
            "condition": vals.get("weather_condition", "Clear"),
            "humidity": vals.get("humidity", 50.0)
        },
        "forecast_7_day": result.get("forecast_7_day", 0.0),
        "forecast_30_day": result.get("forecast_30_day", 0.0)
    }
    
    if result["final_score"] > 60:
        alert = {
            "id": f"ALT-{int(data.timestamp * 1000)}",
            "timestamp": datetime.fromtimestamp(data.timestamp).isoformat(),
            "sensor_id": data.sensor_id,
            "location": f"KM {np.random.randint(100, 200)}.{np.random.randint(0, 9)}",
            "severity": "EMERGENCY" if result["final_score"] > 80 else "SCHEDULE_INSPECTION",
            "score": result["final_score"],
            "details": result
        }
        recent_alerts.insert(0, alert)
        if len(recent_alerts) > 50:
            recent_alerts.pop()
            
        asyncio.run(broadcast_event("new_alert", alert))
        
    asyncio.run(broadcast_event("track_update", track_data))

@app.post("/api/v1/sensor-data")
async def receive_sensor_data(data: SensorData, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_sensor_data, data)
    return {"status": "accepted"}

@app.post("/api/v1/tickets")
async def create_ticket(req: TicketRequest):
    ticket_id = f"TKT-{int(time.time() * 1000)}"
    timestamp = datetime.now().isoformat()
    
    prev_hash = blockchain_tickets[0]["hash"] if blockchain_tickets else "0000000000000000000000000000000000000000000000000000000000000000"
    
    data_to_hash = f"{ticket_id}{req.sensor_id}{req.location}{timestamp}{prev_hash}"
    current_hash = hashlib.sha256(data_to_hash.encode()).hexdigest()
    
    ticket = {
        "id": ticket_id,
        "sensor_id": req.sensor_id,
        "location": req.location,
        "timestamp": timestamp,
        "status": "Dispatched",
        "prev_hash": prev_hash,
        "hash": current_hash
    }
    
    blockchain_tickets.insert(0, ticket)
    await broadcast_event("new_ticket", ticket)
    return ticket

@app.post("/api/v1/analyze-image")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    result = analyze_track_image(contents)
    return result

@app.get("/api/v1/stream")
async def message_stream(request: Request):
    queue = asyncio.Queue()
    clients.append(queue)
    
    async def event_generator():
        try:
            yield {
                "event": "message",
                "data": json.dumps({
                    "type": "init", 
                    "data": {
                        "tracks": track_data, 
                        "alerts": recent_alerts,
                        "tickets": blockchain_tickets
                    }
                })
            }
            while True:
                if await request.is_disconnected():
                    break
                message = await queue.get()
                yield {
                    "event": "message",
                    "data": message
                }
        finally:
            clients.remove(queue)
            
    return EventSourceResponse(event_generator())
