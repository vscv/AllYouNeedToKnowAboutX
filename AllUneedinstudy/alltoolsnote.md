收集一些輔助工具的筆記

# Chrome remotedesttop 遠端桌面

* host/client 僅需要安裝chrome瀏覽器以及google帳號。

`host` 進入remotedesktop 直接輸入https://remotedesktop.google.com/

登入host google帳號

遠端存取-> 設定遠端存取功能 -> （下載plugin）-> 設定好名稱pin碼 -> OK


`client` 使用host google帳號登入 chrome

進入remotedesktop

遠端存取-> 遠端裝置 （此帳號分享的裝置）-> 第一次連線要輸入pin碼

操作設定：進入遠端桌面畫面後，右側有個箭頭，點開可以設定解析度等等，也可以中斷連線。直接關閉分頁也可以中斷連線。



* * *


# Youtube 下載工具

`youtube-dl https://www.youtube.com/watch?v=rkAfWfZkfyo`

`-F` 查詢有什麼格式可以下載

`-f` 下載指定的格式

`-a` 由檔案中的列表下載

`--extract-audio --audio-format mp3` youtube沒有mp3格式，會自動轉檔一次(mac/linux預設用ffmpeg)


例如：僅下載mp3音訊

彩虹小馬列表_url_only.txt  

```Python
https://www.youtube.com/watch?v=mrjXQp3f4Uo
https://www.youtube.com/watch?v=n8miGs6-zKo
https://www.youtube.com/watch?v=wjsv-6wfqyg
https://www.youtube.com/watch?v=wb-6vKk3MJg
```

下載

`youtube-dl --extract-audio --audio-format mp3  -a 彩虹小馬列表_url_only.txt`

* * *

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

