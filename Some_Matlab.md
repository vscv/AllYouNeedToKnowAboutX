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
![image](https://user-images.githubusercontent.com/18000764/223909114-8405aea7-f9bc-4b89-9f41-9094bf96c2bb.png)
 ➩
![image](https://user-images.githubusercontent.com/18000764/223909049-7b82f502-6205-4602-b6f6-2e3517b8e5d9.png)



#### 繪圖存檔

```Matlab
%% ADD figure obj
figure('Name','Spectrum Data');

for i = 1:numel(bubble_list)
    disp(bubble_list(i));
    load(bubble_list{i})

    R2=reshape(data,[recordLength fastFrameCount]);
    fs=1/sampleInterval;
    faxis2 = [0:recordLength-1]/(recordLength-1)*fs/1E6;
    for ii=1:fastFrameCount
        ft2=abs(fft(R2(:,ii)));
        spectrum_before2=20*log10((ft2));
        spectrum2(:,ii)=spectrum_before2-noise_level;
    end

    s2=mean(spectrum2, 2)-0.5;
    
    plot(faxis2(:),s2(:,1),'linewidth',3);
    hold on;
end

%% Figure out
Xi = [0]  ; 
Xe = [60]; 
Yi = [-inf]; 
Ye = [inf]; 

sum_of_legend= [water_list, bubble_list]
no_posfix_sum_of_legend = strrep(sum_of_legend, '.mat', '')
no_posfix_sum_of_legend

legend(no_posfix_sum_of_legend, 'Location','best')

axis([Xi Xe Yi Ye]);
set(gca,'linewidth',2);
set(gca,'fontsize',15,'fontweight','bold');
title('Spectrum','fontsize',20);
xlabel(['Frequency(MHz)']);
ylabel(['dB']);

%% Export the Spectrum_plot to png
f = gcf;
exportgraphics(f,'0306_Spectrum_plot.png')
```

#### 去除檔名列表中的特定字符

`no_posfix_sum_of_legend = strrep(sum_of_legend, '.mat', '')`
replace all '.mat' in list by "".


#### 各種參數清理
`clear;clc ; clear all; close all;`


* * *
### 排列figure視窗
https://www.mathworks.com/matlabcentral/fileexchange/55468-align-figures-without-overlap

![image](https://user-images.githubusercontent.com/18000764/225803703-cf85aa0d-9666-4069-8530-73b1fe5d1c53.png)

```Matlab
% Position — Location and size of drawable area : [left bottom width height]
% OuterPosition — Location and size of drawable area : [left bottom width height] 注意 這是對整個外框
```

```Matlab
%
% Reset the figure window location. Horizontal
%
if if_set_figs_vertical_true 
    figs = [fig_1, fig_2, fig_3, fig_4]
    nfig = length(figs);
    for K = 1 : nfig
      old_pos = get(figs(K), 'Position')
      set(figs(K), 'Position', [(K-1)*old_pos(3) old_pos(2) old_pos(3) old_pos(4)]);
    end
end
```

![image](https://user-images.githubusercontent.com/18000764/226075598-b6d2b33f-fbdb-4909-a19e-66b84181e28f.png)

```Matlab
%
% Reset the figure window location. Grid
%

% fake figs
fig_1 = figure();fig_2 = figure();fig_3 = figure();fig_4 = figure();

if if_set_figs_vertical_true 
    figs = [fig_1, fig_2, fig_3, fig_4]
    nfig = length(figs);
    
    % grid-line 1
    for K = 1 : 2                              % OuterPosition 注意 這是對整個外框
      old_pos = get(figs(K), 'OuterPosition')  % 這裡抓的是預設位置 中央上方，故old_pos(2)就沿用為頂排button
      set(figs(K), 'OuterPosition', [(K-1)*old_pos(3) old_pos(2) old_pos(3) old_pos(4)]);
      get(figs(K), 'OuterPosition')
    end
    % grid-line 2
    for K = 3 : 4
      old_pos = get(figs(K), 'OuterPosition') %第二排位置應該是 old_pos(2) - old_pos(4) 才對，即第一排底往下減一個height高度
      set(figs(K), 'OuterPosition', [(K-3)*old_pos(3) (old_pos(2) - old_pos(4)) old_pos(3) old_pos(4)]);
      get(figs(K), 'OuterPosition')
    end

end
```
note: 因切換不同外接螢幕、接多螢幕時，位置可能會改變。請再調整get(fig_#)取得當下視窗預設位置。

note: 因是將已經繪出在螢幕的視窗重新調整位置，所以會看到所有視窗顯示完後，才再移動到指定位置。

[作業]如何先排好視窗位置後才進行繪圖。不能這樣做的原因是？怎麼解決？有較優雅的方法嗎？如果用Python工具要怎麼做？


***
