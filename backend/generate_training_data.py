import csv
import random
from datetime import datetime, timedelta
import os

def generate_dataset(filename="historical_training_data.csv", num_records=50000):
    sensors = [
        "DEL_UMB_001_ACC", "DEL_UMB_002_ACC", "CHD_ASR_001_ACC", "JAI_AJE_001_ACC",
        "MUM_PUN_001_ACC", "MUM_PUN_002_ACC", "AMD_BRC_001_ACC", "SRT_BRC_001_ACC",
        "BLR_MYS_001_ACC", "MAA_MDU_001_ACC", "HYD_VJA_001_ACC", "COK_TRV_001_ACC",
        "CCU_BBS_001_ACC", "BBS_VSK_001_ACC", "PNQ_NAG_001_ACC", "BPL_IND_001_ACC",
        "LKO_CNB_001_ACC", "PAT_GAY_001_ACC",
        "GHY_DBR_001_ACC", "VAR_DDU_001_ACC", "AGR_GWL_001_ACC", "JBP_KAT_001_ACC",
        "CBE_ED_001_ACC", "VSK_BZA_001_ACC", "DND_KGP_001_ACC"
    ]
    
    weather_conds = ["Clear", "Partly Cloudy", "Heavy Rain", "Thunderstorm", "Fog"]
    
    # Ensure data directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "timestamp", "sensor_id", "peak_freq", "rms_accel", "crest_factor", 
            "band1", "band2", "band3", "acoustic_peak", "acoustic_rms", 
            "temp", "humidity", "weather_condition", "label"
        ])
        
        start_time = datetime.now() - timedelta(days=365) # 1 year of data
        
        for i in range(num_records):
            is_anomaly = random.random() < 0.05 # 5% anomaly rate
            
            # Timestamp goes forward in time
            current_time = start_time + timedelta(minutes=15 * i)
            sensor = random.choice(sensors)
            
            if is_anomaly:
                peak_freq = random.uniform(1000, 1500)
                rms_accel = random.uniform(2.0, 4.0)
                crest_factor = random.uniform(6.0, 10.0)
                band1 = random.uniform(0.01, 0.05)
                band2 = random.uniform(0.4, 0.8)
                band3 = random.uniform(0.1, 0.3)
                acoustic_peak = random.uniform(8.0, 15.0)
                acoustic_rms = random.uniform(4.0, 8.0)
                temp = random.uniform(28.0, 35.0)
                humidity = random.uniform(80.0, 100.0)
                weather = random.choice(["Heavy Rain", "Thunderstorm"])
                label = 1 # Anomaly / Fracture Risk
            else:
                peak_freq = random.uniform(200, 300)
                rms_accel = random.uniform(0.1, 0.5)
                crest_factor = random.uniform(2.0, 3.5)
                band1 = random.uniform(0.05, 0.15)
                band2 = random.uniform(0.05, 0.15)
                band3 = random.uniform(0.05, 0.15)
                acoustic_peak = random.uniform(0.5, 1.5)
                acoustic_rms = random.uniform(0.2, 0.8)
                temp = random.uniform(15.0, 26.0)
                humidity = random.uniform(40.0, 60.0)
                weather = random.choice(["Clear", "Partly Cloudy", "Fog"])
                label = 0 # Normal
                
            writer.writerow([
                current_time.isoformat(),
                sensor,
                round(peak_freq, 2),
                round(rms_accel, 3),
                round(crest_factor, 2),
                round(band1, 3),
                round(band2, 3),
                round(band3, 3),
                round(acoustic_peak, 2),
                round(acoustic_rms, 2),
                round(temp, 1),
                round(humidity, 1),
                weather,
                label
            ])

if __name__ == "__main__":
    print("Generating historic training dataset (50,000 records)...")
    generate_dataset("data/historical_training_data.csv", 50000)
    print("Dataset generated successfully at data/historical_training_data.csv")
