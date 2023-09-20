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

