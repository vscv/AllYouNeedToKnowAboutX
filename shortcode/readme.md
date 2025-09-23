

# 1

## 2

### clock_on_desktop_with_python_tkinter

- windows tkinter

- MacOS tkinter error
  - 
  這個錯誤訊息 _tkinter.TclError: bad attribute "-transparentcolor" 清楚地表明，您在 macOS 上使用的 Tkinter 版本不支援 wm_attributes("-transparentcolor", "white") 這個屬性。
  
  原因分析
  平台差異性：Tkinter 的 wm_attributes 方法是用來控制視窗管理器（window manager）的屬性。其中，-transparentcolor 屬性是專為 Windows 系統設計的，用於將特定顏色（此處為白色）設定為透明。
  
  macOS 的限制：macOS 上的視窗管理器不支援這種透過顏色來定義透明區域的方式。因此，當程式碼在 macOS 上執行時，Tkinter 會報錯，因為它不認識 -transparentcolor 這個指令。
  
  其他透明屬性：macOS 支援的透明屬性是 -transparent 或 -alpha，而不是 -transparentcolor。這就是錯誤訊息中列出的選項。


- PyQT5

<img width="1482" height="1126" alt="image" src="https://github.com/user-attachments/assets/b5358e2d-5527-459b-9ce8-775f54e58c14" />


## exe or app

### Mac
```bash
▶ pip install pyinstaller

pyinstaller  --onefile --noconsole --icon=clock.png clock_pyqt5.py
```
<img width="390" height="140" alt="image" src="https://github.com/user-attachments/assets/150ecf70-40dc-4e85-9984-fecb1eb9ca3a" />
<img width="390" height="246" alt="image" src="https://github.com/user-attachments/assets/cea262db-5e76-47c4-aecf-74710b995e45" />
