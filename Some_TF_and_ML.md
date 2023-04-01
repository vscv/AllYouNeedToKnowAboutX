### 2023-03-25 ⚠ Bug Trace ⚠

* 計算預測影像品質的指標數據非常的好！ 
`(數據太好才是疑問的開始!)`

當看到MSE遠小於MAE時，發生了什麼事情？

由於MSE是取差值再平方，但是Tensor儲存時已經先轉成[0,1]了，因此計算MSE的差值都會小於1使得平方時使數值變得更小了。

[ToDo]計算MAE MSE PSNR SSIM時 必須把scale轉回[0,255]之後才能正確地計算！