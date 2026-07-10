import streamlit as st
import streamlit.components.v1 as components

# 1. 網頁頁面初始化設定（強制全螢幕、純黑背景）
st.set_page_config(page_title="究極黑客控制台 v11.2", page_icon="💀", layout="wide")

# 強制隱藏 Streamlit 的所有原生網頁元件，達成 100% 全螢幕純黑客視窗
st.markdown(
    """
    <style>
    [data-testid="stHeader"], footer, #MainMenu {visibility: hidden !important;}
    .stApp {background-color: #000000 !important;}
    .block-container {padding: 0px !important; max-width: 100% !important; margin: 0px !important;}
    
    /* 強制讓元件的內外層容器都具備完整的滾動能力 */
    [data-testid="stHtmlBlock"], [data-testid="stElementContainer"], iframe {
        width: 100% !important;
        height: 100vh !important;
        display: block !important;
        border: none !important;
    }
    body {
        overflow: hidden !important;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# 2. 注入完全去姓名、內部流暢虛擬滾動引擎
html_code = """
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
            overflow: hidden; /* 防止最外層大環境破相 */
            width: 100%;
            height: 100vh;
            font-family: 'Courier New', Courier, monospace;
        }
        canvas {
            display: block;
            position: absolute;
            top: 0;
            left: 0;
            z-index: 1;
            opacity: 0.15;
        }
        
        /* 終端機面板：全螢幕高度，啟用原生平滑滾動 */
        #terminal {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            z-index: 2;
            padding: 40px;
            color: #00ff00;
            font-size: 18px;
            line-height: 1.6;
            overflow-y: auto; /* 開啟內部核心滾動 */
            white-space: pre-wrap;
            word-wrap: break-word;
            text-shadow: 0 0 4px #00ff00;
        }
        
        /* 隱藏原生網頁捲軸，保持純粹黑客介面 */
        #terminal::-webkit-scrollbar {
            display: none;
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
            position: absolute;
            opacity: 0;
            z-index: -1;
        }
        .log-line {
            margin-bottom: 4px;
        }
    </style>
</head>
<body>

    <canvas id="canvas"></canvas>
    <div id="terminal">
        <div class="log-line">==================================================================</div>
        <div class="log-line">💀 首席網路安全專家：[REDACTED] | 核心作戰控制終端 v11.2</div>
        <div class="log-line">==================================================================</div>
        <div class="log-line">&gt;&gt; CORE STATUS: READY</div>
        <div class="log-line">&gt;&gt; INFILTRATION LEVEL: INITIALIZED</div>
        <div class="log-line"></div>
        <div id="dynamic-content"></div>
        <div id="input-line">root@ghost-terminal:~# <span class="cursor"></span></div>
    </div>
    
    <input type="text" id="hidden-input" autofocus>

    <div id="success-overlay">
        💀 [SYSTEM UNLOCKED] 你已成功侵入 💀<br>
        ========================================<br>
        ACCESS GRANTED // 核心控制權限獲取成功！<br>
        指揮官：ANONYMOUS OPERATOR 已全面接管。
    </div>

    <script>
        // === 1. Matrix 數位雨引擎 ===
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


        // === 2. 核心隨機數據庫與流暢聚焦引擎 ===
        const terminal = document.getElementById('terminal');
        const dynamicContent = document.getElementById('dynamic-content');
        const inputLine = document.getElementById('input-line');
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

        function generateRandomHackerLine() {
            lineCount++; 
            const hexAddr = '0x' + Math.floor(Math.random() * 16777215).toString(16).toUpperCase() + 
                            Math.floor(Math.random() * 16777215).toString(16).toUpperCase();
            const rand = Math.random();
            
            if (rand < 0.35) {
                const tag = tags[Math.floor(Math.random() * tags.length)];
                const action = actions[Math.floor(Math.random() * actions.length)];
                const target = targets[Math.floor(Math.random() * targets.length)];
                return '[' + tag + '] [MEM:' + hexAddr + '] ' + action + ' >> 目標: ' + target + '...';
            } else if (rand < 0.7) {
                const code = scripts_pool[Math.floor(Math.random() * scripts_pool.length)];
                return '[CODE_STR] [ADDR:' + hexAddr + ']  ' + code;
            } else {
                const progress = '■'.repeat(Math.floor(Math.random() * 15) + 10);
                const percent = Math.floor(Math.random() * 40) + 60;
                return '[DECRYPT] [BLOCK:' + hexAddr + '] 演算破解中 [' + progress + '] ' + percent + '% SUCCESS...';
            }
        }

        // 新增一行指令，並強制讓輸入行平滑滾動到最底端
        function appendNewLine() {
            if (isUnlocked) return;

            if (lineCount >= 30) {
                isUnlocked = true;
                successOverlay.style.display = 'block';
                return;
            }

            const rawText = generateRandomHackerLine();
            const div = document.createElement('div');
            div.className
