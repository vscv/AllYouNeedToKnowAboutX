

* * *
# Note_OpenCV
A collection of sample code of OpenCV


## Text

```Python
#cv2.putText
font = cv2.FONT_HERSHEY_SIMPLEX
#org
org = (50, 50)
#fontScale
fontScale = 3
#Blue color in BGR
color = (255, 0, 0)
#Blue color in BGR
color_blue = (255, 0, 0)
# Line thickness of 2 px
thickness = 2

cv2.putText(img=img, text=txt, org=(int(x)+20, int(y)-20), fontFace=font, fontScale=2.0, color=color, thickness=thickness, lineType=cv2.LINE_AA)
```
* * *
## BGR2RGB
- BGR是OpenCV惱人的預設色彩讀取順序，原因是發展OpenCV當下時代盛行的色彩是BGR格式[1]，只是現在主流是RGB了。
- cv2讀取時預設為BGR，如果處理過程跟色彩有關會需要先轉回RGB(或是把你的處理過程用BGR格式)。
- cv2儲存時預設為RGB，即如果沒有做任何色彩處理的話，可直接存檔不需再轉換。

Example:

```Python
#Util function
def get_date():
    date= datetime.datetime.today()
    return date.strftime("%Y_%m_%d_%H%M")

#Show anns on the sample image
path="/PATH_TO/train/"
img =  cv2.imread(path + img_name) # If only for showing, BGR -> RGB , cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Check ann by cv2, comment if use cocoapi
for a in ann:
    #print(f'[A box]: {a}')
    category_id = a['category_id']
    txt = 'id:' + str(category_id)
    x,y,w,h = a['bbox']
    cv2.rectangle(img, (int(x), int(y)), (int(x+w), int(y+h)), (255, 255, 0), 5)
    cv2.putText(img=img, text=txt, org=(int(x)+20, int(y)-20), fontFace=font, fontScale=2.0, color=color, thickness=thickness, lineType=cv2.LINE_AA)

fig = plt.figure()
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)); plt.axis('off') #must after the every cv2 task

#Show ann by cocoapi, comment if use cv2
coco.showAnns(ann, draw_bbox=True)


#cannot save the ann on top of image, only save the original img
cv2.imwrite(f'test_patchs/show_ann_{img_name}_cv2_{timestamp}.jpg', img) #imwrite do BGR2RGB for you
#bcs it plot object, we should apply plt.save instead
timestamp = get_date()
# plt.savefig(f'test_patchs/show_ann_with_image_{img_name}_{timestamp}.jpg', bbox_inches='tight', pad_inches=0)
plt.savefig(f'test_patchs/show_ann_{img_name}_plt_{timestamp}.jpg', bbox_inches='tight', pad_inches=0)
```

[1] 來源請求

* * *
## 依機率選擇使用某個函數
* 這在深度學習的數據集增強中常會用到，增強套件裡一定有幫你寫好這個功能，但總有例外不能直上的時候。
之前有寫過，但懶得找了。因此重新寫在這裡...

* oneof

多個函數中選擇一個，有時候也會配上p。如果需求是每次必選一個則p=1，最簡單就是用random.choices(list)來選

```Python
def oneof():
    list = [f1, f2, f3, f4, ]
    return random.choices(list)

aug_f = oneof()
output = aug_f(image) 
```
    
TypeError: 'list' object is not callable： 如果list裡是一堆函數f1() f2()，返回使用時記得加上[0]。

```Python
def oneof():
    list = [f1, f2, f3, f4, ]
    return random.choices(list)[0]

aug_f = oneof()
output = aug_f(image) 
```
    或是

```Python
def oneof():
    list = [f1, f2, f3, f4, ]
    return random.choices(list)

aug_f = oneof()
output = aug_f[0](image) 
```    
    
ps.random.choices的weights參數是可以設定個別元素被選到的機率，但總和為100%。若要給一個是否會執行oneof的機率，就在預先產生一個p值在判斷要不要執行。

##### 假設80%機率才執行oneof時
```Python
p = random.uniform(0, 1)
if p >= 0.8:
    do oneof()
```

* p `執行該函數的機率`

* * * 
### 舊版Tensorflow範例 讀取影像耗時問題
`當初沒考量reshape對於大圖會非常耗時，改用numpy處理即可解決。`

