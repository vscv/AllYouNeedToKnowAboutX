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
  * 注意 image captioning, instances(mask or segmentation), keypoints的annotations也是分開的
  * 
![image](https://user-images.githubusercontent.com/18000764/210498855-e1a7d184-0bb0-4698-9314-462d8c0fda46.png)
