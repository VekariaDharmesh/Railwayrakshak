import re
import os

simulator_path = '/Users/vekariadharmeshh/Documents/Railway Faucture /backend/simulator.py'
training_path = '/Users/vekariadharmeshh/Documents/Railway Faucture /backend/generate_training_data.py'

new_sensors = """    # Additional 7 locations to reach 25
    "GHY_DBR_001_ACC": {"lat": 26.1445, "lng": 91.7362}, # Guwahati
    "VAR_DDU_001_ACC": {"lat": 25.3176, "lng": 82.9739}, # Varanasi
    "AGR_GWL_001_ACC": {"lat": 27.1767, "lng": 78.0081}, # Agra
    "JBP_KAT_001_ACC": {"lat": 23.1815, "lng": 79.9864}, # Jabalpur
    "CBE_ED_001_ACC": {"lat": 11.0168, "lng": 76.9558}, # Coimbatore
    "VSK_BZA_001_ACC": {"lat": 17.6868, "lng": 83.2185}, # Visakhapatnam
    "DND_KGP_001_ACC": {"lat": 23.7947, "lng": 86.4304}, # Dhanbad
}"""

# Update simulator.py
with open(simulator_path, 'r', encoding='utf-8') as f:
    sim_content = f.read()

sim_content = re.sub(r"}\s*def generate_normal_data\(\):", new_sensors + "\n\ndef generate_normal_data():", sim_content)

with open(simulator_path, 'w', encoding='utf-8') as f:
    f.write(sim_content)

# Update generate_training_data.py
training_sensors = """        "DEL_UMB_001_ACC", "DEL_UMB_002_ACC", "CHD_ASR_001_ACC", "JAI_AJE_001_ACC",
        "MUM_PUN_001_ACC", "MUM_PUN_002_ACC", "AMD_BRC_001_ACC", "SRT_BRC_001_ACC",
        "BLR_MYS_001_ACC", "MAA_MDU_001_ACC", "HYD_VJA_001_ACC", "COK_TRV_001_ACC",
        "CCU_BBS_001_ACC", "BBS_VSK_001_ACC", "PNQ_NAG_001_ACC", "BPL_IND_001_ACC",
        "LKO_CNB_001_ACC", "PAT_GAY_001_ACC",
        "GHY_DBR_001_ACC", "VAR_DDU_001_ACC", "AGR_GWL_001_ACC", "JBP_KAT_001_ACC",
        "CBE_ED_001_ACC", "VSK_BZA_001_ACC", "DND_KGP_001_ACC"
    ]"""

with open(training_path, 'r', encoding='utf-8') as f:
    train_content = f.read()

train_content = re.sub(
    r'sensors = \[.*?\]',
    'sensors = [\n' + training_sensors,
    train_content,
    flags=re.DOTALL
)

with open(training_path, 'w', encoding='utf-8') as f:
    f.write(train_content)

print("Updated 25 locations.")
