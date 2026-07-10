import streamlit as st
import streamlit.components.v1 as components

# 1. 網頁頁面初始化設定
st.set_page_config(page_title="賴以航 究極黑客控制台 v8.0", page_icon="💀", layout="wide")

# 強制隱藏 Streamlit 的所有原生網頁元件，只留下全螢幕黑客視窗
st.markdown("""
    <style>
    /* 隱藏網頁標頭、漢堡選單、底部註腳 */
    [data-testid="stHeader"], footer, #MainMenu {visibility: hidden !important;}
    .stApp {background-color: #000000 !important;}
    /* 移除邊距，達成真正全螢幕 */
    .block-container {padding: 0px !important; max-width: 100% !important;}
    iframe {display: block; border: none;}
    </style>
""", unsafe_allow_html=True)

# 2. 注入好萊塢級別的「真．黑客終端與 Matrix 數位雨」互動組件
html_code = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>Matrix Terminal</title>
    <style>
        * { box-sizing: border-box; }
        body, html {
            margin: 0;
            padding: 0;
            background-color: #000;
            overflow: hidden;
            width: 100%;
            height: 100vh;
            font-family: 'Courier New', Courier, monospace;
        }
        /* 畫布：背景數位雨 */
        canvas {
            display: block;
            position: absolute;
            top: 0;
            left: 0;
            z-index: 1;
            opacity: 0.25; /* 讓背景雨淡淡的，不干擾文字閱讀 */
        }
        /* 終端機文字顯示層 */
        #terminal {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            z-index: 2;
            padding: 25px;
            color: #00ff00;
            font-size: 18px;
            line-height: 1.5;
            overflow-y: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
            text-shadow: 0 0 5px #00ff00;
        }
        /* 游標閃爍特效 */
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
        /* 隱藏真正用來觸發的手機/網頁輸入，全靠鍵盤監聽 */
        #hidden-input {
            position: absolute;
            opacity: 0;
            z-index: -1;
        }
    </style>
</head>
<body>

    <canvas id="canvas"></canvas>

    <div id="terminal"></div>
    <input type="text" id="hidden-input" autofocus>

    <script>
        // === 1. 經典 Matrix 數位雨動畫引擎 ===
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');

        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);

        const katakana = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789🧬💀🛰️🔥🔓🚀💥⚡";
        const alphabet = katakana.split("");

        const fontSize = 16;
        let columns = canvas.width / fontSize;

        const rainDrops = [];
        for (let x = 0; x < columns; x++) {
            rainDrops[x] = 1;
        }

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


        // === 2. 究極模擬黑客自動碼生成引擎 ===
        const terminal = document.getElementById('terminal');
        const hiddenInput = document.getElementById('hidden-input');

        // 電影級駭客日誌庫
        const hackerScripts = [
            "\\n[SYSTEM] 初始化首席網路安全專家：賴以航 (Yi-Hang Lai) 的專屬核心協定...",
            "\\n[CONNECT] 正在嘗試透過 256 位元洋蔥路由繞過各國防火牆網閘...",
            "\\n[INFO] 成功在 0x7FFF8B40 建立虛擬通道 -> Proxy: SOCKS5://103.24.51.9",
            "\\n[BYPASS] 偵測到 Cloudflare 高階 WAF 防禦防護層，啟動「流式代碼動態偽裝」技術...",
            "\\n[STATUS] 防火牆已成功繞過！(Bypass 100%) 進駐核心主控台。",
            "\\n[SCAN] 正在對 nasa.gov.secure 進行全面埠位掃描：",
            "       -> Port 80 (HTTP)    .... [OPEN]",
            "       -> Port 443 (HTTPS)  .... [SECURE]",
            "       -> Port 22 (SSH)     .... [VULNERABLE - EXPLOIT READY!]",
            "\\n[INJECT] 正在向 Port 22 注入隱形木馬程式 (Backdoor.Trojan.Lai.v8)...",
            "\\n[DATABASE] 攔截核心加密資料庫節點封包，正在下載資料群組：",
            "           Progress: [■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100% SECURE_LOG.DB",
            "\\n[DECRYPT] 啟動量子演算矩陣，嘗試暴力破解管理員密碼...",
            "          解密嘗試中... 0x9A4F... 0x11BC... 0x77EE...",
            "\\n[SUCCESS] 密碼解密破譯成功！ 系統密碼已重設為: LaiHang2026ProMatrix",
            "\\n[ACCESS] 成功獲取最高主機 Root 系統管理員權限！",
            "\\n[WARN] 偵測到反向追蹤異常警告！防衛機制啟動，自動刪除系統足跡(Logs)...",
            "\\n[CLEAR] 歷史日誌抹除完畢。任務完美達成。系統進入待命模式。"
        ];

        // 初始歡迎詞
        let currentText = "==================================================================\\n" +
                          "💀 首席網路安全專家：賴以航 (Yi-Hang Lai) | 黑客任務控制終端 v8.0\\n" +
                          "==================================================================\\n" +
                          ">> 系統已進入高度隱密狀態。\\n" +
                          ">> 【真・黑客提示】：請隨意在鍵盤上敲擊任意字母或按鍵！代碼會自動流出...\\n\\n" +
                          "lai-hang@matrix-terminal:~# <span class='cursor'></span>";
        
        terminal.innerHTML = currentText;

        let scriptIndex = 0;
        let charIndex = 0;
        let isTyping = false;

        // 當使用者敲擊鍵盤時，自動傾洩一段帥氣代碼
        function autoTypeHackerCode() {
            if (scriptIndex >= hackerScripts.length) {
                // 放煙火或循環
                scriptIndex = 0;
            }

            // 取得目前應該跑的那一段話
            let chunk = hackerScripts[scriptIndex];
            
            // 每次敲鍵盤，吐出 3 個字元，速度更快更有爽快感
            for(let k = 0; k < 4; k++) {
                if (charIndex < chunk.length) {
                    let nextChar = chunk.charAt(charIndex);
                    
                    // 處理換行或特殊符號
                    if (nextChar === '\\n') {
                        nextChar = '<br>';
                    }
                    
                    // 拔掉游標，塞入字元，補回游標
                    let base = terminal.innerHTML.replace("<span class=\\"cursor\\"></span>", "");
                    terminal.innerHTML = base + nextChar + "<span class=\\"cursor\\"></span>";
                    charIndex++;
                } else {
                    // 這一段吐完了，換下一段
                    scriptIndex++;
                    charIndex = 0;
                    break;
                }
            }
            
            // 自動滾動到最底端
            terminal.scrollTop = terminal.scrollHeight;
        }

        // 保持焦點在輸入監聽上
        document.body.addEventListener('click', () => {
            hiddenInput.focus();
        });
        
        // 核心監聽：只要有按鍵按下，就執行自動代碼生成
        document.addEventListener('keydown', (e) => {
            // 排除單純的功能鍵不觸發
            if (e.key !== 'Shift' && e.key !== 'Control' && e.key !== 'Alt' && e.key !== 'Meta') {
                autoTypeHackerCode();
            }
        });
    </script>
</body>
</html>
"""

# 3. 渲染全螢幕視窗（高度設定為 1000 像素，填滿大部分桌面螢幕）
components.html(html_code, height=1000, scrolling=False)
