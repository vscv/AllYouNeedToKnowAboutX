
src:https://juejin.cn/post/7120506737685168158
.icns檔案是什麼？又是如何在Mac系統中建立的？

1.了解什麼是.icns
.icns 是Apple 的macOS 作業系統的App 圖示檔案的副檔名，你在macOS 的「 Desktop 桌面」、「Finder 訪達」、「Dock 程式塢」等看到應用程式的外觀就是由一個內建在此App內部的副檔名為.icns的檔案實現的。
你可以透過滑鼠「右鍵」點擊App - “顯示包內容” - 進入「Contents」 目錄- 進入「Resources」目錄，然後在目錄下可以找到名為Appicon.icns或其他後綴為.icns的一個圖示檔。
2. 如何建立.icns副檔名的圖示文件
首先要了解下Apple 介面設計規範：
要建立一個.icns圖示文件，需要準備以下10 種不同大小的.png圖片文件


a. 準備最大尺寸1024x1024 圖片一張，重新命名為icon.png，其他大小尺寸可透過終端命令產生；資料夾名稱不能改要同範例一致！
mkdir icons.iconset

b. 開啟終端機指令： ▶ sips -h
sips - scriptable image processing system.
This tool is used to query or modify raster image files and ColorSync ICC profiles.
Its functionality can also be used through the "Image Events" AppleScript suite.

Sips -z 16 16 icon.png -o icons.iconset/icon_16x16.png
Sips -z 32 32 icon.png -o icons.iconset/icon_16x16@2x.png
Sips -z 32 32 icon.png -o icons.iconset/icon_32x32.png
Sips -z 64 64 icon.png -o icons.iconset/icon_32x32@2x.png
Sips -z 128 128 icon.png -o icons.iconseticon_128x128.png
Sips -z 256 256 icon.png -o icons.iconset/icon_128x128@2x.png
Sips -z 256 256 icon.png -o icons.iconset/icon_256x256.png
Sips -z 512 512 icon.png -o icons.iconset/icon_256x256@2x.png
Sips -z 512 512 icon.png -o icons.iconset/icon_512x512.png
Sips -z 1024 1024 icon.png -o icons.iconseticon_512x512@2x.png

b. 轉成icns格式：
iconutil -c icns icons.iconset -o icon.icns


作者：Windows阿咪
链接：https://juejin.cn/post/7120506737685168158
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
