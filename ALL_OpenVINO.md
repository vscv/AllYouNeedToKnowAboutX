### 使用OpenVINO
`OpenVINO工具包是一個免費的工具包，可通過使用推理引擎將深度學習模型從框架和部署優化到英特爾硬件。(wiki)`

#### 支援的框架
ONNX、PaddlePaddle - 直接支持的格式，這意味著它們無需任何事先轉換即可與 OpenVINO Runtime 一起使用。

TensorFlow、PyTorch、MXNet、Caffe、Kaldi - 間接支持的格式，這意味著它們需要在運行推理之前以mo轉換為 OpenVINO IR。




##### 安裝環境

sudo apt update
sudo apt install python3-dev python3-pip python3-venv

###### Create a venv

 python3 -m venv --system-site-packages ./vvino

###### into the venv
 source ./vvino/bin/activate

###### leave from venv
 deactive
 
###### pip install --upgrade pip
python -m pip install --upgrade pip
 
 
