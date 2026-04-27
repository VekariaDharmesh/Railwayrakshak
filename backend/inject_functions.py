import re

html_path = '/Users/vekariadharmeshh/Documents/Railway Faucture /backend/static/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add ID to global search
content = content.replace(
    '<input type="text" placeholder="Search Node/KM..."',
    '<input type="text" id="global-search" onkeyup="filterNodes()" placeholder="Search Node/KM..."'
)

# 2. Add Profile Dropdown
profile_html = """
            <div class="relative group cursor-pointer" onclick="document.getElementById('profile-dropdown').classList.toggle('hidden')">
                <div class="flex items-center gap-2 pl-4 border-l border-slate-200">
                    <div class="text-right hidden sm:block">
                        <div class="text-[10px] font-bold text-slate-900 uppercase tracking-wider">Cdr. Sharma</div>
                        <div class="text-[9px] text-indigo-500 font-mono">SYS_ADMIN</div>
                    </div>
                    <div class="w-7 h-7 rounded bg-slate-200 border-2 border-indigo-500 flex items-center justify-center text-xs font-bold text-slate-900 shadow-[0_0_10px_rgba(139,92,246,0.3)]">S</div>
                </div>
                <div id="profile-dropdown" class="hidden absolute right-0 top-full mt-2 w-48 bg-white border border-slate-200 rounded-lg shadow-lg overflow-hidden z-50">
                    <a href="#" class="block px-4 py-2 text-xs text-slate-700 hover:bg-slate-50">My Profile</a>
                    <a href="#" class="block px-4 py-2 text-xs text-slate-700 hover:bg-slate-50">Access Logs</a>
                    <div class="border-t border-slate-200"></div>
                    <a href="#" class="block px-4 py-2 text-xs text-rose-500 hover:bg-slate-50 font-bold" onclick="alert('Session Terminated')">Secure Logout</a>
                </div>
            </div>
"""
# Replace existing User profile block
content = re.sub(
    r'<!-- User -->\s*<div class="flex items-center gap-2 pl-4 border-l border-slate-200">.*?</div>\s*</div>\s*</div>',
    '<!-- User -->\n' + profile_html + '\n        </div>',
    content,
    flags=re.DOTALL
)

# 3. Add onclick to settings button
content = content.replace(
    '<button class="w-full text-left py-2 text-xs text-slate-500 hover:text-slate-900 flex items-center gap-2"><svg class="w-3 h-3"',
    '<button onclick="toggleSettings()" class="w-full text-left py-2 text-xs text-slate-500 hover:text-slate-900 flex items-center gap-2"><svg class="w-3 h-3"'
)

# 4. Inject Modals and JS functions before </body>
modals_and_js = """
    <!-- Toast Notification -->
    <div id="toast-container" class="fixed top-20 right-4 z-50 flex flex-col gap-2"></div>

    <!-- Settings Modal -->
    <div id="settings-modal" class="hidden fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-50 flex items-center justify-center">
        <div class="bg-white rounded-xl shadow-xl w-96 p-6 border border-slate-200">
            <h2 class="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2">
                <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                System Settings
            </h2>
            <div class="space-y-4">
                <div class="flex items-center justify-between">
                    <span class="text-sm font-bold text-slate-700">Auto-Dispatch Mode</span>
                    <input type="checkbox" checked class="w-4 h-4 text-blue-600 rounded focus:ring-blue-500">
                </div>
                <div class="flex items-center justify-between">
                    <span class="text-sm font-bold text-slate-700">Drone Auto-Patrol</span>
                    <input type="checkbox" class="w-4 h-4 text-blue-600 rounded focus:ring-blue-500">
                </div>
                <div>
                    <span class="text-sm font-bold text-slate-700 mb-1 block">AI Sensitivity Threshold</span>
                    <input type="range" min="1" max="100" value="80" class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer">
                </div>
            </div>
            <button onclick="toggleSettings()" class="mt-6 w-full py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-bold transition-colors">Save Preferences</button>
        </div>
    </div>

    <script>
        function filterNodes() {
            const query = document.getElementById('global-search').value.toLowerCase();
            const nodes = document.querySelectorAll('#tracks-container .py-2');
            nodes.forEach(node => {
                const text = node.innerText.toLowerCase();
                node.style.display = text.includes(query) ? 'flex' : 'none';
            });
        }

        function toggleSettings() {
            const modal = document.getElementById('settings-modal');
            modal.classList.toggle('hidden');
        }

        function showToast(message, type='info') {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            const color = type === 'error' ? 'bg-rose-500' : 'bg-slate-900';
            toast.className = `${color} text-white px-4 py-2 rounded shadow-lg text-xs font-mono font-bold animate-fade-in`;
            toast.innerText = message;
            container.appendChild(toast);
            setTimeout(() => { toast.remove(); }, 3000);
        }
    </script>
</body>
"""

content = content.replace("</body>", modals_and_js)

# 5. Fix Voice Command to show toast if not supported
voice_code = """
        const voiceBtn = document.getElementById('voice-btn');
        if ('webkitSpeechRecognition' in window) {
            const recognition = new webkitSpeechRecognition();
            recognition.continuous = false;
            
            voiceBtn.onclick = () => { recognition.start(); voiceBtn.classList.add('listening'); };
            recognition.onresult = (e) => {
                const cmd = e.results[0][0].transcript.toLowerCase();
                showToast(`Voice heard: "${cmd}"`);
                if (cmd.includes('drone') || cmd.includes('camera')) switchView('drone');
                else if (cmd.includes('ledger') || cmd.includes('blockchain')) switchView('ledger');
                else if (cmd.includes('dashboard')) switchView('dashboard');
                else showToast(`Command unmapped: "${cmd}"`, 'error');
            };
            recognition.onend = () => voiceBtn.classList.remove('listening');
        } else {
            voiceBtn.onclick = () => { showToast('Voice AI not supported in this browser.', 'error'); };
        }
"""
content = re.sub(r"const voiceBtn = document\.getElementById\('voice-btn'\);.*?recognition\.onend = \(\) => voiceBtn\.classList\.remove\('listening'\);\s*\}", voice_code, content, flags=re.DOTALL)

# 6. Update `updateUI` to inject alerts and AI health dynamically
update_ui_code = """
        function updateUI() {
            // Header stats
            document.getElementById('h-nodes').innerText = Object.keys(tracks).length;
            const anyNode = Object.values(tracks)[0];
            if(anyNode && anyNode.weather) document.getElementById('h-weather').innerText = anyNode.weather.condition;
            
            document.getElementById('h-alerts').innerText = alerts.length;
            
            let avgScore = 0;
            const nodes = Object.values(tracks);
            if (nodes.length > 0) {
                nodes.forEach(n => avgScore += n.score);
                const health = Math.max(0, 100 - (avgScore / nodes.length)).toFixed(1);
                document.querySelector('.text-neon-green.font-bold').innerText = health + '%';
            }
"""
content = content.replace("""        function updateUI() {
            // Header stats
            document.getElementById('h-nodes').innerText = Object.keys(tracks).length;
            const anyNode = Object.values(tracks)[0];
            if(anyNode && anyNode.weather) document.getElementById('h-weather').innerText = anyNode.weather.condition;

            // Map & Node List
            const tc = document.getElementById('tracks-container');
            tc.innerHTML = '';
            
            let avgScore = 0;
            const nodes = Object.values(tracks);""", update_ui_code + "\n            // Map & Node List\n            const tc = document.getElementById('tracks-container');\n            tc.innerHTML = '';\n")


with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected functions successfully!")
