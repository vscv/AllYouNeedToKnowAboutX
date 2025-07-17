### 誤用已定義的變數函數

```def PencilScribbles(tras_img):
    ink_phase = []
    paper_phase = []
    post_phase = [
    PencilScribbles(
        size_range=(100, 800),
        count_range=(1, 6),
        stroke_count_range=(1, 2),
        thickness_range=(2, 6),
        #brightness_change=random.randint(64, 224),
        brightness_change=128,
        p=1,
    ),]
    pipeline = AugraphyPipeline(ink_phase, paper_phase, post_phase)
    
    return pipeline.augment(tras_img)["output"]
```

TypeError: PencilScribbles() got an unexpected keyword argmunet "size_range"


原本裡面的PencilScribbles()是來自from augraphy，但自訂函數用了相同的名字造成。

***

### ipynb (jupyter notebook/lab) import 自製套件
每次更新套件原始碼如script.py時，import前請restart kernel。

```Python3
from ZhuYin.zytk.zytk import transforms_pixel_level,transforms_spatial_level
```
`can not import "xxxx fun or var" from $your_local_script_py/local.py`


* * * 

雲端主機連不上

[從安全模式進入 VCS 個體](https://tws.twcc.ai/vcs-safe-mode/)
