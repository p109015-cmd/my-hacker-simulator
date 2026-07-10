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

# 2. 全核心程式碼導入（限制只能使用小鍵盤 9 鍵修復）
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
        
        /* 劇烈搖晃效果（晶片爆炸特別加重振幅） */
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
    <canvas id="canvas"></canvas>
    
    <div id="terminal">
        <div class="log-line">========================================================================================</div>
        <div class="log-line">💀 遠端深層控制鏈主控台 v17.4 | 侵入成功後將自動解鎖 C2 全功能戰略面板</div>
        <div class="log-line">========================================================================================</div>
        <div id="dynamic-content"></div>
        <div id="status-display" class="status-panel">目前進度: [ 🧭 PHASE 1: 初始化全網子網段探測機制... ] [0%]</div>
        <div id="input-line">root@ghost-terminal:~# <span class="cursor"></span></div>
    </div>
    
    <input type="text" id="hidden-input" autofocus>
    
    <div id="c
