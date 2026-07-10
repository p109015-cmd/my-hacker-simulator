import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. 網頁頁面初始化設定（強制全螢幕、純黑背景）
st.set_page_config(page_title="究極黑客控制台 v11.0", page_icon="💀", layout="wide")

# 強制隱藏 Streamlit 的所有原生網頁元件
st.markdown(
    """
    <style>
    [data-testid="stHeader"], footer, #MainMenu {visibility: hidden !important;}
    .stApp {background-color: #000000 !important;}
    .block-container {padding: 0px !important; max-width: 100% !important; margin: 0px !important;}
    iframe {display: block !important; border: none !important; width: 100% !important;}
    body {overflow: hidden !important;}
    </style>
    """, 
    unsafe_allow_html=True
)

# 2. 純淨網頁控制引擎（將 HTML 編碼為 Base64，強制讓瀏覽器以獨立頁面渲染以獲得完整的滾動權限）
html_content = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>Matrix Terminal Ultimate</title>
    <style>
        * { box-sizing: border-box; }
        body, html {
            margin: 0;
            padding: 0;
            background-color: #000;
            width: 100%;
            height: 100%;
            overflow-y: auto; /* 允許整個網頁主體上下滾動 */
            font-family: 'Courier New', Courier, monospace;
        }
        canvas {
            display: block;
            position: fixed; /* 固定在背景，不隨滾動條移動 */
            top: 0;
            left: 0;
            z-index: 1;
            opacity: 0.15;
            width: 100vw;
            height: 100vh;
        }
        
        /* 終端機面板：高度隨內容自動撐開，讓最外層出現滾動條 */
        #terminal {
            position: relative;
            z-index: 2;
            padding: 30px;
            color: #00ff00;
            font-size: 18px;
            line-height: 1.6;
            white-space: pre-wrap;
            word-wrap: break-word;
            text-shadow: 0 0 4px #00ff00;
            min-height: 100vh;
        }
        
        .cursor {
            display: inline-block;
            background-color: #00ff00;
            width: 10px;
            height: 18px;
            animation: blink 0.8s infinite;
            vertical-align: middle;
        }
        @keyframes blink {
            0%, 49% { background-color: #00ff00; }
            50%, 100% { background-color: transparent; }
        }
        
        #success-overlay {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 999;
            background-color: rgba(0, 0, 0, 0.95);
            border: 3px solid #00ff00;
            padding: 40px;
            text-align: center;
            color: #00ff00;
            font-size: 28px;
            font-weight: bold;
            box-shadow: 0 0 30px #00ff00;
            letter-spacing: 2px;
        }
        #hidden-input {
            position: fixed;
            top: 0;
            left: 0;
            opacity: 0;
            z-index: -1;
        }
    </style>
