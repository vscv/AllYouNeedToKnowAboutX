* * *
[OOM]

OOM有兩種，host CPU與GPU。

CPU: 

不要直接將dataset載入記憶體中使用，最好用tf.data、tfrecord來處理。

GPU:

減少batch size，減少輸入影像的解析度，使用混合精度。

(transfer learning可以跑，fine tuneing就OOM？ 問題一樣，fine tune會`真的`啟用所有參數因此需要的GPU記憶體會更多！)

近年GPU記憶體規格：

V100 32GB

A100 80GB

H100 80GB

⭕️ 至少V100就跑不了EfficientNet-V2-XL的fine tuning!!!



⭕️ 沒資源的話可以上kaggle註冊，一週有20小時的TPU可以使用。

TPU: 

e.g. "TPU v3-8" 8核心 128GB memory

  EfficientNet-V2-XL: Fine-tune, bs=64 <-- BATCH_SIZE = 8 * strategy.num_replicas_in_sync 

    INFO:tensorflow:Deallocate tpu buffers before initializing tpu system.
    INFO:tensorflow:Initializing the TPU system: local
    INFO:tensorflow:Finished initializing TPU system.
    INFO:tensorflow:Found TPU system:
    INFO:tensorflow:*** Num TPU Cores: 8
    INFO:tensorflow:*** Num TPU Workers: 1
    INFO:tensorflow:*** Num TPU Cores Per Worker: 8
    INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:localhost/replica:0/task:0/device:CPU:0, CPU, 0, 0)
    INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:localhost/replica:0/task:0/device:TPU:0, TPU, 0, 0)
    INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:localhost/replica:0/task:0/device:TPU:1, TPU, 0, 0)
    INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:localhost/replica:0/task:0/device:TPU:2, TPU, 0, 0)
    INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:localhost/replica:0/task:0/device:TPU:3, TPU, 0, 0)
    INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:localhost/replica:0/task:0/device:TPU:4, TPU, 0, 0)
    INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:localhost/replica:0/task:0/device:TPU:5, TPU, 0, 0)
    INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:localhost/replica:0/task:0/device:TPU:6, TPU, 0, 0)
    INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:localhost/replica:0/task:0/device:TPU:7, TPU, 0, 0)
    INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:localhost/replica:0/task:0/device:TPU_SYSTEM:0, TPU_SYSTEM, 0, 0)
    /QK/ TPU!
    Number of accelerators:  8


    model_pruner failed: INVALID_ARGUMENT: Graph does not contain terminal node AssignAddVariableOp. `這個目前無解，僅是警告還是可以訓練的。`


* log

    
      Epoch 1: val_loss improved from inf to 229.27214, saving model to best_my_model_20230904_bs8_reduce_lr_efnv2xl_fine_tune_TPU/saved_weight
      4/4 [==============================] - 714s 101s/step - loss: 449.7910 - mean_squared_error: 449.7810 - mean_absolute_error: 18.9748 - root_mean_squared_error: 21.2080 - val_loss: 229.2721 - val_mean_squared_error: 229.2620 - val_mean_absolute_error: 14.2356 - val_root_mean_squared_error: 15.1414 - lr: 0.0010
      Epoch 2/1000
      4/4 [==============================] - ETA: 0s - loss: 269.9185 - mean_squared_error: 269.9084 - mean_absolute_error: 14.9394 - root_mean_squared_error: 16.4289
      ...
      ...
      Epoch 156: val_loss did not improve from 55.49997
      4/4 [==============================] - 4s 1s/step - loss: 39.4206 - mean_squared_error: 39.4083 - mean_absolute_error: 4.6351 - root_mean_squared_error: 6.2776 - val_loss: 80.0362 - val_mean_squared_error: 80.0239 - val_mean_absolute_error: 6.6511 - val_root_mean_squared_error: 8.9456 - lr: 1.0000e-09


* download model/data from kaggle working

`!tar cvf best_my_model_20230904_bs8_reduce_lr_efnv2xl_fine_tune_TPU.tar /kaggle/working/best_my_model_20230904_bs8_reduce_lr_efnv2xl_fine_tune_TPU/`

```python
from IPython.display import FileLink
FileLink(r'best_my_model_20230904_bs8_reduce_lr_efnv2xl_fine_tune_TPU.tar')
```

* 產生一個下載連結
![image](https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/f662f950-ceea-40ec-807a-55999800ae1d)


  
* * *

### 2023-03-25 ⚠ Bug Trace ⚠

* 計算預測影像品質的指標數據非常的好！ 
`(數據太好才是疑問的開始!)`

當看到MSE遠小於MAE時，發生了什麼事情？

由於MSE是取差值再平方，但是Tensor儲存時已經先轉成[0,1]了，因此計算MSE的差值都會小於1使得平方時使數值變得更小了。

[ToDo]計算MAE MSE PSNR SSIM時 必須把scale轉回[0,255]之後才能正確地計算！



