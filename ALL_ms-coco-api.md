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
