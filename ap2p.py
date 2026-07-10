import streamlit as st
import time
import random

# 1. 網頁頁面初始化設定
st.set_page_config(page_title="賴以航 終極黑客控制台", page_icon="💀", layout="centered")

# 核心開發者資訊區塊
with st.container(border=True):
    st.subheader("💀 首席網路安全專家：賴以航 (Yi-Hang Lai)")
    st.caption("⚡ SYSTEM STATUS: INFILTRATING... | 核心技術：動態流式代碼偽裝與防禦重導向")

st.title("💻 黑客帝國控制終端 v4.0")
st.write("本終端已安全連線至雲端防禦中心，請鎖定目標並執行滲透指令。")
st.write("---")

# 2. 準備超逼真的黑客日誌代碼庫
hacker_logs = [
    "⚡ [INFO] 正在初始化網路監聽通訊埠 (Port Sockets)...",
    "📡 [CONNECT] 成功連接至多重代理伺服器 (Proxy Node: SOCKS5://103.24.51.9)",
    "🔓 [BYPASS] 正在繞過 Cloudflare 進階防火牆 (WAF)... 成功過濾！",
    "🔑 [DECRYPT] 啟動 AES-256 密鑰暴力破解中...",
    "💾 [DATABASE] 攔截核心資料庫封包 >> 成功下載 encrypted_ledger.db (100%)",
    "🚨 [WARNING] 偵測到反向追蹤防禦！正在緊急重導向至虛擬網段...",
    "💻 [ROOT] 成功獲取目標主機系統最高管理員權限 (Root Access Granted)！",
    "🛠️ [INJECT] 隱形後門程式 (Backdoor.Trojan.Lai.v4) 植入完畢。"
]

# 3. 駭客控制命令台介面
st.markdown("### 🎯 遠端滲透作戰指令")

# 讓使用者輸入想要攻擊的目標
target_ip = st.text_input("📡 請輸入鎖定目標網址或 IP 地址：", "nasa.gov.secure")

# 建立 3 個完全獨立可用的功能按鈕
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔥 執行 DDoS 癱瘓", use_container_width=True):
        st.write(f"⚙️ 正在向 `{target_ip}` 部署 20,000 個殭屍網路電腦...")
        
        # 動態進度條特效
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01) # 讓進度條跑動
            progress_bar.progress(i + 1)
            
        st.success(f"💥 攻擊成功！`{target_ip}` 伺服器流量瞬間衝破 150Gbps，系統已全面癱瘓！")

with col2:
    if st.button("💰 侵入虛擬金庫", use_container_width=True):
        st.write("⚙️ 正在嘗試解密區塊鏈私鑰結算節點...")
        
        with st.spinner("量子演算法密碼破解中..."):
            time.sleep(1.5) # 模擬運算延遲
            
        st.warning("⚠️ 密碼防盜機制觸發！已成功自動切換虛擬本地 IP，安全撤離！")

with col3:
    if st.button("🚀 解鎖核彈發射井", use_container_width=True):
        # 駭客專屬驚喜互動
        st.error("❌ 系統警告：拒絕訪問！需要最高指揮官密碼驗證。")
        
        # 密碼鎖檢查機制
        auth_check = st.checkbox("🧬 啟動指揮官『賴以航』生物特徵掃描")
        if auth_check:
            with st.spinner("正在辨識指紋與虹膜..."):
                time.sleep(1.2)
            st.success("🔓 驗證通過！最高指揮官 賴以航 歡迎回來。核彈發射井已解鎖！")
            st.balloons() # 滿分氣球特效慶祝！

st.write("---")

# 4. 終端機動態串流效果（核心功能）
st.markdown("### 📟 即時網路數據串流緩衝區 (Live Console)")

# 點擊這個按鈕就會像好萊塢電影一樣一行一行吐程式碼！
if st.button("🖥️ 啟動代碼滲透串流 (Live Stream)", use_container_width=True):
    st.write(">> 正在與遠端伺服器同步日誌：")
    
    # 隨機挑選日誌並一行一行印出來，非常有科技感
    for _ in range(12):
        random_log = random.choice(hacker_logs)
        
        # 利用 Streamlit 的 chat_message 來做黑客對話框排版，保證百分之百可用不跑版
        with st.chat_message("assistant", avatar="💀"):
            st.code(random_log, language="bash")
            
        time.sleep(0.2) # 控制每一行代碼掉下來的時間間隔
        
    st.success("🎯 終端任務執行完畢。所有足跡已完全抹除。")

st.write("\n---")
st.caption("⚡ Powered by Streamlit Components & Logic Engine")
st.caption("© 2026 賴以航 (Yi-Hang Lai). Confidential Hack Terminal. All rights reserved.")
