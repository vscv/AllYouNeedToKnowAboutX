## Finder
### Finder 更改顯示字型

`設了半天重開Finder視窗後，為何預設的自型大小就消失了？`

參考：https://support.apple.com/zh-tw/guide/mac-help/mchldaafb302/13.0/mac/13.0

多層資料集設定：

父資料夾：選擇「顯示方式」->『打開顯示方式選項』
<p align="center"> <img width=200 src="https://user-images.githubusercontent.com/18000764/216751152-716752c4-f1ca-4db8-ae5d-3b71852718e9.png"> </p>

注意：只有父資料夾的第二個設定要勾選。

父資料夾：選擇「顯示方式」->『打開顯示方式選項』
<p align="center"> <img width=200 src="https://user-images.githubusercontent.com/18000764/216751174-d0c95fc0-3738-4b94-8c09-36947645dece.png"> </p>

注意：所有子資料集的第二個設定不要勾選。

* * *

## iTune 音樂

拷貝一份放本機中離線播放

MP3位置：/Users/NAME/Music/iTunes/2023_02_02_MP3

若是要整個資料夾MP3加入 播放列表

`直接拖曳 資料夾 到iTune的播放列表下變成列表，然後可以建立列表資料夾，再把多個列表移動到列表資料夾中。`


* * *

## MacOS 郵件預覽/網頁瀏覽器，某些頁面的中文顯示問號框框

* 若是在mail2000郵件，選擇純文字模式，就正常顯示中文。
* 此外，用右鍵選取時prompt可以看到文字，或是右鍵拷貝貼上任何編輯器也可正常顯示中文。

![Pasted Graphic 3](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/673abcc2-8b9f-4165-a05c-c304e5bfa09c)

* 應該是字型問題：開啟『字體簿』查看字型，有一個字體就是問號框框。把他停用之後，郵件、chrome網頁的問號框框就變成文字了。

![Pasted Graphic 1](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/e9a1aff1-7bb7-4fb0-87d2-83cea7237394)

* 移除字體：進入『所有字體』，有移除選項，移除後若還存在，請重開字體簿重整。
* 重置字體：再去設定，進階，『重置字體』。發現.last resort並不是預設字體，所以不會重新下載。
* 
![Pasted Graphic 4](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/cfd7f8de-ba34-4f19-a28c-89cbab2b244d)


* * *

## Finder自製新增檔案工具與icns製作

![image](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/f03f7fc4-e31b-43ea-a5a3-8b162495387b)
### 開啟工序編輯
新增檔案，AppleScript處填入`tell application "Finder" to make new file at (the target of the front window) as alias`
![image](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/bfb0e753-b902-4cf8-a1b3-93929806c1d4)

### 存檔選應用程式
![image](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/e3b87508-fd4d-472b-ab51-d31a63b97729)

### 預設的icon是scirpt圖示
![image](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/67fd1bb5-d3fd-4a75-b32a-64a6f9f1ce6f)
![image](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/98472d37-343d-473c-8ed1-972b9d824507)

### 加入Finder工具列
![image](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/068f53c7-e670-41a5-a4ab-f71d16b742c8)
這時候把`Finder新增檔案.app`拖曳到Finder即可。


### icns製作

用Inkscape製作一個1024x1024的png圖片，或是下載現成的SVG或png來改都可以。這裡是用https://upload.wikimedia.org/wikipedia/commons/3/31/U%2B1F02A_MJbaida.svg來放大。
![image](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/45dae621-50cc-4860-bdfe-d1bf94989e58)

#### 開啟終端機指令： 

```shell
mkdir icons.iconset

sips -z 16 16 icon.png -o icons.iconset/icon_16x16.png
sips -z 32 32 icon.png -o icons.iconset/icon_16x16@2x.png
sips -z 32 32 icon.png -o icons.iconset/icon_32x32.png
sips -z 64 64 icon.png -o icons.iconset/icon_32x32@2x.png
sips -z 128 128 icon.png -o icons.iconseticon_128x128.png
sips -z 256 256 icon.png -o icons.iconset/icon_128x128@2x.png
sips -z 256 256 icon.png -o icons.iconset/icon_256x256.png
sips -z 512 512 icon.png -o icons.iconset/icon_256x256@2x.png
sips -z 512 512 icon.png -o icons.iconset/icon_512x512.png
sips -z 1024 1024 icon.png -o icons.iconseticon_512x512@2x.png

iconutil -c icns icons.iconset -o icon.icns
```

#### 取代原本app/Contents/Resources/applet.icns： 

```shell
▶ cp -rf icon.icns ../Finder新增檔案.app/Contents/Resources/applet.icns 
```
不要急，icns不會馬上更新要等一會。
![image](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/e9ec97bd-9d13-46c0-b205-8f993ef2d636)
![image](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/0b0cb56e-c901-4c32-9a28-1da25e7eca30)


若要換成新icns，一樣自訂工具列，把舊的拉下，新的拖曳上去就好了。
![image](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/073ed15a-32c6-4862-ac70-659375bc3122)

