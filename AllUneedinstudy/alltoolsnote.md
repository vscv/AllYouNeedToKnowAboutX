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

#### Ubuntu [Ctrl] + [Alt] + [Shift] + [R]
Ubuntu內建的螢幕錄影ctrl+alt+shift+r預設只錄三十秒

修改錄影時間限制
gsettings set org.gnome.settings-daemon.plugins.media-keys max- screencast-length 60  #僅能錄60秒
gsettings set org.gnome.settings-daemon.plugins.media-keys max- screencast-length 0   #不限制時間


#### MacOS
內建QuickTime

# Text editor
直接開XCODE or VSCODE打字

Linux下請用vim或內建文字編輯器


# Code editor
XCODE or VSCODE
