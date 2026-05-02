# Railrakshak AI 🛡️
## Behavioral Anomaly & Fracture Detection Suite
**National Railway Safety & Predictive Infrastructure Platform**  
*AI-Driven (Computer Vision + Time-Series Forecasting) — Zero Manual Inspection Dependency*

---

### 📌 What is Railrakshak AI?
**Railrakshak AI** is a privacy-focused, mission-critical infrastructure tool that detects railway track fractures, sensor anomalies, and operational risks through behavioral AI analysis instead of scheduled manual checks.

It learns the "normal" vibrational and visual patterns of a healthy track network and flags unusual patterns such as:
- **Structural Anomalies**: Micro-cracks detected via drone-based computer vision.
- **Predictive Risk Spikes**: 7-day and 30-day forecasting of potential failures.
- **Sensor Deviations**: Abnormal track vibration, temperature, or alignment data.
- **Environmental Threats**: GIS-integrated risk assessments for weather-related disasters.

---

### ✨ Main Features
- **Zero-Day Fracture Detection**: Automated identification of unknown track defects.
- **Personalized Predictive Model**: AI trained on specific regional track usage and soil behavior.
- **Cyber-NOC Dashboard**: Real-time operational monitoring and command center.
- **Map Intelligence**: GIS-based tracking of infrastructure health across the network.
- **Blockchain Maintenance Ledger**: Tamper-proof verification of all safety records.
- **Automated Dispatch System**: Professional AI-generated threat notifications and work orders.
- **IoT Sensor Suite**: Real-time monitoring of 25+ live sensor data points.
- **Cross-platform Mobility**: Works on desktop command centers and field-agent devices.

---

### 🚀 Quick Start (Installation)
1. **Clone Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/railrakshak.git
   cd railrakshak
   ```

2. **Create Virtual Environment**
   - **Linux / macOS**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Train Your Predictive Model (Recommended)**
   - **Step 1 – Process historical data**
     ```bash
     python data_processor.py
     ```
   - **Step 2 – Train AI Predictor**
     ```bash
     python train_predictor.py
     ```
   *This generates the trained weights in the `/models` directory.*

5. **Run Application**
   - **Recommended (Launch NOC Dashboard)**
     ```bash
     ./run_noc.sh
     ```
   - **OR manually**
     ```bash
     streamlit run dashboard.py --server.address=0.0.0.0 --server.port=8501
     ```

---

### 📂 Project Structure
```text
railrakshak/
│
├── dashboard.py           # Streamlit Cyber-NOC Interface
├── run_noc.sh            # Launch script
│
├── vision_engine.py      # Drone-based Crack Detection (CV)
├── predictive_model.py    # Time-series Risk Forecasting (AI)
│
├── iot_bridge.py         # Sensor data integration
├── blockchain_service.py  # Tamper-proof Ledger management
│
├── notification_service.py # Alerting & Dispatch center
│
├── data_processor.py      # Data cleaning & normalization
├── train_predictor.py     # AI model training script
│
├── requirements.txt       # Dependencies
├── README.md              # Documentation
└── models/                # Saved model weights (.pth / .pkl)
```

---

### 🛠️ Full Setup Guide
#### Requirements
- **Python 3.9 – 3.11**
- **Git**
- **FastAPI / Streamlit**
- **OpenCV** (for computer vision modules)

#### Setup Steps
1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Train AI models (recommended for regional accuracy)
5. (Optional) Setup Drone Feed:
   - Connect drone via RTSP/Mavlink
   - Run: `python drone_connector.py`

---

### 🔧 Typical Usage
- **Predictive Scanning**
  - Open NOC Dashboard
  - Select "Risk Forecast"
  - View 7-day vs 30-day risk probability scores
- **Drone Surveillance**
  - Launch Vision Engine
  - Click "Analyze Feed"
  - Fractures > 85% confidence are auto-logged to blockchain
- **Blockchain Verification**
  - Access the "Maintenance Ledger"
  - View cryptographically signed inspection records

---

### ⚠️ Notes & Limitations
- **Hardware Dependent**: Computer vision requires stable drone/camera feeds.
- **Initial Training**: Best accuracy requires 3-6 months of historical sensor data.
- **Blockchain Node**: Requires an active connection to the safety ledger.
- **Privileged Access**: Critical alerts and dispatch require supervisor credentials.

---

### 🛠️ Troubleshooting
| Problem | Solution |
| :--- | :--- |
| **Model accuracy low** | Retrain with a larger historical dataset |
| **Drone feed lag** | Check network bandwidth or reduce resolution |
| **NOC dashboard error** | Ensure all environment variables are set in `.env` |
| **Blockchain sync fail** | Check network connection to the ledger node |

---

### 🔮 Future Improvements
- **iOS/Android Field App** for maintenance crews.
- **Micro-acoustic sensors** for real-time wheel-flat detection.
- **Multi-region shared AI model** for cross-country track patterns.
- **Full Autonomous Repair Drones** integration.

---

### 📄 License
MIT License — Free to use, modify, distribute for safety and research.

### ❤️ Contributing
Pull requests welcome for:
- Improved Computer Vision algorithms.
- Better predictive modeling for soil-track interaction.
- UI/UX enhancements for the NOC dashboard.

### 👨‍💻 Author
**Dharmesh Vekaria**  
Anand, Gujarat · 2025–2026

*Focused on national infrastructure safety & modern AI-driven threat detection.*

---
🛡️ **Stay Safe · Stay On Track.**
