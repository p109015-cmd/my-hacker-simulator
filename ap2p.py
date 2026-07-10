import streamlit as st
import time
import random

# 1. 網頁頁面初始化設定
st.set_page_config(page_title="賴以航 終極黑客控制台 Pro+", page_icon="💀", layout="centered")

# --- 🎯 終極視覺魔法：強行覆蓋全網頁為黑底綠字 ---
st.markdown("""
    <style>
    /* 全網頁底色與主文字 */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #000000 !important;
        color: #00FF00 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    
    /* 側邊欄改為極深黑底與綠字 */
    [data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid #00FF00 !important;
    }
    [data-testid="stSidebar"] * {
        color: #00FF00 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }

    /* 所有標題與內文一律強制變成螢光綠 */
    h1, h2, h3, h4, h5, h6, p, span, label, .stMarkdown {
        color: #00FF00 !important;
    }

    /* 輸入框（Text Input）造型調整 */
    input {
        background-color: #111111 !important;
        color: #00FF00 !important;
        border: 1px solid #00FF00 !important;
    }

    /* 按鈕元件暗黑螢光綠特殊樣式 */
    button, div.stButton > button {
        background-color: #000000 !important;
        color: #00FF00 !important;
        border: 1px solid #00FF00 !important;
        border-radius: 4px !important;
        transition: all 0.3s ease;
    }
    button:hover, div.stButton > button:hover {
        background-color: #00FF00 !important;
        color: #000000 !important;
        box-shadow: 0 0 10px #00FF00 !important;
    }
    
    /* 強化 code 區塊的黑底綠字效果 */
    code, pre {
        background-color: #111111 !important;
        color: #00FF00 !important;
        border: 1px solid #003300 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 【核心開發者：賴以航 原生控制台區塊】 ---
with st.container(border=True):
    st.subheader("💀 首席網路安全專家：賴以航 (Yi-Hang Lai)")
    st.caption("⚡ SYSTEM STATUS: INFILTRATING... | 核心技術：動態流式代碼偽裝與密碼矩陣破譯")

st.title("💻 駭客任務控制終端 Matrix v6.0")
st.write(">> 警告：本終端已全面進入高度隱密模式，所有傳輸數據皆過濾為經典矩陣視訊。")
st.write("---")

# 2. 側邊欄：密碼矩陣破譯小工具
st.sidebar.title("🔑 密碼破譯面板")
crack_target = st.sidebar.text_input("輸入要破譯的密碼名稱：", "Pentagon_Admin_Pass")

if st.sidebar.button("💥 啟動暴力破譯"):
    st.sidebar.write(">> 正在載入密碼字典檔...")
    crack_bar = st.sidebar.progress(0)
    
    placeholder = st.sidebar.empty()
    for i in range(100):
        fake_pass = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*", k=10))
        placeholder.text(f"🔑 嘗試中: {fake_pass}")
        time.sleep(0.02)
        crack_bar.progress(i + 1)
        
    placeholder.success(f"🔓 破譯成功！密碼為: LaiHang{random.randint(1000,9999)}Pro")

# 3. 駭客控制命令台介面
st.markdown("### 🎯 遠端滲透作戰指令")
target_ip = st.text_input("📡 請輸入鎖定目標網址或 IP 地址：", "nasa.gov.secure")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔥 執行 DDoS 癱瘓", use_container_width=True):
        st.write(f"⚙️ 正在向 `{target_ip}` 部署 20,000 個殭屍網路電腦...")
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        st.success(f"💥 攻擊成功！`{target_ip}` 伺服器流量已全面癱瘓！")

with col2:
    if st.button("💰 侵入虛擬金庫", use_container_width=True):
        st.write("⚙️ 正在嘗試解密區塊鏈私鑰結算節點...")
        with st.spinner("量子演算法密碼破解中..."):
            time.sleep(1.5)
        st.warning("⚠️ 密碼防盜機制觸發！已成功自動切換虛擬本地 IP，安全撤離！")

with col3:
    if st.button("🚀 解鎖核彈發射井", use_container_width=True):
        st.error("❌ 系統警告：拒絕訪問！需要最高指揮官密碼驗證。")
        auth_check = st.checkbox("🧬 啟動指揮官『賴以航』生物特徵掃描")
        if auth_check:
            with st.spinner("正在辨識指紋與虹膜..."):
                time.sleep(1.2)
            st.success("🔓 驗證通過！最高指揮官 賴以航 歡迎回來。核彈發射井已解鎖！")
            st.balloons()

st.write("---")

# 4. 終端機自訂指令輸入框
st.markdown("### ⌨️ 控制台手動輸入指令")
cmd_input = st.text_input("請輸入 Linux 終端指令 (例如: `help`, `scan`, `bypass`):", "")

if cmd_input:
    st.write(f"`lai-hang@hacker-terminal:~# {cmd_input}`")
    with st.spinner("執行指令中..."):
        time.sleep(0.8)
    
    if cmd_input.lower() == "help":
        st.code("可用指令清單:\n- scan : 掃描目標主機通訊埠\n- bypass : 跳過防火牆\n- clear : 清除系統日誌", language="bash")
    elif cmd_input.lower() == "scan":
        st.code("🔑 正在掃描 Port 80... OPEN\n🔑 正在掃描 Port 443... OPEN\n🔑 正在掃描 Port 22... VULNERABLE!", language="bash")
    elif cmd_input.lower() == "bypass":
        st.success("🛡️ 防火牆安全防禦層已成功繞過！")
    else:
        st.error(f"❌ 找不到指令 '{cmd_input}'。請輸入 'help' 查看完整清單。")

st.write("---")

# 5. 終端機動態串流
st.markdown("### 📟 即時網路數據串流緩衝區 (Live Console)")

hacker_logs = [
    "⚡ [INFO] 正在初始化網路監聽通訊埠 (Port Sockets)...",
    "📡 [CONNECT] 成功連接至多重代理伺服器 (Proxy Node: SOCKS5://103.24.51.9)",
    "🔓 [BYPASS] 正在繞過 Cloudflare 進階防火牆 (WAF)... 成功過濾！",
    "🔑 [DECRYPT] 啟動 AES-256 密鑰暴力破解中...",
    "💾 [DATABASE] 攔截核心資料庫封包 >> 成功下載 encrypted_ledger.db (100%)",
    "🚨 [WARNING] 偵測到反向追蹤防禦！正在緊急重導向至虛擬網段...",
    "💻 [ROOT] 成功獲取目標主機系統最高管理員權限 (Root Access Granted)！",
    "🛠️ [INJECT] 隱形後門程式 (Backdoor.Trojan.Lai.v6) 植入完畢。"
]

if st.button("🖥️ 啟動代碼滲透串流 (Live Stream)", use_container_width=True):
    st.write(">> 正在與遠端伺服器同步日誌：")
    for _ in range(10):
        random_log = random.choice(h
