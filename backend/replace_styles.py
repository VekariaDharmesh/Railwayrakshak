import re
import os

html_path = '/Users/vekariadharmeshh/Documents/Railway Faucture /backend/static/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Title and Naming
content = content.replace('RailGuard Cyber-NOC - National Safety Platform', 'Railway Rakshak - Minimal Dashboard')
content = content.replace('RailGuard <span class="text-neon-blue font-light">NOC</span>', 'Railway Rakshak <span class="text-neon-blue font-light">NOC</span>')

# 2. Tailwind Config & CSS Changes
content = re.sub(
    r"colors: \{.*?\}",
    "colors: { neon: { blue: '#2563eb', purple: '#6366f1', red: '#e11d48', green: '#10b981', yellow: '#f59e0b' } }",
    content,
    flags=re.DOTALL
)

# Fix body background
content = content.replace("body { background-color: #050b14; color: #f8fafc;", "body { background-color: #f8fafc; color: #0f172a;")
content = content.replace("before:bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')]", "")
content = content.replace("before:opacity-20", "")

# Redefine glass-panel and cyber-border
content = re.sub(r"\.glass-panel \{.*?\}", ".glass-panel { background: #ffffff; border: 1px solid #e2e8f0; box-shadow: 0 1px 3px 0 rgba(0,0,0,0.1); border-radius: 0.75rem; }", content)
content = re.sub(r"\.cyber-border \{.*?\}", ".cyber-border { border-color: #e2e8f0 !important; }", content)
content = re.sub(r"\.cyber-border:hover \{.*?\}", ".cyber-border:hover { border-color: #cbd5e1 !important; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1) !important; }", content)

# 3. Global Text and Background Inversions
# dark gray borders to light gray
content = content.replace('border-gray-800', 'border-slate-200')
content = content.replace('border-gray-700', 'border-slate-300')

# Text color inversions
content = content.replace('text-white', 'text-slate-900')
content = content.replace('text-gray-300', 'text-slate-700')
content = content.replace('text-gray-400', 'text-slate-500')
content = content.replace('text-gray-500', 'text-slate-400')

# Background inversions
content = content.replace('bg-black/40', 'bg-slate-50')
content = content.replace('bg-black/50', 'bg-slate-100')
content = content.replace('bg-black/60', 'bg-slate-100')
content = content.replace('bg-black/80', 'bg-white')
content = content.replace('bg-black', 'bg-white')
content = content.replace('bg-white/5', 'bg-slate-50 hover:bg-slate-100')
content = content.replace('bg-white/10', 'bg-slate-100')
content = content.replace('bg-gray-800', 'bg-slate-200')
content = content.replace('bg-gray-700', 'bg-slate-300')

# Replace neon names internally (Wait, I kept them in tailwind.config mapped to minimal hex codes! So I just need to adjust opacity logic if any)
# For example, text-neon-blue mapped to #2563eb looks good on white!

# Fix map styles
content = content.replace('#map { background: #050b14; }', '#map { background: #f8fafc; }')
content = content.replace('.leaflet-container { background: #050b14 !important; }', '.leaflet-container { background: #f8fafc !important; }')

# Fix table borders
content = content.replace('divide-gray-800', 'divide-slate-200')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied minimal style replacements successfully!")