* * *
# 在Mac上將文章轉成語音檔
其實基本轉換只要用Mac上內建的功能就可以做了。
轉語音檔的方法有兩種，先講麻煩一點、但可以做細部設定的。
1.
首先要做點準備動作。打開「系統偏好設定」，找到「輔助使用」。
<!-- ![Pasted Graphic 1](https://user-images.githubusercontent.com/18000764/225552403-795080c5-d56c-4e0e-ad44-f9eb9cba8194.jpg) -->
<img src="https://user-images.githubusercontent.com/18000764/225552403-795080c5-d56c-4e0e-ad44-f9eb9cba8194.jpg" width="600" class="center">
然後在「輔助使用」中找到「語音內容」：

如果是要轉換中文文章，「系統聲音」選單中只有三種語音可以選：「Mei-Jia」（台灣）、「Ting-Ting」（中國）、「Sin-ji」（香港，廣東話）。
其他語文就依此類推，自己選擇；但如果選到不懂中文的語音，就只會聽到它胡言亂語了。
在「朗讀速度」選項中，可以調整自己習慣的閱讀速度。
最下面的「按下按鍵時朗讀所選的文字」如果打勾，就可以在閱讀文章時選取段落、再按下指定的按鍵組合（預設是Option+Esc，可以改），即時收聽閱讀語音。

2. 開啟Safari 這邊用google翻譯當作文字介面。
<!-- ![Pasted Graphic 2](https://user-images.githubusercontent.com/18000764/225552442-8124a0bd-55fa-4af6-ab34-4690c22a7064.jpg) -->
<img src="https://user-images.githubusercontent.com/18000764/225552442-8124a0bd-55fa-4af6-ab34-4690c22a7064.jpg" width="600" class="center">
設定好之後，如果想將文字段落存成聲音檔，則可以在選取文字段落之後，在應用軟體的「服務」選單中，選「加入iTunes做為語音軌」。
<!-- ![Pasted Graphic 3](https://user-images.githubusercontent.com/18000764/225552472-facabe06-f68a-4e04-997b-1f67198eaa32.jpg) -->
<img src="https://user-images.githubusercontent.com/18000764/225552472-facabe06-f68a-4e04-997b-1f67198eaa32.jpg" width="600" class="center">
在出現的對話框中，先確認系統聲音是講中文的（如果是中文文章），然後指定存檔位置；按「繼續」，就會自動轉檔了。
Mac系統轉存出來的是「m4a」（MP4聲音檔）的格式，大多數平台和播放器應該都收。至於細部的停頓、語調等部分就別太要求了；如果想要剪接的話，可以用Mac上內建的QuickTime或其他工具。

剛轉出的語音
<!-- ![Pasted Graphic](https://user-images.githubusercontent.com/18000764/225552492-8334678f-f7e2-4e9e-9a78-cbb08f671374.jpg) -->
<img src="https://user-images.githubusercontent.com/18000764/225552492-8334678f-f7e2-4e9e-9a78-cbb08f671374.jpg" width="600" class="center">
把講稿打在PPT下面的筆記中，在用語音轉換每頁的講稿。
製作視訊簡報時 再把語音檔案放上去即可！





* * *


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

`xcode
開啟專案
File-New-Project-Command Line Tool
`
    
    /** Making a Beep with "\a" in C++ not working in xcode on mac ??
 
     Please go to Terminal to run you Beep code!


     cout << "alarm sound.... '\a' \n" << endl;
     cout << "alarm sound.... " << '\a' << endl;

     g++ main.cpp -o beep.exe
     ./beep.exe
     **/

# 簡易的網頁版UI工具
Gradio, Streamlit, Dash(Plotly), Flask, Visdom
  
  當深度學習模型完成開發時，或是預先發布MVP服務時，如何將機器學習應用轉換成APP模式，提供使用者、開發者進行體驗、回饋等功能。相比於前端的核心模型開發主要仰賴AI工程師進行，在APP應用端通常會需要考量到UI/UX設計領域，需要引入專業的前端開發工程師來接手後續APP架構。但通常由於團隊規模或是資源較少，又或是POC/MVP階段無法投注較多資源等因素，使得APP開發工作只能回頭由AI工程師自行完成。雖然，業界熱門強調全棧式工程師/開發者的專業素養，然不全然有益於對個別專業領域的發揮。因此，核心開發人員是否有選項可以最少的成本完成終端APP可視化部署的任務。

* Visdom 方便展示多圖、圖照片、影片、繪圖 
* Plotly是Dash的企業版，Dash僅用過車輛偵測的範例，介面尚可。
* 最近用過Gradio，簡單好用，尤其今年加入Blocks功能使得佈局彈性以及input/oupt多層次串接都比較好寫了。缺點是預設的外觀很普通，如要漂亮的外觀似乎可以經過theme/CSS方式修改，但未曾嘗試。(ps. theme在目前版本v3.12.0的Blocks與的Interface都不能改了！！)
* Flask 用來直接寫API endpoint，反而沒試web介面，因為像Flask/django介面要漂亮都是要套CSS或板模，非專業的人不可能自己寫出漂亮的介面。
* Streamlit跟Gradio相同，主打AI模型的展示與線上互動demo，因此介面都幫你寫好了但就是不太美觀。

* * * * * * 

* Visdom 方便展示多圖、圖照片、影片、繪圖。
* Plotly是Dash的企業版，例如以Dash實現車輛偵測的線上服務，強項在儀表介面數據分析的呈現。
* Flask 用來直接寫API endpoint，因Flask/django介面要美觀均要套CSS或板模，非專業的人較難短時間內寫出漂亮的介面。
* Streamlit跟Gradio相同，主打AI模型的展示與線上互動demo，因此高階介面都能夠直接呼叫，但同樣自由度與美觀度就有限制。
* Gradio，與Streamlit都簡單好用但更高階，尤其今年加入Blocks功能使得佈局彈性以及input/oupt多層次串接都比較好寫了。缺點是預設的外觀很普通，如要漂亮的外觀似乎可以經過theme/CSS方式修改。

***

## Gradio example
<!-- ![image](https://user-images.githubusercontent.com/18000764/227428694-dfb910fe-46f3-4a0b-8430-25b6dd9515eb.png) -->
`範例`

<img src="https://user-images.githubusercontent.com/18000764/227428694-dfb910fe-46f3-4a0b-8430-25b6dd9515eb.png" width="600" class="center">

***
## Streamlit example
`範例` ppocr+gTTS
<!-- ![image](https://user-images.githubusercontent.com/18000764/227437874-409098b3-9f60-444f-87db-5365c4991187.png) -->
<img src="https://user-images.githubusercontent.com/18000764/227437874-409098b3-9f60-444f-87db-5365c4991187.png" width="600" class="center">


### 自動播放gTTS合成語音
若自動播放沒有作用，請打開網頁瀏覽器的允許播放音效設定。把該APP網址加入允許列表。
<!-- ![image](https://user-images.githubusercontent.com/18000764/227427014-c3775e0a-fc5f-46da-a02a-04d153baf8b8.png) -->
<img src="https://user-images.githubusercontent.com/18000764/227427014-c3775e0a-fc5f-46da-a02a-04d153baf8b8.png" width="600" class="center">
<!--  
```Python3
import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
         <audio controls autoplay="true">
         <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
         </audio>
         """
        st.markdown(
         md,
         unsafe_allow_html=True,
     )
     
# # gTTS ##
from gtts import gTTS
sound_file = BytesIO()
tts = gTTS('森山小姐，我相信你。Add text-to-speech to your app', lang='zh-TW')
tts.write_to_fp(sound_file)
tts.save("speech.mp3")
# # gTTS ##

# # Stresmlit web app ##
st.set_page_config(layout="wide", page_title="gTTs")
st.write("## gTTs from your image")
st.sidebar.write("## Upload and download :gear:")

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")
    
col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# # gTTS ##
# tell someingin here #
st.write("# Auto-playing Audio!")
autoplay_audio("speech.mp3")
#st.audio(sound_file)

if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("./40469519171_fa183b8d38_z.jpg")
```
-->

```Bash
$streamlit run bg_remove_tell-gTTS.py --server.address 0.0.0.0 --server.port 5000
```

For client users, public IP:Port.  And we need to set host IP to any.
http://203.145.211.221:55416/

<!-- ![image](https://user-images.githubusercontent.com/18000764/227427917-4f4e8673-c6ee-4d64-8d9c-b1dc56271a61.png) -->
<img src="https://user-images.githubusercontent.com/18000764/227427917-4f4e8673-c6ee-4d64-8d9c-b1dc56271a61.png" width="200" class="center">


***

# 中文語音生成
有個專案需要做TTS把辨識出的文字轉成中文語音並朗讀出來，測了幾種的感想：

*  gTTS : 谷歌本家翻譯裡的發音工具，安裝最方便，支援多國語音包含中文。
*  pyttsx3 ： 發音工具來自各平台內建的語音系統，Windows上使用的是sapi5語音合成引擎，Mac OS X上是nsspeech合成器，eSpeak其他Linux平台上使用。但espeak中文發音其糟無比。
*  PPTTS：槳槳出的語音合成工具，套件安裝法目前有衝突，建議先用docker安裝。語音品質大約與gTTS相等或略好，但有多種男女人聲可選用，也能夠自製訓練。
*  雅婷語音：台灣AI實驗室出品的商用產品，是目前聽到中文語音品質最優的，可申請會員有1000元免費試用額度。

|TTS |安裝難度|中文發音品質|
|-----|--------|--------|
|gTTS|3       |--------|
|pyttsx3  |12      |--------|
|PPTTS  |12      |--------|
|PPTTS  |12      |--------|

***


# 自動滑鼠、鍵盤與視窗、螢幕控制

  AHK: autohotkey 用於微軟視窗作業系統中的腳本控制自動化滑鼠、鍵盤操作。跨平台上有AutoHotkey.py包了DLL來使用，最新在2021年。
  
    GT7 with AHK : 利用AHK來控制在Windows中的PS remote視窗，以達成自動跑圈、刷卷功能。
  * https://github.com/ByPrinciple/GT7-Scripts  
  
  PyAutoGUI: Python的腳本控制滑鼠、鍵盤與其他應用程序的自動化操作。PyAutoGUI 只能在 Windows、macOS 和 Linux 上運行，現在 PyAutoGUI 只處理主監視器。
  pynput:自製熱鍵(停更)。 
    
    自動網頁點按與隨機換頁導航

* [python]依靠pynput和pyautogui替换ahk https://zhuanlan.zhihu.com/p/133096887



# `pandoc` 各種文件檔案格式轉換工具

Pandoc is the swiss-army knife of converting documents between various formats. While being able to deal with heavy-weight formats like docx and epub, we will need it for the more lightweight markdown. To be able to generate PDF files, we need LaTeX. On OSX, the solution of choice is usually MacTeX.

### 把markdown (md)轉成pdf
`注意 若有中文字、符、空格 報錯 ex: ! LaTeX Error: Unicode character 關 (U+95DC) not set up for use with LaTeX.` 請去研究latex中文支援問題。不然轉兩次，先轉成docx再用word輸出pdf。

    $ brew update
    $ brew install pandoc
    $ pandoc -o out.pdf inputgithub.md
    
### 把文件轉成EPUB(電子書)
除了pandoc，max內建工具可以轉。
<!-- ![image](https://user-images.githubusercontent.com/18000764/225554176-80750d62-2bb6-4d56-875f-c6347999b1df.png) -->
<img src="https://user-images.githubusercontent.com/18000764/225554176-80750d62-2bb6-4d56-875f-c6347999b1df.png" width="200" class="center">


### pdf2docx
pdf是一種layout描述不是格式，需要解析後轉換，例如轉成html txt等，再用`pandoc`轉成docx。
`pdf2docx`就是利用解析pdf內的文字、圖片（by PyMuPDF），也可以當作內容的擷取工具，讀取出內容物後再幫你轉成docx格式（by python-docx）。
https://github.com/dothinking/pdf2docx


```Python
from pdf2docx import Converter

pdf_file = '/path/to/sample.pdf'
docx_file = 'path/to/sample.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()
```
* 若是AttributeError: partially initialized module 'cv2' has no attribute '_registerMatType' (most likely due to a circular import) 是因為cv2版本過舊，請更新opencv-contrib-python，並把opencv-python移除，或保留其中一個即可。
***
### 實驗影像轉成動畫
Use `Imagemagick convert` to convert the still images to GIF is the best choice!

```Shell
convert -resize 65% -delay 30 -loop 3 `ls -v ./zhuyin_encoder_48-128_ckpt_cleanGT/*.jpg` ZhuYin_64-128_ckpt_cleanGT_evl_results_convert_2k_0.65_epoch.gif 

convert -resize 100% -delay 30 -loop 3 `ls -v ./zhuyin_encoder_48-128_ckpt_cleanGT/*.jpg` ZhuYin_64-128_ckpt_cleanGT_evl_results_convert_2k_1.00_epoch_22.gif 

```

***
# `Overleaf` 寫paper的好幫手，研究生必備！
TLDR:Overleaf支援各大期刊、研討會範本，可直接使用，唯一缺點是必須聯網使用。一開始也是為了在mac裝LaTex、中文支援、Bibtex等花了很多時間，編譯次數太頻繁對筆電來說太耗電。而且MacTeX檔案之大加上其他套件都會狠狠吃掉你珍貴的SSD，好處是可以獨立運行，也可以稍微保密的你研究工作。