```Python
def load_image_into_numpy_array(pil_image):
    (im_width, im_height) = pil_image.size
    data = pil_image.getdata()

    data_array = np.array(data)

    return data_array.reshape((im_height, im_width, 3)).astype(np.uint8)
```
`改成不要reshape了`
```Python
def load_image_into_numpy_array(path):
    """Load an image from file into a numpy array.

    Puts image into numpy array to feed into tensorflow graph.
    Note that by convention we put it into a numpy array with shape
    (height, width, channels), where channels=3 for RGB.

    Args:
    path: a file path (this can be local or on colossus)

    Returns:
    uint8 numpy array with shape (img_height, img_width, 3)
    """
    img_data = tf.io.gfile.GFile(path, 'rb').read()
    image = Image.open(BytesIO(img_data))

    return np.array(image)
```

`改成不要reshape了2`
```Python
def pil_image_to_numpy_array(pil_image):
    return np.asarray(pil_image)  
```



* * *
## OpenCV 舊版範例問題

`舊版cv2.findContours例如cv2 2.x回傳順序為hierarchy,contours，但4.x 5.x已經改成contours, hierarchy！`

```Python
def find_biggest_contour(image):

# Copy to prevent modification
image = image.copy()

_,contours  = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#get contour sizes and return the biggest contour
max_area = -1
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    if area>max_area:
        biggest_contour = contours[i]
        max_area = area

#create an empty mask
mask = np.zeros(image.shape, np.uint8)

#draw the biggest contour on it
cv2.drawContours(mask, [biggest_contour], -1, 255, -1)

return mask
```
for cv2 4.x 5.x

`contours, hierarchy = cv2.findContours()`

* * *
## Cat-Dog 貓狗資料集EXIF錯誤
首先trace錯誤訊息 找到可能的原因 大部分應該找最源頭而不是最後的Error!例如看到這個會以為TF又出包了
        
        UnknownError: Graph execution error:

其實再往回看源頭，這才是原因。因為其EXIF損壞(可交換圖檔格式Exchangeable image file format是專門為數位相機的相片設定的檔案格式，可以記錄數位相片的屬性資訊和拍攝資料。)

        UserWarning: Possibly corrupt EXIF data.


三種方法：

1. PIL : 請先去除訓練集中損壞的圖片，例如PetImages/Cat/666.jpg, PetImages/Dog/11702.jpg。另請參閱     https://www.kaggle.com/code/sushovansaha9/cat-dog-classification-transferlearning-ipynb。

2. PIL ：刪除 EXIF 數據但保留圖像。

```Python
import piexif  
piexif.remove(filename)
```

3. tf.io：僅讀取圖像數據，因此不用刪除任何圖像或EXIF：
```Python
file = tf.io.read_file(filename)
image = tf.image.decode_jpeg(file)
```
* * *

* * *

* * *
## 繪出標註框修改字型與支援繁體中文
#### deploy/python/infer_LSW.py ---> visualize -> visualize_box_mask -> draw_box
* edukai-4.0.ttf 教育部標準楷書字形檔(Version 4.00)  https://language.moe.gov.tw/001/Upload/Files/site_content/M0001/edukai-4.0.zip
* 然後拷貝到系統預設字型路徑下
sudo cp -rf deploy/python/font_local /usr/share/fonts/truetype/


### 在visualize.py中，增加字體並控制大小
* 中文標籤
```Python
#JCK 中文標籤顯示
labels_cht = [
                "寶特瓶",
                "塑膠瓶蓋",
                "其他飲料瓶與食物容器",
                "非食物的瓶罐與容器",
                "塑膠提袋",
                "食品包裝袋",
                "吸管",
                "外帶飲料杯",
                "免洗餐具",
                "鐵鋁罐",
                "鋁箔包或利樂包",
                "玻璃瓶",
                "釣魚用具",
                "漁業浮球/浮筒/漁船防碰墊",
                "漁網與繩子",
                "菸蒂",
                "牙刷",
                "針筒/針頭",
                "打火機",
                "其他",
            ]
```

* 設定楷體字型與大小
```Python
from PIL import ImageFont
font = ImageFont.turepytpe("edukai-4.0.ttf", 36, encoding="utf-8")
```



* * *

* * *
