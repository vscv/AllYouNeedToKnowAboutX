### 使用OpenVINO
`OpenVINO工具包是一個免費的工具包，可通過使用推理引擎將深度學習模型從框架和部署優化到英特爾硬件。(wiki)`

#### 支援的框架
ONNX、PaddlePaddle - 直接支持的格式，這意味著它們無需任何事先轉換即可與 OpenVINO Runtime 一起使用。

TensorFlow、PyTorch、MXNet、Caffe、Kaldi - 間接支持的格式，這意味著它們需要在運行推理之前以mo轉換為 OpenVINO IR。


 * * * 

##### 安裝環境

sudo apt update
sudo apt install python3-dev python3-pip python3-venv

###### Create a venv

 python3 -m venv --system-site-packages ./vvino

###### into the venv
 source ./vvino/bin/activate

###### leave from venv
 deactive
 
###### upgrade pip 
python -m pip install --upgrade pip
 
 
###### 安裝OpenVINO最新版
 pip install 'openvino-dev[onnx,tensorflow2]==2022.3.0'   "注意⚠️ OpenVINO改成新版了2022.3.0"


###### test vino
mo -h
`正常印出help說明`


 * * * 

## 檢查VINO與EdgeAI硬體資訊
    #!/bin/bash

    # Check device
    echo ''
    echo '*****************************   [1] Check device   ***************************'
    echo ''
    python /opt/intel/openvino_2022/samples/python/hello_query_device/hello_query_device.py

    # Check xml model
    echo ''
    echo '*****************************   [2] Check XML   ******************************'
    echo ''
    benchmark_app -m ./model/saved_model.xml  -data_shape "[1,640,640,1]" -niter 1 -d CPU

 * * * 
#### 轉換Tensorflow SavedModel為vino可使用之IR格式
 `$ mo --saved_model_dir tf-savedmodel-dir/ --output_dir "./model_v1"`
 ``` 給予資料夾即可  ```
 * * * 
 
#### 使用IR範例
    from openvino.runtime import Core
    from pathlib import Path

    img_size=640
    model_path_v1 = Path("model_v1/saved_model.xml")
    ir_path_v1 = Path(model_path_v1).with_suffix(".xml")

    ie_v1 = Core()
    model_v1 = ie_v1.read_model(model=ir_path_v1, weights=ir_path_v1.with_suffix(".bin"))
    compiled_model_v1 = ie_v1.compile_model(model=model_v1, device_name="CPU")

    input_key_v1 = compiled_model_v1.input(0)
    output_key_v1 = compiled_model_v1.output(0)

    img = get_bHWC_image_from_gardio_gray(img)
    out = compiled_model_v1([img])[output_key_v1]
    out = tf.squeeze(out, axis=0, name=None)
    out = out.numpy()
    out = out.reshape(img_size, img_size)






 * * * 
 * * * 
 * * * 
 