import streamlit as st
import streamlit.components.v1 as components

# 1. 網頁頁面初始化設定（強制全螢幕、純黑背景）
st.set_page_config(page_title="究極黑客控制台 v17.5", page_icon="💀", layout="wide")

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

# 2. 全核心程式碼導入（超長15秒核心熔毀 + 專屬小鍵盤9鍵解鎖）
raw_html_code = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>Matrix Terminal Command Center v17.5</title>
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
        canvas { display: block; position: absolute; top: 0; left: 0; z-index: 1; opacity: 0.12; }
        
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
        
        /* 階段三：全新完全黑底特製效果遮罩層 */
        #fullscreen-fx-layer {
            display: none; position: absolute; top: 0; left: 0; width: 100%; height: 100vh; z-index: 100;
            background-color: #000000; padding: 50px; overflow-y: auto; color: #00ff00; font-size: 16px;
        }
        #fullscreen-fx-layer::-webkit-scrollbar { display: none; }
        
        /* 紅警自毀排版 */
        .nuke-title { color: #ff0055; font-size: 40px; font-weight: bold; text-align: center; margin-top: 10vh; text-shadow: 0 0 20px #ff0055; animation: red-flash 0.5s infinite; }
        .nuke-countdown { color: #ffffff; font-size: 120px; font-weight: bold; text-align: center; margin-top: 30px; text-shadow: 0 0 30px #ff0055; }
        @keyframes red-flash { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
        
        /* 全螢幕老電視縮線崩潰特效 */
        .screen-collapse { animation: tv-collapse 0.5s forwards ease-in; }
        @keyframes tv-collapse {
            0% { transform: scaleY(1) scaleX(1); filter: brightness(1); }
            60% { transform: scaleY(0.01) scaleX(1); filter: brightness(2); background: #fff; }
            100% { transform: scaleY(0) scaleX(0); filter: brightness(5); background: #fff; opacity: 0; }
        }
        
        /* 衛星影片科技風格濾鏡 */
        .video-container {
            position: relative; width: 560px; height: 315px; margin: 25px auto;
            border: 2px solid #00ff00; box-shadow: 0 0 30px rgba(0,255,0,0.3);
            filter: hue-rotate(60deg) contrast(1.2) sepia(0.2);
        }
        
        /* 劇烈搖晃效果（晶片大爆炸特別加強震盪感） */
        .nuke-alert-active { background: rgba(25,0,0,1) !important; animation: screen-shake 0.05s infinite !important; }
        .shake { animation: screen-shake 0.4s linear; }
        @keyframes screen-shake {
            0%, 100% { transform: translate(0, 0); }
            20% { transform: translate(-11px, 9px); }
            40% { transform: translate(11px, -9px); }
            60% { transform: translate(-10px, -5px); }
            80% { transform: translate(9px, 8px); }
        }
    </style>
</head>
<body>
    <canvas id="canvas"></canvas>
    
    <div id="terminal">
        <div class="log-line">========================================================================================</div>
        <div class="log-line">💀 遠端深層控制鏈主控台 v17.5 | 侵入成功後將自動解鎖 C2 全功能戰略面板</div>
        <div class="log-line">========================================================================================</div>
        <div id="dynamic-content"></div>
        <div id="status-display" class="status-panel">目前進度: [ 🧭 PHASE 1: 初始化全網子網段探測機制... ] [0%]</div>
        <div id="input-line">root@ghost-terminal:~# <span class="cursor"></span></div>
    </div>
    
    <input type="text" id="hidden-input" autofocus>
    
    <div id="c2-dashboard">
        <div class="panel-header">💀 [GHOST-NETWORK CENTRAL C2 PANEL v17.5] - ACCESS GRANTED 💀</div>
        <div class="panel-main">
            <div class="control-side">
                <div style="font-weight:bold; border-bottom: 1px solid #00ff00; padding-bottom:5px; margin-bottom:5px;">[ 戰略後門操控模組 ]</div>
                <button class="interactive-btn" onclick="triggerDump()">📂 數據導出 (Dump User Credentials)</button>
                <button class="interactive-btn" onclick="triggerSatellite()">衛星劫持 (Hijack Orbital Satellite)</button>
                <button class="interactive-btn" onclick="triggerClean()">🎭 換臉偽裝 (Wipe Terminal Traces)</button>
                <button class="interactive-btn" style="border-color:#ff0055; color:#ff0055;" onclick="triggerNuke()">💣 自毀程序 (Nuke Mainframe Server)</button>
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
        
        var lineCount = 0; var isUnlocked = false; var maxLines = 500;
        var alertCount = 0; var isDead = false;
        
        function triggerTerminalShake() { terminal.classList.add("shake"); setTimeout(function() { terminal.classList.remove("shake"); }, 400); }
        
        function appendNewLine() {
            if (isUnlocked || isDead) return;
            
            if (lineCount >= maxLines) {
                isUnlocked = true; terminal.style.display = "none";
                c2Dashboard.style.display = "grid";
                document.getElementById("c2-cmd-field").focus();
                return;
            }
            
            if (Math.random() < 0.008) {
                alertCount++;
                triggerTerminalShake();
                
                var div = document.createElement("div"); div.className = "log-line critical-alert";
                div.textContent = "[CRITICAL ALERT (" + alertCount + "/5)] !!! DETECTION WARNING: FIREWALL COUNTERMEASURE TRIGGERED... !!!";
                dynamicContent.appendChild(div); lineCount++;
                
                if (alertCount > 5) {
                    isDead = true;
                    openFxLayer();
                    fxLayer.classList.add("nuke-alert-active");
                    
                    var timeLeft = 15;
                    fxLayer.innerHTML = "<div style='text-align:center; color:#ff0055; font-size:45px; font-weight:bold; margin-top:15vh;'>" +
                                        "💥 [SYSTEM MELTDOWN: CRITICAL HARDWARE EXPLOSION] 💥<br>" +
                                        "<span style='font-size:22px; color:#fff;'>核心晶片正在承受不可逆的高壓過載熔毀...</span><br>" +
                                        "<div style='font-size:60px; color:#ff0055; margin-top:20px;' id='burn-timer'>15s</div>" +
                                        "<div style='font-size:14px; color:#ffaa00; margin-top:20px; animation:blink 0.3s infinite;'>[⚡ VOLTAGE OVERFLOW: 999% - MOTHERBOARD DESTROYING ⚡]</div></div>";
                    
                    var burnInterval = setInterval(function() {
                        timeLeft--;
                        var timerEl = document.getElementById("burn-timer");
                        if(timerEl) timerEl.textContent = timeLeft + "s";
                        if(timeLeft <= 0) { clearInterval(burnInterval); }
                    }, 1000);

                    // 15 秒大爆炸持續時間
                    setTimeout(function() {
                        clearInterval(burnInterval);
                        fxLayer.className = "dead-screen";
                        fxLayer.innerHTML = "YOU ARE DIED<div class='dead-sub'>按下 [ 小鍵盤 9 ] 以重新處理</div>";
                    }, 15000);
                    return;
                }
            } else {
                var div = document.createElement("div"); div.className = "log-line";
                div