</head>
<body>

    <canvas id="canvas"></canvas>
    <div id="terminal"></div>
    <input type="text" id="hidden-input" autofocus>

    <div id="success-overlay">
        💀 [SYSTEM UNLOCKED] 你已成功侵入 💀<br>
        ========================================<br>
        ACCESS GRANTED // 核心控制權限獲取成功！<br>
        指揮官：ANONYMOUS OPERATOR 已全面接管。
    </div>

    <script>
        // === 1. Matrix 數位雨 ===
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');

        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);

        const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789🧬💀🛰️🔥🔓🚀💥⚡";
        const alphabet = chars.split("");
        const fontSize = 16;
        let columns = canvas.width / fontSize;
        const rainDrops = Array(Math.floor(columns)).fill(1);

        function drawMatrix() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#0F0';
            ctx.font = fontSize + 'px monospace';

            for (let i = 0; i < rainDrops.length; i++) {
                const text = alphabet[Math.floor(Math.random() * alphabet.length)];
                ctx.fillText(text, i * fontSize, rainDrops[i] * fontSize);
                if (rainDrops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    rainDrops[i] = 0;
                }
                rainDrops[i]++;
            }
        }
        setInterval(drawMatrix, 30);


        // === 2. 隨機代碼 + 視窗級自動滿頁滾動引擎 ===
        const terminal = document.getElementById('terminal');
        const hiddenInput = document.getElementById('hidden-input');
        const successOverlay = document.getElementById('success-overlay');

        const tags = ['INFO', 'WARN', 'SYSTEM', 'INJECT', 'DECRYPT', 'BYPASS', 'CONNECT', 'EXPLOIT'];
        const actions = [
            '正在偵測通訊埠漏洞', '成功繞過防火牆安全認證層', '攔截核心加密資料庫封包', 
            '正在注入隱形後門 Trojan.Core', '啟動量子演算法破解私鑰', '成功切換虛擬本地代理網段', 
            '遠端溢位攻擊成功', '正在強制同步資料傳輸緩衝區', '核心偽裝層部署完畢', '全面癱瘓伺服器流量'
        ];
        const targets = [
            'nasa.gov.secure', 'pentagon.admin.node', 'mainframe.central.bank', 'global.dns.server', 
            'crypto.vault.ledger', 'security.gateway.firewall', 'backbone.root.switch', 'cloud.matrix.core'
        ];
        const scripts_pool = [
            'for (int i = 0; i < 1024; i++) { malloc(sizeof(payload)); }',
            'connect_to_proxy_node("SOCKS5://103.24.51.9", port=22);',
            'if (auth_token == "BYPASS_TRUE") { grant_root_access(); }',
            'AES_256_Decrypt(key_matrix, cipher_text, chunk_size=4096);',
            'iptables -A INPUT -s 127.0.0.1 -j DROP # Erasing footprints',
            'send_packet_stream(target_ip, protocol="UDP", packets=250000);'
        ];

        let lineCount = 0; 
        let isUnlocked = false; 

        // 🛠️ 【即時視窗滾動修正】：只要偵測到文字變多，直接命令整個網頁 window 滾動到最底端！
        const observer = new MutationObserver(() => {
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
            });
        });
        observer.observe(terminal, { childList: true, subtree: true });

        function generateRandomHackerLine() {
            lineCount++; 
            const hexAddr = '0x' + Math.floor(Math.random() * 16777215).toString(16).toUpperCase() + 
                            Math.floor(Math.random() * 16777215).toString(16).toUpperCase();
            const rand = Math.random();
            
            if (rand < 0.35) {
                const tag = tags[Math.floor(Math.random() * tags.length)];
                const action = actions[Math.floor(Math.random() * actions.length)];
                const target = targets[Math.floor(Math.random() * targets.length)];
                return ['', '[' + tag + '] [MEM:' + hexAddr + '] ' + action + ' >> 目標: ' + target + '...'].join(String.fromCharCode(10));
            } else if (rand < 0.7) {
                const code = scripts_pool[Math.floor(Math.random() * scripts_pool.length)];
                return ['', '[CODE_STR] [ADDR:' + hexAddr + ']  ' + code].join(String.fromCharCode(10));
            } else {
                const progress = '■'.repeat(Math.floor(Math.random() * 15) + 10);
                const percent = Math.floor(Math.random() * 40) + 60;
                return ['', '[DECRYPT] [BLOCK:' + hexAddr + '] 演算破解中 [' + progress + '] ' + percent + '% SUCCESS...'].join(String.fromCharCode(10));
            }
        }

        let currentText = [
            "==================================================================",
            "💀 首席網路安全專家：[REDACTED] | 核心作戰控制終端 v11.0",
            "==================================================================",
            ">> CORE STATUS: READY",
            ">> INFILTRATION LEVEL: INITIALIZED",
            "",
            "root@ghost-terminal:~# <span class='cursor'></span>"
        ].join(String.fromCharCode(10));
        
        terminal.innerHTML = currentText;

        let currentLineBuffer = "";
        let bufferCharIndex = 0;

        function autoTypeHackerCode() {
            if (isUnlocked) return; 

            for (let k = 0; k < 5; k++) {
                if (!currentLineBuffer || bufferCharIndex >= currentLineBuffer.length) {
                    if (lineCount >= 35) { // 增加至 35 行，讓它滾動得更過癮
                        isUnlocked = true;
                        successOverlay.style.display = 'block'; 
                        return;
                    }
                    currentLineBuffer = generateRandomHackerLine();
                    bufferCharIndex = 0;
                }

                let nextChar = currentLineBuffer.charAt(bufferCharIndex);
                if (nextChar.charCodeAt(0) === 10) {
                    nextChar = '<br>';
                }

                let base = terminal.innerHTML.replace("<span class=\\"cursor\\"></span>", "");
                terminal.innerHTML = base + nextChar + "<span class=\\"cursor\\"></span>";
                bufferCharIndex++;
            }
        }

        document.body.addEventListener('click', () => { hiddenInput.focus(); });
        document.addEventListener('keydown', (e) => {
            if (e.key !== 'Shift' && e.key !== 'Control' && e.key !== 'Alt' && e.key !== 'Meta') {
                autoTypeHackerCode();
            }
        });
        
        setTimeout(() => { hiddenInput.focus(); }, 200);
    </script>
</body>
</html>
"""

# 將 HTML 轉為 Base64 Data URI，防止 Streamlit 多層容器截斷滾動行為
b64_html = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
data_uri = f"data:text/html;base64,{b64_html}"

# 3. 使用獨立的 iframe 進行高度擴展渲染，完美實現自動向下滑動
st.components.v1.iframe(data_uri, height=1200, scrolling=True)
