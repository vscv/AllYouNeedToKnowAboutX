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

⭕️ 沒資源的話可以上kaggle註冊，一週有20小時的TPU可以使用。



* * *

### 2023-03-25 ⚠ Bug Trace ⚠

* 計算預測影像品質的指標數據非常的好！ 
`(數據太好才是疑問的開始!)`

當看到MSE遠小於MAE時，發生了什麼事情？

由於MSE是取差值再平方，但是Tensor儲存時已經先轉成[0,1]了，因此計算MSE的差值都會小於1使得平方時使數值變得更小了。

[ToDo]計算MAE MSE PSNR SSIM時 必須把scale轉回[0,255]之後才能正確地計算！


