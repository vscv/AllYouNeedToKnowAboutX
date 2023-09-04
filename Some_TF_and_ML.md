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

e.g. "TPU v3-8" 8核心 128GB memory。

⭕️ 沒資源的話可以上kaggle註冊，一週有20小時的TPU可以使用。



* * *

### 2023-03-25 ⚠ Bug Trace ⚠

* 計算預測影像品質的指標數據非常的好！ 
`(數據太好才是疑問的開始!)`

當看到MSE遠小於MAE時，發生了什麼事情？

由於MSE是取差值再平方，但是Tensor儲存時已經先轉成[0,1]了，因此計算MSE的差值都會小於1使得平方時使數值變得更小了。

[ToDo]計算MAE MSE PSNR SSIM時 必須把scale轉回[0,255]之後才能正確地計算！


