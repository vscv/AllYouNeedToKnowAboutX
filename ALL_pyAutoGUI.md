### mouse position 滑鼠座標
    print(pyautogui.position())
    """Point(x=2986, y=1663)"""
    x, y = pyautogui.position()

### 螢幕解析度
    print(pyautogui.size())



### 滑鼠控制 : https://pyautogui.readthedocs.io/en/latest/mouse.html

### 移動 : 設定移動的位置，與移動時間(duration)
    pyautogui.moveTo(100, 100, duration = 1.5) # 用1.5秒移動到x=100，y=100的位置 有慢動作的效果

### 移動 : 滑鼠目前的位置來做相對移動
    pyautogui.moveRel()


### 拖曳 : 除了目標位置以及移動的時間外，可設定button選擇是左(left)、中(middle)、右(right)鍵
    pyautogui.dragTo(100, 100, duration=2, button='right') # 用2秒按住滑鼠右鍵到x=100，y=100的位置


### 點按 ： 參數是clicks(點擊次數)以及interval(點擊中相隔的時間)
    pyautogui.click(clicks=2, interval=0.5, button='right') # 雙擊左鍵並且中途間隔0.5秒

### 獨立點與按 :
    pyautogui.mouseDown(); pyautogui.mouseUp()  # does the same thing as a left-button mouse click
    pyautogui.mouseDown(button='right')  # press the right button down
    pyautogui.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.


### 滾輪 : 在 OS X 和 Linux 平台上，PyAutoGUI 還可以通過調用 hscroll() 函數來執行水平滾動
    pyautogui.scroll(10)   # scroll up 10 "clicks"
    pyautogui.scroll(-10)  # scroll down 10 "clicks"
    pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"


### 補間/緩動函數 Tween / Easing Functions : 花式移動
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
    pyautogui.moveTo(1000, 1000)
    pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
    pyautogui.moveTo(1000, 1000)
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
    pyautogui.moveTo(1000, 1000)
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
    pyautogui.moveTo(1000, 1000)
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end



### 鍵盤控制

### type打字
    pyautogui.write('Hello world!')                 # prints out "Hello world!" instantly
    pyautogui.write('Hello world!', interval=0.25)  # prints out "Hello world!" with a quarter second delay after each character

### 按鍵 : https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys
    pyautogui.keyDown('ctrl')   # down
    pyautogui.keyUp('ctrl')     # up

    pyautogui.press('left')     # press the left arrow key

### 熱鍵 : 依序按下，再依序釋放
    pyautogui.hotkey('ctrl', 'shift', 'esc')
    """ 等同於下：
    >>> pyautogui.keyDown('ctrl')
    >>> pyautogui.keyDown('shift')
    >>> pyautogui.keyDown('esc')
    >>> pyautogui.keyUp('esc')
    >>> pyautogui.keyUp('shift')
    >>> pyautogui.keyUp('ctrl')"""

### The hold() Context Manager 祕技熱鍵
    with pyautogui.hold('shift'):
            pyautogui.press(['left', 'left', 'left'])
    """ 等同於下：
    >>> pyautogui.keyDown('shift')  # hold down the shift key
    >>> pyautogui.press('left')     # press the left arrow key
    >>> pyautogui.press('left')     # press the left arrow key
    >>> pyautogui.press('left')     # press the left arrow key
    >>> pyautogui.keyUp('shift')    # release the shift key

    很微妙的用法，有些遊戲有即時輸入對話或開發指令的功能，如WOT按ENTER後鍵盤進入打字區，IOH按~可以進入開發指令。
    """


### 螢幕快照與螢幕影像比對

### screenshot()
    im1 = pyautogui.screenshot()
    im2 = pyautogui.screenshot('my_screenshot.png')


### 找出範例影像在螢幕的位置 (沒成功)
    """注意：您需要安裝OpenCV才能使confidence關鍵字起作用。"""
    """注意：從 0.9.41 版開始，如果定位函數找不到提供的圖像，它們將引發ImageNotFoundException而不是返回None。"""
    """這些“定位”功能相當昂貴；他們可以花整整一秒鐘的時間來運行。加速它們的最好方法是傳遞一個region參數（一個 4 整數元組（左、上、寬、高））來只搜索屏幕的較小區域而不是整個屏幕：pyautogui.locateOnScreen('someButton.png', region=(0,0, 300, 400))"""
    """(left, top, width, height) or  center() XY"""

    button7location = pyautogui.locateOnScreen('py_logo.jpg', confidence=0.9)
    print("calc 7 key (left, top, width, height) : ", button7location)

    button7center = pyautogui.center(button7location)
    print("calc 7 key (center X,Y) : ", button7center)

### 灰度匹配
    """提供輕微的加速（大約 30% 左右），但可能會導致誤報匹配。"""

### RGB匹配
    """
    >>> im = pyautogui.screenshot()
    >>> im.getpixel((100, 200))"""


 * * *
 
 * * *
 
 ### 一個規律點按範例
 
    import pyautogui
    print(pyautogui.__version__) # 0.9.53
    import time
    import random

    def Scroll_d(n=4):
        i=0
        while i <= n:
            pyautogui.scroll(-100)
            i+=1
        
        # give it more randomly
        time.sleep(random.randint(1,4))


    def one_page_over():
        # Sleep a while y may Ctrl-C this.
        time.sleep(2)

    # TAable select
    pyautogui.moveTo(2540, 25, duration = 1.5)
    pyautogui.moveTo(2000, 1500, 2, pyautogui.easeInElastic)
    pyautogui.moveTo(2540, 25, 2, pyautogui.easeInElastic)
    pyautogui.click(clicks=1, interval=0.5, button='left')


    # Topic select
    pyautogui.moveTo(1840, 315, duration = 1.5)
    pyautogui.click(clicks=1, interval=0.5, button='left')

    # T1 page
    pyautogui.moveTo(2122, 770, duration = 1.5)
    pyautogui.click(clicks=1, interval=0.5, button='left')
    Scroll_d(20)


    # go-back one page
    pyautogui.moveTo(1742, 57, duration = 1.5)
    pyautogui.click(clicks=1, interval=0.5, button='left')


    # T2 page
    pyautogui.moveTo(2110, 890, duration = 1.5)
    pyautogui.click(clicks=1, interval=0.5, button='left')
    Scroll_d(5)

    # go-back one page
    pyautogui.moveTo(1742, 57, duration = 1.5)
    pyautogui.click(clicks=1, interval=0.5, button='left')

    # Sleep a while y may Ctrl-C this.
    time.sleep(10)


    while True:
        # give it more randomly
        time.sleep(random.randint(2,5))
        one_page_over()
 
 
