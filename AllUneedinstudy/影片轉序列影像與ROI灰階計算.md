# 影片轉序列影像與ROI灰階計算
本文實作了一種序列影像ROI像素強度計算。首先，使用FFMPEG工具將原始影像轉換成序列影像，以方便進行後續處理。接著，對序列影像中的ROI區域進行像素強度計算，得到該區域在不同時間點上的像素強度值。最後，統計這些像素強度值的變化，得到像素強度變化圖，用於分析序列影像中ROI區域的時間演化趨勢。


這種方法可以應用於多種序列影像的分析，例如醫學影像中的腫瘤跟踪和細胞學中的細胞追蹤等。以下是一些未來可能應用該技術的領域：

1. 醫學影像學：可以應用在CT、MRI等醫學影像中，計算ROI區域的像素強度，進而分析患者的病情。

2. 環境監測：可以應用在空氣、水質等環境監測領域，計算ROI區域的像素強度，進而分析污染物的濃度和分布情況。

3. 工業檢測：可以應用在工業檢測領域，對機器設備的各個部位進行像素強度計算，以進行設備故障檢測和預防性維護。

4. 生命科學：可以應用在生命科學領域，計算細胞影像的ROI區域的像素強度，從而對細胞的功能和病理狀態進行研究。

5. 智能交通：可以應用在智能交通領域，對交通影像中的ROI區域進行像素強度計算，從而進行交通流量的預測和路況分析。

* FFmpeg是一個免費、開源的跨平台音視頻編解碼器，它能夠將音視頻等多媒體數據進行格式轉換、編解碼、剪輯、合併等操作。使用FFmpeg可以透過指令運行對多媒體數據進行處理。


## workflow

1. 首先把實驗錄影中的ROI儲存為PNG檔。
<p align="center"> <img width=40% height=40% src="https://user-images.githubusercontent.com/18000764/234156216-116f6996-0a34-4dca-9838-52ac423c5210.jpg"> </p>
<p align="center"> <img width=40% height=40% src="https://user-images.githubusercontent.com/18000764/234157081-1acbf2f2-ff69-48a4-a126-566ec1c544c3.png"> </p>

2. 將目錄下所有原始錄影轉成序列影像。

`使用指令列印，再貼上termial執行`

```Python3
"""
 ▶ py Print_the_name_based_commands_for_FFMPEG_video2images.py 20230411_Video
"""
import os
import sys


dir_root = sys.argv[1]

for file in os.listdir(dir_root):
    if file.endswith(".mp4"):
        mp4_dir_name = os.path.splitext(file)[0]
        mp4_dir_path = dir_root + '/' + mp4_dir_name
        
        os.mkdir(mp4_dir_path)
        print(f"Q make jpgoutput dir {mp4_dir_path}")

        print(f"ffmpeg -i {dir_root + '/' + file} -vf fps=1 -qscale 0 {dir_root + '/' + mp4_dir_name}/{mp4_dir_name}_%05d.jpg")
```


3. 計算每個子資料夾下序列影像之ROI灰階
```Python3
# Usage: $python3 Compute_pixel_mean_in_RoI.py 20230406 
#
# ex:
# Compute_pixel_mean_in_RoI.py
# 02030406/
#         /100_cycle
#         /101_cycle
#         /102_cycle
#

"""
1. imageio to imageio.v3 as iio
2. up-level the output files.
"""

import os
import sys
import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt
import natsort
import pandas as pd
from tqdm import tqdm

def get_filename_from_dir(data_Dir):

    file_name_list = []
    #FV_val_list = []

    for file in os.listdir(data_Dir): #FD_img
        #print(file)
        #print(os.path.splitext(file))
        
        if file.endswith(".jpg"):
            file_name = os.path.splitext(file)[0] # to remove the .jpg postfix
            file_name_list.append(file_name)
        
    return natsort.natsorted(file_name_list) # make it ordered.


def get_gray_intensity_in_roi(dir_root, dir_name):
    
    # All set as default name #
    roi_img = dir_root + "/" + dir_name + "/" + dir_name + "_Mask.png"
    #print(f"Q {roi_img}")
    RG = iio.imread(roi_img)
    RGBin = RG > 200
    RGBinMasked = np.ma.masked_where(RGBin == 0, RGBin)
    
    filename_list = get_filename_from_dir(dir_root + "/" + dir_name + "/")
    #print(f"Q {filename_list}")
    
    #csv_name = dir_root + "/" + dir_name + "/" + dir_name + "_CSV.csv"
    csv_name = dir_root + "/" + dir_name + "_CSV.csv"
    #print(f"Q {csv_name}")
    #plt_name = dir_root + "/" + dir_name + "/" + dir_name + "_Plot.png"
    plt_name = dir_root + "/" + dir_name + "_Plot.png"
    # All set as default name #
    
    compute_val_list = []
    for jpg_name in tqdm(filename_list):
        img = iio.imread(dir_root + "/" + dir_name + "/" + str(jpg_name) + ".jpg")
        img = np.dot(img, [0.2989, 0.5870, 0.1140]) # comvert to gray scale
        
        new_roi_img = img[:,:][RGBinMasked]
        g_mean=np.mean(new_roi_img)
        g_max=np.max(new_roi_img)
        g_min=np.min(new_roi_img)
        g_std=np.std(new_roi_img)
        g_area=len(new_roi_img)
        #print(f"Q mean: {g_mean}, max: {g_max}, min: {g_min}, std: {g_std}, area: {g_area}")
        compute_val_list.append([g_mean,g_max,g_min,g_std,g_area])

    data_n_v = []
    for n,v in zip(filename_list, compute_val_list): # here, n=str, v=int
        v = [float(vv) for vv in v]
        #print(f"Q {n,v}")
        joint_list_n_v = [n] + v
        data_n_v.append(joint_list_n_v)
        
    
    # Create the pandas DataFrame
    df = pd.DataFrame(data_n_v, columns=['image', 'mean', "max",  "min",  "std", "area"])

    df.to_csv(csv_name, index=False)

    #print(f"Q {data_n_v[1]}")
    
    # plot the every one #
    df.plot(subplots=True, figsize=(10,20))
    plt.savefig(plt_name)
    
    
# One dir by one dir in the root dir #
def main():
    """
    # Usage: $python3 Compute_pixel_mean_in_RoI_MacOS.py 20230406 100_cycle
    """
    try:
        if len(sys.argv) != 3: # 0 1 2 = 3
            raise ValueError('The path and target of directory not giving!')
        # OK GO
        dir_root = sys.argv[1]
        dir_name = sys.argv[2]
        get_gray_intensity_in_roi(dir_root, dir_name)

    except ValueError as e:
        print("Error:", e)


# Compute all dirs in the root dir #
def main_do_all():
    """
    # Usage: $python3 Compute_pixel_mean_in_RoI_MacOS.py 20230406
    """
    try:
        if len(sys.argv) != 2: # 0 1 = 2
            raise ValueError('The path and target of directory not giving!')
        # OK GO
        print(f"Q")
        dir_root = sys.argv[1]

        for dir_name in os.listdir(dir_root):
            print(f"Q {os.path.abspath(dir_root + '/' + dir_name)}")
            if os.path.isdir(os.path.abspath(dir_root + "/" + dir_name)):
                print(f"Q name.........{dir_name}")
                get_gray_intensity_in_roi(dir_root, dir_name)
            else:
                print(f"Q not the dir?")

    except ValueError as e:
        print("Error:", e)
        

if __name__ == '__main__':
    #main()
    main_do_all()
```


