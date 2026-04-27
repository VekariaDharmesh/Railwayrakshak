import re

html_path = '/Users/vekariadharmeshh/Documents/Railway Faucture /backend/static/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace white/gray grid lines with light theme grid lines
content = re.sub(r"color:\s*'rgba\(255,\s*255,\s*255,\s*0\.1\)'", "color: 'rgba(0,0,0,0.05)'", content)
content = re.sub(r"color:\s*'#374151'", "color: 'rgba(0,0,0,0.05)'", content)

# Replace tick text colors
content = re.sub(r"color:\s*'#9ca3af'", "color: '#64748b'", content)
content = re.sub(r"color:\s*'#6b7280'", "color: '#94a3b8'", content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated charts for light mode.")