* * *
## 已經終止的GPU進程無法根據nvidia-smi命令的PID殺死的問題解決方案

  ```python
  https://zhuanlan.zhihu.com/p/506686899
  首先使用linux中的fuser庫，這個庫在我的環境中不是自帶的庫，所以需要下載。
  下載命令如下：
  apt install psmisc
  安裝之後使用如下命令：
  fuser -v /dev/nvidia*
  在結果中發現，在不同的GPU上都有同一個進程，進程號為"53940"。
  為了確定這個進程是不是我們運行的程序，我們使用如下的方式來查看一下這個進程的信息。
  ps -ef|grep 53940
  最後使用上述提到的刪除進程的方法。
  kill -9 53940
  更新：
  從別人的博客裡面看到的，批量刪除進程的code
  sudo fuser -v /dev/nvidia* |awk '{for(i=1;i<=NF;i++)print "kill -9 " $i;}' | sudo sh
  或者針對某一個GPU刪除進程的code
  sudo fuser -v /dev/nvidia2 |awk '{for(i=1;i<=NF;i++)print "kill -9 " $i;}' | sudo sh
  參考： {不要加sudo!}
  ```

* * *

### TF Tensor 對Mask影像值進行過濾

##### mask = [1 if x > 0.5 else 0 for x in mask]
𝑓(𝑥)={(1, 𝑖𝑓 𝑥≥0.5  0, 𝑒𝑙𝑠𝑒.)
<img width="236" alt="image" src="https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/04c672b0-31ae-49a6-bdd2-13bc3177c488">

上:輸入 中:分割結果 下:分割過濾
<img width="236" alt="image" src="https://github.com/vscv/AllYouNeedToKnowAboutX/assets/18000764/23066424-a1f4-404a-a4de-4fffe7afc39a">

`tf.where`
```python
mask = tf.constant([[0.1,0.2,0.6,0.7], [0.5,0.7,0.3,0.4]])
tf.where(mask >= 0.5, 1, 0)

<tf.Tensor: shape=(2, 4), dtype=int32, numpy=
array([[0, 0, 1, 1],
       [1, 1, 0, 0]], dtype=int32)>
       
tf.where(mask > 0.5, 1, 0)

<tf.Tensor: shape=(2, 4), dtype=int32, numpy=
array([[0, 0, 1, 1],
       [0, 1, 0, 0]], dtype=int32)>
```

`tf.cast`
這是利用cast成整數型態時會~~自動四捨五入~~ ，算floor在轉型態。

```python
mask = tf.constant([[0.1,0.2,0.6,1.7], [0.5,0.7,0.3,0.4]])
tf.cast(mask + 0.5, tf.int32)
<tf.Tensor: shape=(2, 4), dtype=float32, numpy=
array([[0., 0., 0., 1.],
       [0., 0., 0., 0.]], dtype=float32)>
```

`tf.floor`取最大整數 1.7->1 # 捨去小數後最大整數
```python
tf.floor([0.1, 0.5, 0.9, 1.2, 1.9])
<tf.Tensor: shape=(5,), dtype=float32, numpy=array([0., 0., 0., 1., 1.], dtype=float32)>
```

`tf.round` # 四捨六入五取偶，當小數為0.5若整數為偶數則捨去小數取偶數，若為奇數則進位。

```python
tf.round([0.1, 1.5, 2.5, 0.5, 0.6, 1.2, 1.9])
<tf.Tensor: shape=(7,), dtype=float32, numpy=array([0., 2., 2., 0., 1., 1., 2.], dtype=float32)>
```

* * *
## kaggle 無網路環境下，預先下載套件再離線安裝
https://www.kaggle.com/competitions/severstal-steel-defect-detection/discussion/113195

* 取得wheel檔
```bash
#pip download [package_name], then you will get the whl file.

""" put a lot of wheels in dir """
mkdir wheels_dir
cd wheels_dir/
pip download segmentation-models
```

* 放入kaggle-> dataset自訂中，再由本地安裝
```bash
!pip install segmentation-models --no-index --find-links=file:///kaggle/input/wheels_dir/
```

* * *
# tf.image.resize, tf.image.resize_with_pad
`todo:回傳dtype差異，以及原始



* * *
# tensorboard

```bash
$tensorboard --logdir train_log/20231223-203132 --port 5000

# --port 若在公有雲請設成
#目標埠: 5000 (userdefine1)內部可見
#對外埠: 55955 (外部可見)
```

* tensorboard dev
`tensorboard dev upload --logdir {logs/}`
`2023/11/31終止該dev線上服務，請用回本地tensorboard！`

* tensorboard.data.experimental.ExperimentFromDev()
`僅支援讀取tensorboard dev的線上位址，因此也無法使用了。`

* from tensorboard.backend.event_processing.event_file_loader import RawEventFileLoader
https://github.com/tensorflow/tensorboard/issues/6388
```python
from tensorboardX import SummaryWriter
from tensorboard.backend.event_processing.event_file_loader import RawEventFileLoader
from tensorboard.compat.proto import event_pb2

loader = RawEventFileLoader("{path_to_your_logdir}/events.out.tfevents.{old_suffix}.ps") # it is a file name, need to add "ps"
events = []
for raw_event in loader.Load():
    e = event_pb2.Event.FromString(raw_event)
    # print(e)
    # print(e.step) # the "step" in my result is the index of training epoch, I want to choose the last 20 epochs.
    if e.step <= 100 and e.step > 80:
            events.append(e)

tb_log = SummaryWriter(log_dir="{path_to_your_logdir}/events") # it is a path, not a file, I create a folder called events
for e in events[1:]:   

    # For me, the first element in "events" seems not the result data, you can print "events[0:2]" to check it.
    # print(events[0:2])

    # wall_time: 1684237044.4711838
    # file_version: "brain.Event:2"

    # wall_time: 1684237250.0319963
    # step: 81
    # summary {
    #  value {
               # tag: "recall/roi_0.3"
               # simple_value: 0.9507125616073608
    # }
    # }

    # print(e.summary.value)
    # print(type(e.summary.value))
    for value in e.summary.value:
        # print(value.tag,value.simple_value, e.step)
        tb_log.add_scalar(str(value.tag),value.simple_value, e.step)
```



* * *
## PyTorch test

```python
import torch
import torch.nn as nn

print(f"What about a GPU? {torch.cuda.is_available()}")

print(f"Number about GPU? {torch.cuda.device_count()}")

print(f"What current GPU? {torch.cuda.current_device()}")

print(f"What name is GPU? {torch.cuda.get_device_name(torch.cuda.current_device())}")

print(f"Set default tensor type to CUDA: {torch.set_default_tensor_type(torch.cuda.FloatTensor)}")

print(f"Are tensors stored on GPU by default? {torch.rand(10).device}")
```


    What about a GPU? True
    Number about GPU? 1
    What current GPU? 0
    What name is GPU? Tesla V100-SXM2-32GB
    Set default tensor type to CUDA: None
    Are tensors stored on GPU by default? cuda:0
    torch_ver_major:1, dtype_index:torch.int64



* * *

* * *
* tfb with jupyter notebook
* * *


***
[TODO test]


https://www.tensorflow.org/guide/distributed_training
將 tf.distribute.Strategy 與自訂訓練循環結合使用
如上所示，tf.distribute.Strategy與 Keras 一起使用Model.fit只需更改幾行程式碼。只要多一點努力，您還可以使用自訂訓練循環。tf.distribute.Strategy

如果您需要比 Estimator 或 Keras 更大的靈活性和對訓練循環的控制，您可以編寫自訂訓練循環。例如，當使用 GAN 時，您可能希望每輪採用不同數量的生成器或判別器步驟。同樣，高階框架也不太適合強化學習訓練。



然後，定義訓練的一個步驟。用於tf.GradientTape計算梯度和最佳化器應用這些梯度來更新模型的變數。若要分發此訓練步驟，請將其放入函數中並將其與從先前建立的資料集輸入一起train_step傳遞：tf.distribute.Strategy.rundist_dataset




https://link.springer.com/article/10.1007/s11227-022-04354-1

https://media.springernature.com/full/springer-static/image/art%3A10.1007%2Fs11227-022-04354-1/MediaObjects/11227_2022_4354_Fig1_HTML.png![image](https://github.com/user-attachments/assets/09ff402a-8d8b-4d41-a630-4fbcefae5e17)

Fig. 1



如上所述，執行影像變換任務的生成對抗神經網路至少包含多個神經網路以及多個損失函數。這使得這些網路的訓練相當昂貴。為了減少訓練時間，[ 21 ]中提出了一種演化演算法，它可以穩定第一次迭代中的權重，以避免崩潰（總是從輸入影像產生相同的輸出）和不收斂（變換永遠不會發生）問題。該方法實現了更快的收斂。然而，該解決方案並沒有顯著提高系統的訓練速度，因為它沒有利用主要為系統提供速度的硬體資源。在[ 22 ]中，作者訓練了 Lapras-GAN，這是一種利用 SSIM 和 L1 來獲得逼真影像的影像超解析度方法。為了執行 PyTorch 訓練，使用多個具有多個 GPU 的節點，將訓練時間減少多達 4 倍。在VAE-GAN[ 23 ]中，TensorFlow用於執行多GPU訓練。簡而言之，多個 GPU 的結合可以顯著提高訓練速度。然而，上述的解決方案（Pix2Pix、CycleGAN、BicycleGAN）不包括多 GPU 訓練。

因此，為了利用訓練速度，有必要增加訓練批次的大小。此參數在訓練中非常重要，因為非常大的批量大小可以使訓練速度更快，但可能會導致模型過度泛化並且無法轉換影像細節。在一些工作中，提出了一些根據非生成對抗網絡中的紀元 [ 24 , 25 ] 和網絡層 [ 26 ] 改變批量大小的策略。

然而，先前尚未研究過 GAN（Pix2Pix 或 CycleGAN）中批量大小增加的影響。在這些解決方案中，在不同論文中建立了批量大小，但不建議增加批量大小。
***
