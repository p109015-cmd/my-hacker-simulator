/* 2. 🛰️ 衛星劫持 */
function triggerSatellite() {
    openFxLayer();
    // 使用 NASA 官方或其他允許嵌入的高畫質太空地球視訊
    var videoPool = ["P5_GlAOCHyE", "O6_VbFofA_g"]; 
    var chosenVideoId = videoPool[Math.floor(Math.random() * videoPool.length)];
    
    var pct = 0;
    var container = document.createElement("div");
    container.style.textAlign = "center"; container.style.marginTop = "5vh";
    container.innerHTML = '<h2 style="letter-spacing:3px;">🛰️ [ORBITAL SATELLITE HIJACK PROTOCOL]</h2>' +
                           '<div style="font-size:16px; color:#00aa00; margin-bottom:15px;">正在強制劫持下行微波，同步調取實時光學視訊源...</div>' +
                           '<div class="video-container">' +
                           // 額外加上 playsinline 確保相容性
                           '<iframe width="100%" height="100%" src="https://www.youtube.com/embed/' + chosenVideoId + '?autoplay=1&mute=1&controls=0&loop=1&playlist=' + chosenVideoId + '&playsinline=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>' +
                           '</div>' +
                           '<div id="sat-progress-bar" style="width:60%; margin:0 auto; border:1px solid #00ff00; padding:3px; text-align:left;"><div id="sat-fill" style="width:0%; background:#00ff00; height:20px;"></div></div>' +
                           '<div id="sat-pct" style="margin-top:10px; font-size:24px;">0%</div>' +
                           '<div id="sat-details" style="margin-top:20px; font-size:14px; text-align:left; width:50%; margin-left:auto; margin-right:auto; color:#33ff33; height:120px; overflow-y:auto;"></div>';
    fxLayer.appendChild(container);
    
    var fill = document.getElementById("sat-fill");
    var pctText = document.getElementById("sat-pct");
    var details = document.getElementById("sat-details");
    
    var timer = setInterval(function() {
        pct += 2;
        fill.style.width = pct + "%";
        pctText.textContent = pct + "%";
        if(pct % 10 === 0) {
            details.innerHTML += "&gt;&gt; 量量加密金鑰破譯中... 位元組比對: [OK] | 鎖定軌道經緯度: " + (Math.random()*180).toFixed(4) + "°N, " + (Math.random()*90).toFixed(4) + "°E<br>";
            details.scrollTop = details.scrollHeight;
        }
        if(pct >= 100) {
            clearInterval(timer);
            details.innerHTML += "<br><span style='color:#ffffff; font-size:18px; font-weight:bold;'>🛰️ [HIJACK SUCCESS] 衛星控制鏈已成功切換！即時下行廣播影像接收中。</span><br><button onclick='backToC2()' style='background:#003300; color:#00ff00; border:1px solid #00ff00; padding:10px; margin-top:15px; cursor:pointer;'>返回主控面板</button>";
            details.scrollTop = details.scrollHeight;
        }
    }, 60);
}
