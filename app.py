import streamlit as st
import streamlit.components.v1 as components

# 1. 網頁頁面初始化設定
st.set_page_config(page_title="賴以航 究極黑客控制台 v7.1", page_icon="💻", layout="wide")

# 強制隱藏 Streamlit 的原生白邊與元件，確保 iframe 填滿
st.markdown("""
    <style>
    [data-testid="stHeader"], footer, #MainMenu {visibility: hidden !important;}
    .stApp {background-color: #000000 !important;}
    .block-container {padding: 0px !important; max-width: 100% !important;}
    iframe {display: block; border: none; width: 100vw; height: 100vh;}
    </style>
""", unsafe_allow_html=True)

# 2. 注入包含按鈕、指令、即時數據串流與【全自動流暢滾動】的核心 HTML/JS
html_code = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>Hacker Terminal Control Panel</title>
    <style>
        * { box-sizing: border-box; }
        body, html {
            margin: 0;
            padding: 0;
            background-color: #000;
            color: #00ff00;
            font-family: 'Courier New', Courier, monospace;
            width: 100%;
            height: 100vh;
            overflow-y: auto; /* 允許大視窗整體滾動 */
        }
        
        /* 隱藏原生網頁捲軸，保持純淨 */
        body::-webkit-scrollbar { display: none; }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 25px;
        }

        .header {
            text-align: center;
            border-bottom: 2px dashed #00ff00;
            padding-bottom: 15px;
            margin-bottom: 25px;
            text-shadow: 0 0 5px #00ff00;
        }

        .section-title {
            font-size: 20px;
            margin-top: 20px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
        }

        /* 按鈕特製樣式 */
        .btn-group {
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }
        .btn {
            background: transparent;
            border: 2px solid #00ff00;
            color: #00ff00;
            padding: 10px 20px;
            font-size: 15px;
            cursor: pointer;
            font-family: inherit;
            font-weight: bold;
            transition: all 0.3s;
            text-shadow: 0 0 3px #00ff00;
            box-shadow: 0 0 5px rgba(0,255,0,0.2);
        }
        .btn:hover {
            background: #00ff00;
            color: #000;
            box-shadow: 0 0 15px #00ff00;
        }

        /* 輸入框樣式 */
        .input-box {
            width: 100%;
            background: #050505;
            border: 1px solid #00ff00;
            color: #00ff00;
            padding: 12px;
            font-size: 16px;
            font-family: inherit;
            margin-bottom: 25px;
            outline: none;
            box-shadow: inset 0 0 5px rgba(0,255,0,0.3);
        }

        /* 🤖 即時網絡數據串流緩衝區 (加強版自動滾動容器) */
        #stream-buffer {
            background: rgba(0, 5, 0, 0.9);
            border: 1px solid #00ff00;
            height: 380px; /* 固定高度 */
            overflow-y: auto; /* 內部允許滾動 */
            padding: 15px;
            font-size: 16px;
            line-height: 1.5;
            white-space: pre-wrap;
            word-wrap: break-word;
            box-shadow: 0 0 15px rgba(0,255,0,0.1);
        }
        /* 隱藏緩衝區內建的捲軸 */
        #stream-buffer::-webkit-scrollbar { display: none; }

        .cursor {
            display: inline-block;
            background: #00ff00;
            width: 8px;
            height: 15px;
            animation: blink 0.8s infinite;
        }
        @keyframes blink {
            0%, 49% { background: #00ff00; }
            50%, 100% { background: transparent; }
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="header">
            <h2>💀 首席網路安全專家：賴以航 (Yi-Hang Lai)</h2>
            <p>SYSTEM STATUS: INFILTRATING... [核心控制終端 Matrix v7.1]</p>
        </div>

        <div class="section-title">📡 遠端滲透作戰指令</div>
        <div class="btn-group">
            <button class="btn" onclick="triggerAction('DDoS攻擊')">💥 執行 DDoS 癱瘓</button>
            <button class="btn" onclick="triggerAction('侵入資料庫')">🔓 侵入虛擬金庫</button>
            <button class="btn" onclick="triggerAction('解鎖飛彈')">🚀 解鎖核彈彈射井</button>
        </div>

        <div class="section-title">💻 控制台手動輸入指令 (輸入 help 試試)</div>
        <input type="text" class="input-box" id="cmd-input" placeholder="请输入 Linux 終端指令..." autofocus>

        <div class="section-title">🟩 即時網路數據串流緩衝區 (Live Console)</div>
        <div id="stream-buffer">>> 正在建立連線，同步安全日誌...<br><span class="cursor"></span></div>
    </div>

    <script>
        const buffer = document.getElementById('stream-buffer');
        const cmdInput = document.getElementById('cmd-input');

        // 🛠️ 【全自動向下滾動核心修復】：只要緩衝區HTML一變動，瞬間強制滾動到底部
        const observer = new MutationObserver(() => {
            buffer.scrollTop = buffer.scrollHeight;
            window.scrollTo(0, document.body.scrollHeight); // 同步把大網頁也往下推
        });
        observer.observe(buffer, { childList: true, subtree: true });

        // 黑客代碼池
        const tags = ['INFO', 'WARN', 'SYSTEM', 'INJECT', 'DECRYPT', 'BYPASS'];
        const scripts = [
            "connect_to_proxy_node('SOCKS5://103.24.51.9', port=22);",
            "if (auth_token == 'BYPASS_TRUE') { grant_root_access(); }",
            "AES_256_Decrypt(key_matrix, cipher_text, chunk_size=4096);",
            "iptables -A INPUT -s 127.0.0.1 -j DROP # Erasing footprints",
            "send_packet_stream(target_ip, protocol='UDP', packets=99999);"
        ];

        // 隨機噴射代碼函數
        function appendHackerLine() {
            const hexAddr = '0x' + Math.floor(Math.random()*16777215).toString(16).toUpperCase();
            const tag = tags[Math.floor(Math.random()*tags.length)];
            const script = scripts[Math.floor(Math.random()*scripts.length)];
            
            let base = buffer.innerHTML.replace('<span class="cursor"></span>', '');
            buffer.innerHTML = base + `\\n[${tag}] [ADDR:${hexAddr}] 正在執行：${script}<span class="cursor"></span>`;
        }

        // 讓代碼源源不絕自動跑起來！
        setInterval(appendHackerLine, 250);

        // 點擊作戰按鈕觸發
        function triggerAction(actionName) {
            let base = buffer.innerHTML.replace('<span class="cursor"></span>', '');
            buffer.innerHTML = base + `\\n\\n[🔥 ACTION触发] >>> 正在全力執行【${actionName}】作戰計劃...任務啟動！\\n<span class="cursor"></span>`;
        }

        // 監聽鍵盤輸入框
        cmdInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                const cmd = cmdInput.value.trim().toLowerCase();
                let reply = '';

                if (cmd === 'help') {
                    reply = `\\n\\n[SYSTEM] 可用指令清單：\\n - scan : 掃描目標主機通訊埠\\n - bypass : 繞過防火牆\\n - clear : 清除系統日誌\\n`;
                } else if (cmd === 'scan') {
                    reply = `\\n\\n[SYSTEM] 正在全面掃描 nasa.gov.secure... 發現 Port 22, 80, 443 開放中！\\n`;
                } else if (cmd === 'bypass') {
                    reply = `\\n\\n[SYSTEM] 🔥 成功繞過 Cloudflare 防火牆核心防禦層！\\n`;
                } else if (cmd === 'clear') {
                    buffer.innerHTML = `>> 終端機日誌已清空。<br><span class="cursor"></span>`;
                    cmdInput.value = '';
                    return;
                } else if (cmd !== '') {
                    reply = `\\n\\n[ERROR] 未知指令: '${cmd}'。輸入 help 獲取支援。\\n`;
                }

                if (reply) {
                    let base = buffer.innerHTML.replace('<span class="cursor"></span>', '');
                    buffer.innerHTML = base + reply + '<span class="cursor"></span>';
                }
                cmdInput.value = ''; // 清空輸入框
            }
        });
    </script>
</body>
</html>
"""

# 3. 渲染控制台視窗
components.html(html_code, height=950, scrolling=True)
