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

# 雲端主機連不上 
## 更新OpenSSH後公鑰（public key）的登入方式失效
這是因為更新後/etc/ssh/sshd_config會重設將公鑰登入方式取消，但如果你不小心退出或重啟VM/VCS，就會無法用公鑰登入了。

### TWCC/TWS 的進入救援模式，重設帳密後登入，修改/etc/ssh/sshd_config 
* [從安全模式進入 VCS 個體](https://tws.twcc.ai/vcs-safe-mode/)
1. 在雲端介面下，`點下 Console 右上 SendCtrlAltDel，立即連按下鍵盤的 esc 鍵`
2. 注意要連續點esc，不行的話重試幾次！！成功的話會進入開機選單，選擇 Advanced options for Ubuntu
3. 選擇 recovery mode --> 選擇 root --> 建立帳號密碼 $passwd ubuntu （為帳號 ubuntu 設定密碼）
4. 點選 Console 右上 SendCtrlAltDel 進行重開機，以剛剛設定的帳密登入。

* 重新啟用公鑰登入並取消密碼登入
1. 登入後檢查帳號下的公鑰檔案是否還在，cat /home/ubuntu/.ssh/authorized_keys 如果內容還在，就可以恢復公鑰登入。
2. 打開 /etc/ssh/sshd_config，檢查並確保以下設定存在且正確（用 root 權限）：
   ```bash
   PubkeyAuthentication yes
   AuthorizedKeysFile .ssh/authorized_keys
   PasswordAuthentication no   # 建議恢復安全性時設為 no，修復階段可暫設 yes
   ```
3. 重啟 ssh 服務: `sudo systemctl restart ssh` or `sudo service ssh restart` or `重開機`
4. 測試公鑰登入: ssh -i ~/.ssh/你的私鑰 ubuntu@你的伺服器IP

#### 學到的教訓
* 修好後建議將 PasswordAuthentication 設回 no，只用公鑰登入。
* 建議備份 /etc/ssh/sshd_config 和 ~/.ssh/authorized_keys。
* 事先調查一下更新安裝、重新編譯會造成的影響，免得措手不及。


#### 【但是，如果authorized_keys 檔案不見怎麼辦？】
* 若本地還有對應的私鑰（.pem/.ppk），可以把對應的 public key 內容再補進去。如果有備份的話＠＠
* 若所有 key 都遺失，只能用密碼登入或透過 Console、single-user mode、救援模式重新配置新的密鑰。
