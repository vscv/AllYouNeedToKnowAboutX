# MS coco dataset and API


## download COCO API, Images, Annotations
https://cocodataset.org/#download

  wget http://images.cocodataset.org/zips/val2014.zip
  wget http://images.cocodataset.org/zips/train2014.zip
  
  wget http://images.cocodataset.org/annotations/annotations_trainval2014.zip
  
### COCO API
  
    # 先安裝coco api
    # clone https://github.com/cocodataset/cocoapi
    # -For Python, run "make" under coco/PythonAPI
    cd /coco/PythonAPI
    vim Makerfile
    python ---> python3 現在都改用py3了
    # 編譯
    make -j8 
    
  * 在cocoapi/PythonAPI/下這個腳本把使用方法都展示一遍
  pycocoDemo.ipynb
  
  * 注意 他把trainn/val分開寫，請自行切換
  
  * github md僅能用html設定影像尺寸與對齊位置
  *![img](/temp_imgs/ms-coco-switch-anns.jpg) 不能設定尺寸與對齊
  * 
  
  設定影像大小
  <img src="/temp_imgs/ms-coco-switch-anns.jpg" width="500" height="150" class="center">
   
   設定對齊中央
  <p align="center">
    <img width=40% height=40% src="/temp_imgs/ms-coco-switch-anns.jpg">
  </p>

* 注意 image captioning, instances(mask or segmentation), keypoints的annotations也是分開的
* 但任一個ann都可以讀取image
  <p align="center">
    <img width=40% height=40% src="/temp_imags/ms-coco-all-anns-can-load-same-image.jpg">
  </p>
