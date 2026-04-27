import numpy as np
from sklearn.ensemble import IsolationForest

class VibrationAnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(
            contamination=0.05,
            random_state=42,
            n_estimators=100
        )
        # Train on massive historic dataset to simulate a robust baseline
        dummy_normal = np.random.normal(loc=0, scale=1, size=(10000, 6))
        self.model.fit(dummy_normal)
        
    def predict(self, features):
        """Return anomaly score 0-100 (0=normal, 100=anomaly)"""
        # Isolation forest outputs -1 (anomaly) or 1 (normal)
        anomaly_score = self.model.score_samples(features.reshape(1, -1))[0]
        # Remap score to 0-100
        normalized_score = max(0, min(100, (0.5 - anomaly_score) / 1.5 * 100))
        return normalized_score

class AcousticAnomalyDetector:
    def __init__(self):
        # Using a simple heuristic for prototype instead of LSTM
        self.error_threshold = 2.0
        
    def predict(self, features):
        """Return anomaly score 0-100"""
        # Mock prediction based on peak amplitude and RMS
        peak_amp = features[0]
        rms = features[1]
        
        score = (peak_amp + rms) * 10
        return min(100, score)

class EnsembleAnomalyDetector:
    def __init__(self):
        self.vibration_model = VibrationAnomalyDetector()
        self.acoustic_model = AcousticAnomalyDetector()
        
        self.w_vibration = 0.30
        self.w_acoustic = 0.40
        self.w_thermal = 0.30
        
    def detect_thermal_anomaly(self, current_temp, baseline_temp):
        delta_temp = current_temp - baseline_temp
        if delta_temp < 0.5:
            return 0
        elif delta_temp < 1.0:
            return 25
        elif delta_temp < 2.0:
            return 50
        elif delta_temp < 3.0:
            return 75
        else:
            return 100
            
    def fuse_predictions(self, vibration_score, acoustic_score, thermal_score):
        p_v = 1.0 / (1.0 + np.exp(-0.05 * (vibration_score - 50)))
        p_a = 1.0 / (1.0 + np.exp(-0.05 * (acoustic_score - 50)))
        p_t = 1.0 / (1.0 + np.exp(-0.05 * (thermal_score - 50)))
        
        p_fracture = (self.w_vibration * p_v + 
                      self.w_acoustic * p_a + 
                      self.w_thermal * p_t)
                      
        final_score = np.log(p_fracture / (1 - p_fracture + 1e-6)) * 20 + 50
        final_score = np.clip(final_score, 0, 100)
        return final_score
        
    def predict(self, vibration_features, acoustic_features, current_temp, baseline_temp):
        v_score = self.vibration_model.predict(vibration_features)
        a_score = self.acoustic_model.predict(acoustic_features)
        t_score = self.detect_thermal_anomaly(current_temp, baseline_temp)
        
        sensor_agreement = sum([v_score > 60, a_score > 60, t_score > 60])
        final_score = self.fuse_predictions(v_score, a_score, t_score)
        
        # Simulate LSTM Time-Series Forecasting
        base_risk = final_score
        forecast_7_day = min(100, base_risk * 1.15 if base_risk > 50 else base_risk + 5)
        forecast_30_day = min(100, base_risk * 1.4 if base_risk > 50 else base_risk + 15)
        
        return {
            'final_score': float(final_score),
            'vibration_score': float(v_score),
            'acoustic_score': float(a_score),
            'thermal_score': float(t_score),
            'sensor_agreement': int(sensor_agreement),
            'forecast_7_day': float(forecast_7_day),
            'forecast_30_day': float(forecast_30_day)
        }
