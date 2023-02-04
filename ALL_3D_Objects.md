# 關於數位化物件(digital objects) ex, STL, OBJ, VRML, Volume (stacked images), etc.
 * 目前有許多UI工具可使用 ex, Mesh3D, ParaView, 3D Slicer等等等 (多數基於VTK)，此處我們聚焦在工具程式的使用。
 * 套件也是基於VTK的vedo, pyvista, Slicer 等
 * 
* * *
## 對於 3D 打印，我們將數字對象切成圖像堆棧，以便使用 3D 打印機逐層堆疊它們。切片完成後，如何標記內部/外部以設置實體部分？ 
 

 
#### 交換切片影像的WB
```Python
import imageio
import matplotlib.pyplot as plt

img_path = './image_134.jpg'

def inverted_color(img_path):
    img = imageio.imread(img_path)
    print("org dtype", img.shape, img.dtype)
    #img = img.astype('float32') # its ok but get float32 image
    img = 255 - img
    print("inv dtype", img.shape, img.dtype)
    return img
    

img_org = imageio.imread(img_path)
img_inv = inverted_color(img_path)

imageio.imwrite("inv_img.jpg", img_inv)

plt.figure(figsize=(10,10))
plt.subplot(121)
plt.title("org")
plt.imshow(img_org, cmap='gray')
plt.subplot(122)
plt.title("inv")
plt.imshow(img_inv, cmap='gray')
plt.show()
```
 
* * *
  
  
  
  
* * *
