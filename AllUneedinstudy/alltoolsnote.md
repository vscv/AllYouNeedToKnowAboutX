收集一些輔助工具的筆記

# Voideo editor
有用過下面幾種，常用OpenShot來做臨時的短片。

後來都用iMove來處理短片，但iMove對4K(>3440x1440以上)無法預覽使得特效、字幕、標註等無法當下確定時間與位置，且最終僅能輸出FHD（1920x1080）。只能裝Shotcut應急。

* Top 3. PiTiVi 視頻編輯器
* Top 4. Shotcut 視頻編輯器 (4k)
* Top 5. Blender 視頻編輯器
* Top 6. OpenShot 視頻編輯器 

https://acemovi.tuneskit.com/review/best-ubuntu-video-editor.html

Shotcut 轉場效果範例 (拖曳影片嵌入另一端內重疊，即可選轉場屬性。) https://forum.gamer.com.tw/C.php?bsn=60030&snA=542068

Shotcut 自訂畫面比例 21:9 (3440x1440) OK

Shotcut 加入線條、箭頭、任何其他圖案，可用去背的PNG圖檔加入另一個視訊軌。


### 照片去除背景(PNG圖片)
* Adobe Express (免費線上使用 自動選取) https://www.adobe.com/tw/express/feature/image/remove-background
* PowerPoint (圖片格式->移除背景 半手動選取)

# Screen recorder
# 螢幕錄製

### Ubuntu [Ctrl] + [Alt] + [Shift] + [R]
Ubuntu內建的螢幕錄影ctrl+alt+shift+r預設只錄三十秒

  修改錄影時間限制
  * gsettings set org.gnome.settings-daemon.plugins.media-keys max- screencast-length 60  #僅能錄60秒
  * gsettings set org.gnome.settings-daemon.plugins.media-keys max- screencast-length 0   #不限制時間
  
  
  
### MacOS
  內建QuickTime

# Text editor
  直接開XCODE or VSCODE打字

  Linux下請用vim或內建文字編輯器


# Code editor
  XCODE or VSCODE

# 簡易的網頁版UI工具
Gradio, Streamlit, Dash(Plotly), Flask, Visdom
  
  當深度學習模型完成開發時，或是預先發布MVP服務時，如何將機器學習應用轉換成APP模式，提供使用者、開發者進行體驗、回饋等功能。相比於前端的核心模型開發主要仰賴AI工程師進行，在APP應用端通常會需要考量到UI/UX設計領域，需要引入專業的前端開發工程師來接手後續APP架構。但通常由於團隊規模或是資源較少，又或是POC/MVP階段無法投注較多資源等因素，使得APP開發工作只能回頭由AI工程師自行完成。雖然，業界熱門強調全棧式工程師/開發者的專業素養，然不全然有益於對個別專業領域的發揮。因此，核心開發人員是否有選項可以最少的成本完成終端APP可視化部署的任務。

* Visdom 方便展示多圖、圖照片、影片、繪圖 
* Plotly是Dash的企業版，Dash僅用過車輛偵測的範例，介面尚可。
* 最近用過Gradio，簡單好用，尤其今年加入Blocks功能使得佈局彈性以及input/oupt多層次串接都比較好寫了。缺點是預設的外觀很普通，如要漂亮的外觀似乎可以經過theme/CSS方式修改，但未曾嘗試。(ps. theme在目前版本v3.12.0的Blocks與的Interface都不能改了！！)
* Flask 用來直接寫API endpoint，反而沒試web介面，因為像Flask/django介面要漂亮都是要套CSS或板模，非專業的人不可能自己寫出漂亮的介面。
* Streamlit跟Gradio相同，主打AI模型的展示與線上互動demo，因此介面都幫你寫好了但就是不太美觀。

  Visdom 方便展示多圖、圖照片、影片、繪圖。
  Plotly是Dash的企業版，例如以Dash實現車輛偵測的線上服務，強項在儀表介面數據分析的呈現。
  Flask 用來直接寫API endpoint，因Flask/django介面要美觀均要套CSS或板模，非專業的人較難短時間內寫出漂亮的介面。
  Streamlit跟Gradio相同，主打AI模型的展示與線上互動demo，因此高階介面都能夠直接呼叫，但同樣自由度與美觀度就有限制。
  Gradio，與Streamlit都簡單好用，尤其今年加入Blocks功能使得佈局彈性以及input/oupt多層次串接都比較好寫了。缺點是預設的外觀很普通，如要漂亮的外觀似乎可以經過theme/CSS方式修改。
