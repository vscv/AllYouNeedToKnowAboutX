# Some thing about the Matlab

`學術界主要還是使用Matlab當作數值計算工具，雖然有優缺點，碰上了還是記錄一下。`

* * *

#### Matlab的內建檔案比較功能

* 在Current Folder中選擇要比較的檔案或目錄，再按右鍵選擇"Compare Selected Files/Folders"

![image](https://user-images.githubusercontent.com/18000764/223026565-abb6ea48-6a02-4290-8228-b21c0391decb.png)


* 比較視窗，相異處會幫你高亮顯示。

![image](https://user-images.githubusercontent.com/18000764/223026837-46f5932d-2f73-4bc7-b82f-b7be1b1ef283.png)




* * *
#### Legend 圖說位置

`legend(no_posfix_sum_of_legend, 'Location','best')` 通常只要選`best`就會自動避掉繪圖區。最糟就畫在圖框之外，但不建議，可以用縮放大小、微調lcn位置或把lcn背景反白等手法，減少覆蓋的繪圖資訊。

![image](https://user-images.githubusercontent.com/18000764/223908119-4f40b762-f691-4825-9dae-cea1d893d1f4.png)

***
#### Matlab的字串排序
Ref:https://zhuanlan.zhihu.com/p/600265985/, https://www.mathworks.com/matlabcentral/fileexchange/47434-natural-order-filename-sort

    % bubble_list is a 1×2 cell array  and sort is not work for cell array!! %
    % 由於字符串是ASCII編碼的，字符串中的數字對應的是ASCII碼中的順序。如果在MATLAB中如果直接利用sort函數，對超過10的字符串進行排序，得到的結果並非是自然排序：%
    % 例如，根據ASCII碼的順序，字符串1到20的順序是：1，10，11，12，13，14，15，16，17，18，19，2，20，3，4，5，6，7，8，9
    % 所以在進行字符串排序的時候，需要把字符串中的數字轉換為數字類型，然後進行排序，得到的才是正確的順序。
    % 這一操作在MATLAB中，已有現成的輪子，natsort函數：請自行下載https://www.mathworks.com/matlabcentral/fileexchange/47434-natural-order-filename-sort
    % 改用natsortfiles 直接在 dir檔名列表時即做好排序。


```Matlab
%% Parse water/bubble files
water_dir = dir('*water.mat')
water_dir = natsortfiles(water_dir);
water_list = {water_dir.name}
% water_list(1)
numel(water_list)
for i = 1:numel(water_list)
    disp(water_list(i));
end

```
