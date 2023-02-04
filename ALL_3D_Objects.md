# 關於數位化物件(digital objects) ex, STL, OBJ, VRML, Volume (stacked images), etc.
 * 目前有許多UI工具可使用 ex, Mesh3D, ParaView, 3D Slicer等等等 (多數基於VTK)，此處我們聚焦在工具程式的使用。
 * 套件也是基於VTK的vedo, pyvista, Slicer 等
 * 
* * *
## 對於 3D 打印，我們將數字對象切成圖像堆棧，以便使用 3D 打印機逐層堆疊它們。切片完成後，如何標記內部/外部以設置實體部分？ 
 
#### 讀取與檢查3D模型

1. 以pyVista為例

```Python
import pyvista as pv

mesh = pv.read('./haus.stl') 
print("bounds=", mesh.bounds) 

# show model
#mesh.plot()

# set slice, n = how many slice
slices = mesh.slice_along_axis(n=20, axis='z', progress_bar=True) 

# show slice
#slices.plot(line_width=5)

# get slice points
#slice_points = slices[4].points 

# show single slice with camera setting
#slices[15].plot(cpos=[0, 1, 1], line_width=5, parallel_projection=True,)

```

Show model
![sample_object_haus_s](https://user-images.githubusercontent.com/18000764/216750189-353560ab-2bb3-4aa2-9a12-755276bea61f.jpg)



Show slice
![sample_object_haus_slices_s](https://user-images.githubusercontent.com/18000764/216743709-b813f911-c822-43f4-b12f-ffdc3875c6d9.jpg)


Show single slice
![sample_object_haus_slice15_but_only_contour_s](https://user-images.githubusercontent.com/18000764/216743747-923aae0a-256a-4843-9be6-eb046a800df1.jpg)




2. 以VTK為例

```Python
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOGeometry import vtkSTLReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors() 
    filename = './haus.stl'
  
    reader = vtkSTLReader()
    reader.SetFileName(filename)
    reader.Update()
    
    # STL
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetDiffuse(0.8)
    actor.GetProperty().SetDiffuseColor(colors.GetColor3d('LightSteelBlue'))
    actor.GetProperty().SetSpecular(0.3)
    actor.GetProperty().SetSpecularPower(60.0)

    # Create a rendering window and renderer
    ren = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.Render()
    renWin.SetWindowName('ReadSTL [haus]')

    # Create a renderwindowinteractor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Assign actor to the renderer
    ren.AddActor(actor)
    ren.SetBackground(colors.GetColor3d('DarkOliveGreen'))

    # Enable user interface interactor
    iren.Initialize()
    iren.Start()    
    
if __name__ == '__main__':
    main()
```

show model
![VTK_read_show_STL_s](https://user-images.githubusercontent.com/18000764/216752118-45e60be1-c9f8-4d0f-9a0d-a0de0ff2edd0.jpg)

PS.這也是為何有好多基於VTK重新開發的工具出現，原本的VTK語法太冗長了。😰

 
 
 
#### 交換切片影像的BW
若拿到的原始切片是黑白相反時，可以簡單交換回來。

![Figure_inv_color_image_s](https://user-images.githubusercontent.com/18000764/216742696-05ded5d7-d336-45c4-a95b-31916acdee29.jpg)

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
