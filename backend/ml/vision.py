import cv2
import numpy as np
import base64
import io

def analyze_track_image(image_bytes: bytes) -> dict:
    """
    Simulates a Drone Camera Crack Detection module using OpenCV.
    Takes raw image bytes, applies Canny edge detection to find 'cracks',
    and returns a base64 encoded processed image along with a severity score.
    """
    # Convert bytes to numpy array
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        return {"status": "error", "message": "Invalid image"}
        
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply Canny Edge Detection (Simulating Crack Detection)
    edges = cv2.Canny(blurred, 50, 150)
    
    # Calculate crack severity based on number of edge pixels
    edge_pixels = cv2.countNonZero(edges)
    total_pixels = edges.shape[0] * edges.shape[1]
    crack_ratio = edge_pixels / total_pixels
    
    # Overlay edges on original image in Red
    result_img = img.copy()
    result_img[edges > 0] = [0, 0, 255] # BGR format
    
    # Encode back to jpeg
    _, buffer = cv2.imencode('.jpg', result_img)
    b64_str = base64.b64encode(buffer).decode('utf-8')
    
    severity = "CRITICAL" if crack_ratio > 0.05 else "MINOR"
    
    return {
        "status": "success",
        "processed_image": f"data:image/jpeg;base64,{b64_str}",
        "crack_ratio": crack_ratio * 100,
        "severity": severity,
        "edges_detected": edge_pixels
    }
