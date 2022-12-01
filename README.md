# Note_OpenCV
A collection of sample code of OpenCV


## Text

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


## BGR2RGB
- BGR是OpenCV惱人的預設色彩讀取順序，原因是發展OpenCV當下時代盛行的色彩是BGR格式[1]，只是現在主流是RGB了。
- cv2讀取時預設為BGR，如果處理過程跟色彩有關會需要先轉回RGB(或是把你的處理過程用BGR格式)。
- cv2儲存時預設為RGB，即如果沒有做任何色彩處理的話，可直接存檔不需再轉換。

Example:

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

[1] 來源請求



## NOTE Markdowm
![file info](/temp_imgs/2.png)
![file info](flow_sample_001.jpg)



## 依機率選擇使用某個函數
* 這在深度學習的數據集增強中常會用到，增強套件裡一定有幫你寫好這個功能，但總有例外不能直上的時候。
之前有寫過，但懶得找了。因此重新寫在這裡...

* oneof

多個函數中選擇一個，有時候也會配上p。

* p

執行該函數的機率
