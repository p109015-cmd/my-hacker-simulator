import streamlit as st
import streamlit.components.v1 as components

# 1. 網頁頁面初始化設定（強制全螢幕、純黑背景）
st.set_page_config(page_title="究極黑客控制台 v17.4", page_icon="💀", layout="wide")

# 強制隱藏 Streamlit 的所有原生網頁 UI
st.markdown(
    """
    <style>
    [data-testid="stHeader"], footer, #MainMenu {visibility: hidden !important;}
    .stApp {background-color: #000000 !important;}
    .block-container {padding: 0px !important; max-width: 100% !important; margin: 0px !important;}
    
    [data-testid="stHtmlBlock"], [data-testid="stElementContainer"], iframe {
        width: 100% !important;
        height: 100vh !important;
        display: block !important;
        border: none !important;
    }
    body { overflow: hidden !important; }
    </style>
    """, 
    unsafe_allow_html=True
)

# 2. 全核心程式碼導入
raw_html_code = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>Matrix Terminal Command Center v17.4</title>
    <style>
        * { box-sizing: border-box; }
        body, html {
            margin: 0; padding: 0; background-color: #000; overflow: hidden;
            width: 100%; height: 100vh; font-family: "Courier New", Courier, monospace;
        }
        body::before {
            content: " "; display: block; position: fixed; top: 0; left: 0; bottom: 0; right: 0;
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.05), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.05));
            z-index: 99999; background-size: 100% 4px, 6px 100%; pointer-events: none;
        }
        canvas.bg-matrix { display: block; position: absolute; top: 0; left: 0; z-index: 1; opacity: 0.12; }
        
        /* 階段一：黑客入侵終端 */
        #terminal {
            position: absolute; top: 0; left: 0; width: 100%; height: 100vh; z-index: 2;
            padding: 40px; color: #00ff00; font-size: 16px; line-height: 1.5;
            overflow-y: auto; white-space: pre-wrap; word-wrap: break-word;
            text-shadow: 0 0 6px rgba(0,255,0,0.8);
        }
        #terminal::-webkit-scrollbar { display: none; }
        .cursor { display: inline-block; background-color: #00ff00; width: 10px; height: 16px; animation: blink 0.8s infinite; vertical-align: middle; }
        @keyframes blink { 0%, 49% { background-color: #00ff00; } 50%, 100% { background-color: transparent; } }
        .critical-alert { color: #ff0055 !important; font-weight: bold; text-shadow: 0 0 10px #ff0055 !important; animation: glitch-flash 0.2s 2; }
        @keyframes glitch-flash { 0%, 100% { opacity: 1; background: rgba(255,0,85,0.15); } 50% { opacity: 0.3; background: transparent; } }
        .status-panel { color: #1aff1a; font-weight: bold; background: rgba(0, 40, 0, 0.4); padding: 10px; border-left: 4px solid #00ff00; margin-top: 15px; margin-bottom: 15px; }
        
        /* F1 特製隱藏後門打字框彈窗 */
        #backdoor-modal {
            display: none; position: fixed; top: 40%; left: 50%; transform: translate(-50%, -50%);
            background: rgba(0, 20, 0, 0.95); border: 2px solid #00ff00; padding: 25px; z-index: 10000;
            box-shadow: 0 0 30px rgba(0,255,0,0.7); width: 350px; text-align: center;
        }
        .backdoor-input {
            width: 100%; background: #000; border: 1px solid #00ff00; color: #00ff00;
            padding: 10px; font-family: inherit; font-size: 18px; text-align: center; outline: none; margin-top: 15px;
        }

        /* 突發事件過載死亡畫面 */
        .dead-screen {
            background-color: #000000 !important; color: #ff0055 !important;
            font-size: 45px; font-weight: bold; text-align: center; padding-top: 35vh;
            text-shadow: 0 0 20px #ff0055; animation: red-flash 0.4s infinite;
        }
        .dead-sub { font-size: 20px; color: #ffffff; margin-top: 20px; text-shadow: 0 0 5px #fff; }
        
        /* 階段二：解鎖後的 C2 主控面板 */
        #c2-dashboard {
            display: none; position: absolute; top: 0; left: 0; width: 100%; height: 100vh; z-index: 10; 
            padding: 30px; color: #00ff00; background: rgba(0,0,0,0.95); border: 2px solid #00ff00;
            grid-template-rows: auto 1fr auto; gap: 20px; box-shadow: 0 0 50px rgba(0,255,0,0.4);
            animation: panel-appear 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.15);
        }
        @keyframes panel-appear { 0% { transform: scale(0.95); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }
        .panel-header { font-size: 24px; text-align: center; border-bottom: 2px dashed #00ff00; padding-bottom: 10px; font-weight: bold; letter-spacing: 2px; }
        .panel-main { display: grid; grid-template-columns: 1fr 2fr; gap: 20px; height: 100%; overflow: hidden; }
        .control-side { display: flex; flex-direction: column; gap: 15px; background: rgba(0,20,0,0.5); padding: 20px; border: 1px solid #00aa00; }
        .interactive-btn {
            background: #002200; color: #00ff00; border: 1px solid #00ff00; padding: 12px; font-size: 15px;
            font-family: inherit; font-weight: bold; cursor: pointer; text-align: left; transition: all 0.2s;
        }
        .interactive-btn:hover { background: #00ff00; color: #000; box-shadow: 0 0 15px #00ff00; }
        .console-side { display: flex; flex-direction: column; background: #000; border: 1px solid #00ff00; padding: 15px; }
        .console-output { flex: 1; overflow-y: auto; font-size: 14px; line-height: 1.4; color: #33ff33; margin-bottom: 10px; border-bottom: 1px solid #005500; padding-bottom: 5px; }
        .console-input-area { display: flex; gap: 10px; align-items: center; }
        .c2-input { flex: 1; background: #001100; border: 1px solid #00ff00; color: #00ff00; padding: 8px; font-family: inherit; font-size: 15px; outline: none; }
        
        /* 階段三：全黑底特製效果遮罩層 */
        #fullscreen-fx-layer {
            display: none; position: absolute; top: 0; left: 0; width: 100%; height: 100vh; z-index: 100;
            background-color: #000000; padding: 50px; overflow-y: auto; color: #00ff00; font-size: 16px;
        }
        #fullscreen-fx-layer::-webkit-scrollbar { display: none; }
        
        /* 紅警自毀排版 */
        .nuke-title { color: #ff0055; font-size: 30px; font-weight: bold; text-align: center; margin-top: 10vh; text-shadow: 0 0 20px #ff0055; animation: red-flash 0.5s infinite; }
        .nuke-countdown { color: #ffffff; font-size: 120px; font-weight: bold; text-align: center; margin-top: 30px; text-shadow: 0 0 30px #ff0055; }
        @keyframes red-flash { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
        
        /* 全螢幕老電視縮線崩潰特效 */
        .screen-collapse { animation: tv-collapse 0.5s forwards ease-in; }
        @keyframes tv-collapse {
            0% { transform: scaleY(1) scaleX(1); filter: brightness(1); }
            60% { transform: scaleY(0.01) scaleX(1); filter: brightness(2); background: #fff; }
            100% { transform: scaleY(0) scaleX(0); filter: brightness(5); background: #fff; opacity: 0; }
        }
        
        /* 衛星雷達繪圖容器 */
        .radar-container {
            position: relative; width: 560px; height: 315px; margin: 25px auto;
            border: 2px solid #00ff00; box-shadow: 0 0 30px rgba(0,255,0,0.6);
            background: #000; overflow: hidden;
        }
        #satRadarCanvas { width: 100%; height: 100%; display: block; }
        
        /* 劇烈搖晃效果 */
        .nuke-alert-active { background: rgba(25,0,0,1) !important; animation: screen-shake 0.06s infinite !important; }
        .shake { animation: screen-shake 0.4s linear; }
        @keyframes screen-shake {
            0%, 100% { transform: translate(0, 0); }
            20% { transform: translate(-10px, 9px); }
            40% { transform: translate(10px, -8px); }
            60% { transform: translate(-9px, -4px); }
            80% { transform: translate(8px, 7px); }
        }
    </style>
</head>
<body>
    <canvas id="canvas" class="bg-matrix"></canvas>
    
    <div id="backdoor-modal">
        <div style="font-size:14px; color:#00ff00; font-weight:bold; letter-spacing:1px;">⚠️ [OVERRIDE BYPASS TERMINAL]</div>
        <div style="font-size:12px; color:#ff0055; margin-top:5px; font-weight:bold; animation:blink 0.5s infinite;">警告：密碼錯誤將立即引發系統自爆！</div>
        <input type="password" id="backdoor-field" class="backdoor-input" placeholder="********" onkeydown="checkBackdoorToken(event)">
    </div>

    <div id="terminal">
        <div class="log-line">========================================================================================</div>
        <div class="log-line">💀 遠端深層控制鏈主控台 v17.4 | 侵入成功後將自動解鎖 C2 全功能戰略面板</div>
        <div class="log-line">========================================================================================</div>
        <div id="dynamic-content"></div>
        <div id="status-display" class="status-panel">目前進度: [ 🧭 PHASE 1: 初始化全網子網段探測機制... ] [0%]</div>
        <div id="input-line">root@ghost-terminal:~# <span class="cursor"></span></div>
    </div>
    
    <input type="text" id="hidden-input" autofocus>
    
    <div id="c2-dashboard">
        <div class="panel-header">💀 [GHOST-NETWORK CENTRAL C2 PANEL v17.4] - ACCESS GRANTED 💀</div>
        <div class="panel-main">
            <div class="control-side">
                <div style="font-weight:bold; border-bottom: 1px solid #00ff00; padding-bottom:5px; margin-bottom:5px;">[ 戰略後門操控模組 ]</div>
                <button class="interactive-btn" onclick="triggerDump()">📂 數據導出 (Dump User Credentials)</button>
                <button class="interactive-btn" onclick="triggerSatellite()">衛星劫持 (Hijack Orbital Satellite)</button>
                <button class="interactive-btn" onclick="triggerClean()">🎭 換臉偽裝 (Wipe Terminal Traces)</button>
                <button class="interactive-btn" style="border-color:#ff0055; color:#ff0055;" onclick="triggerManualNuke()">💣 自毀程序 (Nuke Mainframe Server)</button>
                <div style="font-size:12px; color:#00aa00; margin-top:auto;">系統狀態: 在線 (ENCRYPTED)<br>中繼節點: SOCKS5://103.24.51.9</div>
            </div>
            <div class="console-side">
                <div class="console-output" id="c2-output">
                    [SYSTEM] 成功對接主機。點擊左側按鈕即可切換至【獨立全黑底功能模式】下達戰略威脅...<br>
                    提示指令：help, download_all, clear
                </div>
                <div class="console-input-area">
                    <span>c2-admin#</span>
                    <input type="text" class="c2-input" id="c2-cmd-field" placeholder="輸入內部指令並按 Enter..." onkeydown="handleC2Command(event)">
                </div>
            </div>
        </div>
    </div>
    
    <div id="fullscreen-fx-layer"></div>
    
    <script>
        var canvas = document.getElementById("canvas");
        var ctx = canvas.getContext("2d");
        function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
        resizeCanvas(); window.addEventListener("resize", resizeCanvas);
        
        var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789🧬💀🛰️🔥🔓🚀💥⚡🛸⚙️☣️";
        var alphabet = chars.split("");
        var columns = canvas.width / 16;
        var rainDrops = Array(Math.floor(columns)).fill(1);
        var mouseParticles = [];
        
        window.addEventListener("mousemove", function(e) {
            if (Math.random() > 0.4) {
                mouseParticles.push({ x: e.clientX, y: e.clientY, text: alphabet[Math.floor(Math.random() * alphabet.length)], alpha: 1.0, size: 14 });
            }
        });
        
        function drawMatrix() {
            ctx.fillStyle = "rgba(0, 0, 0, 0.06)"; ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = "#0F0"; ctx.font = "16px monospace";
            for (var i = 0; i < rainDrops.length; i++) {
                var text = alphabet[Math.floor(Math.random() * alphabet.length)];
                ctx.fillText(text, i * 16, rainDrops[i] * 16);
                if (rainDrops[i] * 16 > canvas.height && Math.random() > 0.98) rainDrops[i] = 0;
                rainDrops[i]++;
            }
            for (var i = 0; i < mouseParticles.length; i++) {
                var p = mouseParticles[i]; ctx.fillStyle = "rgba(0, 255, 0, " + p.alpha + ")";
                ctx.font = "bold " + p.size + "px monospace"; ctx.fillText(p.text, p.x, p.y);
                p.alpha -= 0.02; p.y += 0.5;
            }
            mouseParticles = mouseParticles.filter(function(p) { return p.alpha > 0; });
        }
        setInterval(drawMatrix, 33);
        
        var terminal = document.getElementById("terminal");
        var dynamicContent = document.getElementById("dynamic-content");
        var hiddenInput = document.getElementById("hidden-input");
        var statusDisplay = document.getElementById("status-display");
        var c2Dashboard = document.getElementById("c2-dashboard");
        var fxLayer = document.getElementById("fullscreen-fx-layer");
        var c2Output = document.getElementById("c2-output");
        var backdoorModal = document.getElementById("backdoor-modal");
        var backdoorField = document.getElementById("backdoor-field");
        
        var lineCount = 0; var isUnlocked = false; var maxLines = 500;
        var alertCount = 0; var isDead = false;
        var radarIntervalId = null; // 雷達繪圖排程計時器
        
        function triggerTerminalShake() { terminal.classList.add("shake"); setTimeout(function() { terminal.classList.remove("shake"); }, 400); }
        
        function enterC2Panel() {
            isUnlocked = true; 
            terminal.style.display = "none";
            backdoorModal.style.display = "none";
            c2Dashboard.style.display = "grid";
            document.getElementById("c2-cmd-field").focus();
        }

        function appendNewLine() {
            if (isUnlocked || isDead) return;
            if (lineCount >= maxLines) { enterC2Panel(); return; }
            
            if (Math.random() < 0.008) {
                alertCount++;
                triggerTerminalShake();
                var div = document.createElement("div"); div.className = "log-line critical-alert";
                div.textContent = "[CRITICAL ALERT (" + alertCount + "/5)] !!! DETECTION WARNING: FIREWALL COUNTERMEASURE TRIGGERED... !!!";
                dynamicContent.appendChild(div); lineCount++;
                if (alertCount > 5) { triggerMeltdownBurn(); }
            } else {
                var div = document.createElement("div"); div.className = "log-line";
                div.textContent = "[SYSTEM_CORE] [OK] 注入核心控制流協定因子，正在重構核心記憶體指標...";
                dynamicContent.appendChild(div); lineCount++;
            }
            var pct = Math.floor((lineCount / maxLines) * 100);
            statusDisplay.textContent = "目前進度: [ ⚡ PHASE " + (Math.floor(pct/20)+1) + ": 核心矩陣協議破解中... ] [" + pct + "%]";
            document.getElementById("input-line").scrollIntoView({ behavior: "smooth", block: "end" });
        }
        
        function triggerMeltdownBurn() {
            isDead = true;
            openFxLayer();
            fxLayer.classList.add("nuke-alert-active");
            backdoorModal.style.display = "none";
            
            var timeLeft = 15;
            fxLayer.innerHTML = "<div id='burn-panel' style='text-align:center; color:#ff0055; font-size:38px; font-weight:bold; margin-top:12vh; line-height:1.6;'>" +
                                "💥 [SECURITY VIOLATION: HARDWARE MELTDOWN INITIATED] 💥<br>" +
                                "<span style='font-size:20px; color:#fff;'>特權金鑰錯誤或防禦過載！核心晶片正在承受不可逆高壓熔毀...</span><br>" +
                                "<div style='font-size:90px; color:#ff0055; margin-top:25px; font-weight:900;' id='burn-timer'>15s</div>" +
                                "<div style='font-size:14px; color:#ffaa00; margin-top:25px; animation:blink 0.3s infinite;'>[⚡ VOLTAGE OVERFLOW: 999% - MOTHERBOARD DESTROYING ⚡]</div></div>";
            
            var burnInterval = setInterval(function() {
                timeLeft--;
                var timerEl = document.getElementById("burn-timer");
                if(timerEl) timerEl.textContent = timeLeft + "s";
                if(timeLeft <= 0) { clearInterval(burnInterval); }
            }, 1000);

            setTimeout(function() {
                clearInterval(burnInterval);
                fxLayer.className = "dead-screen";
                fxLayer.innerHTML = "SYSTEM COMPONENT DESTROYED<div class='dead-sub'>核心已徹底熔毀。按下 [ 小鍵盤 9 ] 以重組硬體面板</div>";
            }, 15000);
        }

        document.body.addEventListener("click", function(e) { 
            if(backdoorModal.contains(e.target)) return;
            if(!isUnlocked && !isDead) hiddenInput.focus(); 
        });
        
        document.addEventListener("keydown", function(e) {
            if (e.key === "F1") {
                e.preventDefault();
                if(!isUnlocked && !isDead) { backdoorModal.style.display = "block"; backdoorField.focus(); }
                return;
            }
            if (isDead) {
                if (e.code === "Numpad9") { stopRadar(); location.reload(); }
                return;
            }
            if (backdoorModal.style.display === "block") return;
            if (!isUnlocked && e.key !== "Shift" && e.key !== "Control" && e.key !== "Alt" && e.key !== "Meta") {
                for(var i=0; i<5; i++) { appendNewLine(); }
            }
        });
        
        function checkBackdoorToken(e) {
            if (e.key === "Enter") {
                if (backdoorField.value === "1030622") {
                    lineCount = maxLines;
                    statusDisplay.textContent = "目前進度: [ ⚡ PHASE 5: 核心矩陣協議破解中... ] [100%]";
                    setTimeout(function() { enterC2Panel(); }, 300);
                } else {
                    triggerMeltdownBurn();
                }
            } else if (e.key === "Escape") {
                backdoorField.value = ""; backdoorModal.style.display = "none"; hiddenInput.focus();
            }
        }

        function openFxLayer() { 
            stopRadar();
            c2Dashboard.style.display = "none"; 
            fxLayer.style.display = "block"; 
            fxLayer.innerHTML = ""; 
            fxLayer.className = ""; 
        }

        function stopRadar() {
            if(radarIntervalId) { clearInterval(radarIntervalId); radarIntervalId = null; }
        }
        
        /* C2 Panel 按鈕功能模組 */
        function triggerDump() {
            openFxLayer();
            var count = 0;
            var timer = setInterval(function() {
                var d = document.createElement("div"); d.style.color = "#33ff33"; d.style.fontSize = "14px"; d.style.marginBottom = "2px";
                d.textContent = "[STREAM_DUMP] UID_" + Math.floor(Math.random()*89999+10000) + " | IP: " + Math.floor(Math.random()*254+1) + "." + Math.floor(Math.random()*254) + ".71." + Math.floor(Math.random()*254) + " | PASS_HASH: " + Math.random().toString(16).substring(2,15).toUpperCase() + " | EXPORT: SUCCESS";
                fxLayer.appendChild(d); fxLayer.scrollTop = fxLayer.scrollHeight; count++;
                if(count >= 150) { 
                    clearInterval(timer);
                    var endMsg = document.createElement("div"); endMsg.style.color = "#00ff00"; endMsg.style.fontSize = "20px"; endMsg.style.marginTop = "20px"; endMsg.style.fontWeight = "bold";
                    endMsg.innerHTML = "<br>💀 [DATA EXPORT COMPLETE] 數據庫已完全拖庫成功。<br><button onclick='backToC2()' style='background:#003300; color:#00ff00; border:1px solid #00ff00; padding:10px; margin-top:15px; cursor:pointer;'>返回主控面板</button>";
                    fxLayer.appendChild(endMsg); fxLayer.scrollTop = fxLayer.scrollHeight;
                }
            }, 25);
        }
        
        /* 2. 衛星劫持：全面改用 100% 機密獨立純前端 Canvas 雷達模擬，保證不依賴外部任何影片網址 */
        function triggerSatellite() {
            openFxLayer();
            var pct = 0; 
            var container = document.createElement("div"); 
            container.style.textAlign = "center"; container.style.marginTop = "3vh";
            container.innerHTML = '<h2 style="letter-spacing:3px;">🛰️ [ORBITAL SATELLITE HIJACK PROTOCOL]</h2>' +
                                   '<div style="font-size:14px; color:#00aa00; margin-bottom:10px;">系統已切換至虛擬矩陣接收器，正實時渲染軌道特種光學雷達影像...</div>' +
                                   '<div class="radar-container">' +
                                   '  <canvas id="satRadarCanvas" width="560" height="315"></canvas>' +
                                   '</div>' +
                                   '<div id="sat-progress-bar" style="width:60%; margin:0 auto; border:1px solid #00ff00; padding:3px; text-align:left;"><div id="sat-fill" style="width:0%; background:#00ff00; height:18px;"></div></div>' +
                                   '<div id="sat-pct" style="margin-top:5px; font-size:20px;">0%</div>' +
                                   '<div id="sat-details" style="margin-top:15px; font-size:13px; text-align:left; width:60%; margin-left:auto; margin-right:auto; color:#33ff33; height:110px; overflow-y:auto; border-top:1px dashed #005500; padding-top:10px;"></div>';
            fxLayer.appendChild(container);
            
            // 啟動自畫雷達渲染引擎
            initRadarEngine();
            
            var fill = document.getElementById("sat-fill"); 
            var pctText = document.getElementById("sat-pct"); 
            var details = document.getElementById("sat-details");
            
            var timer = setInterval(function() {
                pct += 2; fill.style.width = pct + "%"; pctText.textContent = pct + "%";
                if(pct % 10 === 0) { 
                    details.innerHTML += "&gt;&gt; 光學反饋接收中... 經緯鎖定: " + (Math.random()*180).toFixed(4) + "°N, " + (Math.random()*90).toFixed(4) + "°E | 訊號強度: [EXCELLENT]<br>"; 
                    details.scrollTop = details.scrollHeight; 
                }
                if(pct >= 100) { 
                    clearInterval(timer); 
                    details.innerHTML += "<br><span style='color:#ffffff; font-size:16px; font-weight:bold;'>🛰️ [HIJACK SUCCESS] 衛星鎖定機制已固化，全球戰術掃描儀常駐在線！</span><br><button onclick='backToC2()' style='background:#003300; color:#00ff00; border:1px solid #00ff00; padding:10px; margin-top:15px; cursor:pointer;'>返回主控面板</button>"; 
                    details.scrollTop = details.scrollHeight; 
                }
            }, 60);
        }
        
        // 純前端模擬軍事雷達掃描動畫（不耗網路流量，100% 成功率）
        function initRadarEngine() {
            var rCanvas = document.getElementById("satRadarCanvas");
            if(!rCanvas) return;
            var rCtx = rCanvas.getContext("2d");
            var angle = 0;
            
            // 隨機產生一些代表地面目標點的座標
            var targets = [];
            for(var i=0; i<12; i++) {
                targets.push({
                    x: Math.random() * (rCanvas.width - 100) + 50,
                    y: Math.random() * (rCanvas.height - 60) + 30,
                    size: Math.random() * 3 + 2,
                    alpha: Math.random()
                });
            }

            radarIntervalId = setInterval(function() {
                // 1. 純黑背景覆蓋
                rCtx.fillStyle = "rgba(0, 0, 0, 0.15)";
                rCtx.fillRect(0, 0, rCanvas.width, rCanvas.height);
                
                var cx = rCanvas.width / 2;
                var cy = rCanvas.height / 2;
                
                // 2. 畫雷達同心圓線條
                rCtx.strokeStyle = "rgba(0, 255, 0, 0.2)";
                rCtx.lineWidth = 1;
                for(var r = 40; r <= 150; r += 40) {
                    rCtx.beginPath(); rCtx.arc(cx, cy, r, 0, Math.PI * 2); rCtx.stroke();
                }
                
                // 十字星準心線
                rCtx.beginPath(); rCtx.moveTo(cx - 180, cy); rCtx.lineTo(cx + 180, cy); rCtx.stroke();
                rCtx.beginPath(); rCtx.moveTo(cx, cy - 140); rCtx.lineTo(cx, cy + 140); rCtx.stroke();
                
                // 3. 畫隨機掃描到的軍事目標點
                for(var i=0; i<targets.length; i++) {
                    var t = targets[i];
                    rCtx.fillStyle = "rgba(0, 255, 50, " + t.alpha + ")";
                    rCtx.beginPath();
                    rCtx.arc(t.x, t.y, t.size, 0, Math.PI*2);
                    rCtx.fill();
                    // 加上科幻小外框
                    if(t.alpha > 0.5) {
                        rCtx.strokeStyle = "rgba(0, 255, 0, " + (t.alpha - 0.3) + ")";
                        rCtx.strokeRect(t.x - t.size - 2, t.y - t.size - 2, t.size*2 + 4, t.size*2 + 4);
                    }
                    // 動態閃爍
                    if(Math.random() > 0.9) t.alpha = Math.random();
                }
                
                // 4. 畫旋轉掃描光束
                angle += 0.04;
                var bx = cx + Math.cos(angle) * 220;
                var by = cy + Math.sin(angle) * 220;
                
                var gradient = rCtx.createLinearGradient(cx, cy, bx, by);
                gradient.addColorStop(0, "rgba(0, 255, 0, 0.6)");
                gradient.addColorStop(1, "rgba(0, 255, 0, 0.0)");
                
                rCtx.strokeStyle = gradient;
                rCtx.lineWidth = 3;
                rCtx.beginPath(); rCtx.moveTo(cx, cy); rCtx.lineTo(bx, by); rCtx.stroke();
                
                // 5. 左上角加上雜訊文字
                rCtx.fillStyle = "#00ff00";
                rCtx.font = "11px monospace";
                rCtx.fillText("SAT-ID: ORBIT-GHOST-X9", 15, 20);
                rCtx.fillText("ALTITUDE: 42,164 KM", 15, 35);
                rCtx.fillText("SYS_LOCK: ACTIVE", 15, 50);
                
                // 右下角加上掃描經緯度數據變動
                rCtx.fillText("LAT: " + (Math.sin(angle)*90).toFixed(4), rCanvas.width - 140, rCanvas.height - 35);
                rCtx.fillText("LNG: " + (Math.cos(angle)*180).toFixed(4), rCanvas.width - 140, rCanvas.height - 20);
                
            }, 30);
        }
        
        function triggerManualNuke() {
            openFxLayer(); fxLayer.classList.add("nuke-alert-active");
            var nukeTitle = document.createElement("div"); nukeTitle.className = "nuke-title"; nukeTitle.textContent = "☣️ [CRITICAL SYSTEM OVERLOAD - HOSTILE NUKE COMMAND] ☣️"; fxLayer.appendChild(nukeTitle);
            var nukeCount = document.createElement("div"); nukeCount.className = "nuke-countdown"; nukeCount.textContent = "5"; fxLayer.appendChild(nukeCount);
            var countdown = 5;
            var timer = setInterval(function() {
                countdown--; if(countdown >= 0) nukeCount.textContent = countdown;
                if(countdown < 0) { clearInterval(timer); nukeTitle.textContent = "💥 [CORE COLLAPSE - SERVER DESTROYED] 💥"; nukeCount.style.display = "none"; document.body.className = "screen-collapse"; setTimeout(function() { location.reload(); }, 600); }
            }, 800);
        }
        
        function triggerClean() { openFxLayer(); fxLayer.innerHTML = "<div style='text-align:center; margin-top:30vh; font-size:20px; color:#00ff00;'>[+] 正在抹除反向連線 Session 指標...<br>[+] 正在清洗 C2 本地歷史緩衝暫存區...<br>[+] 軌跡完全清除完畢。系統即將重新啟動...</div>"; setTimeout(function() { location.reload(); }, 1200); }
        function backToC2() { stopRadar(); fxLayer.style.display = "none"; c2Dashboard.style.display = "grid"; document.getElementById("c2-cmd-field").focus(); }
        function logC2(text) { const p = document.createElement("p"); p.style.margin = "4px 0"; p.innerHTML = text; c2Output.appendChild(p); c2Output.scrollTop = c2Output.scrollHeight; }
        
        function handleC2Command(e) {
            if (e.key === "Enter") {
                var input = document.getElementById("c2-cmd-field"); var cmd = input.value.trim().toLowerCase(); if (!cmd) return;
                logC2("<span style='color:#ffffff'>c2-admin# " + input.value + "</span>"); input.value = "";
                if (cmd === "help") logC2("內建高級指令: <b>download_all</b>, <b>clear</b>");
                else if (cmd === "download_all") logC2("[+] 建立多線程快取隊列... [■■■■■■■■■■■■■■■■] 100% 傳輸完成。");
                else if (cmd === "clear") c2Output.innerHTML = "";
                else logC2("[!] 指令已封裝為虛擬例外，異步盲發送至主機端...");
            }
        }
        setTimeout(function() { hiddenInput.focus(); }, 200);
    </script>
</body>
</html>
"""

components.html(raw_html_code, height=850)
