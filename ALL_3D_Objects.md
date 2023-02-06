# 關於數位化物件(digital objects) ex, STL, OBJ, VRML, Volume (stacked images), etc.
 * 目前有許多UI工具可使用 ex, ParaView, 3D Slicer等等等 (多數基於VTK)，此處我們聚焦在開發程式的使用。
 * vedo, pyvista, Slicer 等開發程式套件也是基於VTK的。
 * 
* * *
## 對於 3D 打印，我們將數字對象切成圖像堆棧，以便使用 3D 打印機逐層堆疊它們。切片完成後，如何標記內部/外部以設置實體部分？ 
 
#### 讀取與檢查3D模型

1. 以pyVista為例: 讀取STL、顯示模型、取得切片。

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

# take 10 slice images
for i in range(10):
    p = pv.Plotter(off_screen=True)
    p.add_mesh(slices[i])
    p.camera_position = 'zy'
    p.enable_parallel_projection()
    #p.show()
    im_name = "im_slice_" + str(i) + ".jpg"
    p.screenshot(im_name)

```

Show model
![sample_object_haus_s](https://user-images.githubusercontent.com/18000764/216750189-353560ab-2bb3-4aa2-9a12-755276bea61f.jpg)



Show slice
![sample_object_haus_slices_s](https://user-images.githubusercontent.com/18000764/216743709-b813f911-c822-43f4-b12f-ffdc3875c6d9.jpg)


Show single slice
![sample_object_haus_slice15_but_only_contour_s](https://user-images.githubusercontent.com/18000764/216743747-923aae0a-256a-4843-9be6-eb046a800df1.jpg)



`PyVista voxelize 由mesh建立voxel(體素)，這樣使內部填充了立體網格，再進行切片。`

```Python
import pyvista as pv
"""使用voxel當作內部填充 不是經濟做法 且體素粗細度直接影像輪廓的精確度。"""

#創建邊界表面的體素模型
voxels = pv.voxelize(mesh, density=mesh.length / 100)

#顯示體素
p = pv.Plotter()
p.add_mesh(voxels, color=True, show_edges=True, opacity=0.5)
p.add_mesh(mesh, color="lightblue", opacity=0.5)
p.show(cpos='xy')

#切片體素
#slices = voxels.slice_along_axis(n=20, axis='z', progress_bar=True)  #, contour=True
#顯示切片
#slices[15].plot(cpos=[0, 1, 1], line_width=5, parallel_projection=True,) # set cpos
```


Show Voxel
![try-1_pyvista__voxelize_+mesh_s](https://user-images.githubusercontent.com/18000764/216754089-66ad538d-0c78-42b7-87b1-68ab3b3468f6.jpg)


Show slice of voxel
![try-1_pyvista__voxelize_slice_dense500_s_crop](https://user-images.githubusercontent.com/18000764/216756669-fd48624c-7e61-48a4-a857-fc57938f2225.jpg)

* * *


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

 
 VTK切片 修改自https://kitware.github.io/vtk-examples/site/Python/PolyData/PolyDataContourToImageData
 
 ```Python
import vtk

filename = './haus.stl'
reader = vtkSTLReader()
reader.SetFileName(filename)
reader.Update()
    
stlMapper = vtk.vtkPolyDataMapper()
stlMapper.SetInputConnection(reader.GetOutputPort())

polydata = stlMapper
print("Get GetOrigin", polydata.GetCenter())
sphereSource = reader 

circleCutter = vtkCutter()
circleCutter.SetInputConnection(sphereSource.GetOutputPort())
cutPlane = vtkPlane() 

circle = stripper.GetOutput()    
    
# prepare the binary image's voxel grid
whiteImage = vtkImageData()
bounds = [0] * 6
circle.GetBounds(bounds) 
spacing = [0] * 3  # desired volume spacing
spacing[0] = 0.5
spacing[1] = 0.5
spacing[2] = 0.5
whiteImage.SetSpacing(spacing)    

# compute dimensions
dim = [0] * 3
for i in range(3):
    dim[i] = int(math.ceil((bounds[i * 2 + 1] - bounds[i * 2]) / spacing[i])) + 1
    if dim[i] < 1:
        dim[i] = 1

whiteImage.SetDimensions(dim) 
whiteImage.SetExtent(0, dim[0] - 1, 0, dim[1] - 1, 0, dim[2] - 1)
origin = [0] * 3
# NOTE: I am not sure whether or not we had to add some offset!
origin[0] = bounds[0]  # + spacing[0] / 2
origin[1] = bounds[2]  # + spacing[1] / 2
origin[2] = bounds[4]  # + spacing[2] / 2
print("check origin ", origin)
whiteImage.SetOrigin(origin)
whiteImage.AllocateScalars(VTK_UNSIGNED_CHAR, 1)

# fill the image with foreground voxels: (to set up the inner/outer gray scale.)
inval = 0
outval = 255
count = whiteImage.GetNumberOfPoints()

#for i in range(count):
#  whiteImage.GetPointData().GetScalars().SetTuple1(i, inval)
whiteImage.GetPointData().GetScalars().Fill(inval) # use Fill faster than for loop setup.

# sweep polygonal data (this is the important thing with contours!)
extruder = vtkLinearExtrusionFilter()
extruder.SetInputData(circle)
extruder.SetScaleFactor(1.0)
# extruder.SetExtrusionTypeToNormalExtrusion()
extruder.SetExtrusionTypeToVectorExtrusion()
extruder.SetVector(0, 0, 1)
extruder.Update()
    
# polygonal data -. image stencil:
pol2stenc = vtkPolyDataToImageStencil()
pol2stenc.SetTolerance(0)  # important if extruder.SetVector(0, 0, 1) !!!
pol2stenc.SetInputConnection(extruder.GetOutputPort())
pol2stenc.SetOutputOrigin(origin)
pol2stenc.SetOutputSpacing(spacing)
pol2stenc.SetOutputWholeExtent(whiteImage.GetExtent())
pol2stenc.Update()

# cut the corresponding white image and set the background:
imgstenc = vtkImageStencil()
imgstenc.SetInputData(whiteImage)
imgstenc.SetStencilConnection(pol2stenc.GetOutputPort())
imgstenc.ReverseStencilOff()
imgstenc.SetBackgroundValue(outval)
imgstenc.Update()    

imageWriter = vtkPNGWriter()
imageWriter.SetFileName('vtk_slice_test_case.png')
imageWriter.SetInputConnection(imgstenc.GetOutputPort())
imageWriter.Write()


if __name__ == '__main__':
    main()
 ```

![labelImage_-10_b_200](https://user-images.githubusercontent.com/18000764/216753841-4da96e36-43b3-4ef3-926a-8545931f9c56.png)

 PS.原本的VTK語法太冗長了。😰


* * *
3. 以3D slicer為例

3D slicer有提供UI介面與API工具，優點有提供完整的雲端虛擬機讓你使用[SlicerWeb](https://mybinder.org/v2/gh/Slicer/SlicerNotebooks/master?filepath=SlicerWeb.ipynb)，是可以使用jupyter notebook開啟它的介面，非常方便連安裝clinet端都不需要。也可以自己建立一個notebook共享服務器，滿適合給實驗室小組習作。

`在jupyter notebook中啟用Slicer介面`

```Python
import JupyterNotebooksLib as slicernb
import slicer
import ipywidgets

# Run this cell (Shift+Enter) to show application here
slicernb.AppWindow(contents='full')

# # Show viewers only
# slicernb.AppWindow(contents='viewers');

# # Show full application window
# slicernb.AppWindow(contents='full');
```


![try-3_3D_SlicerWeb_ok_s](https://user-images.githubusercontent.com/18000764/216756993-ed28cfbf-21cb-4331-80fc-0f8c7c076a39.jpg)
這是jupyter notebook的實際截圖，非client端程式，僅是用來顯示讀取的模型是正確的，並沒有用來操作切片任務。


`用3D Slicer切片` 修改自[Rasterize a model and save it to a series of image files](https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/models.html#rasterize-a-model-and-save-it-to-a-series-of-image-files)

```Python
import JupyterNotebooksLib as slicernb
import slicer
import ipywidgets
import vtk
from slicer.util import pip_install

# This example shows how to generate a stack of image files from an STL file:
inputModelFile = "./data/haus.stl"
outputDir = "./outputs/"
outputVolumeLabelValue = 100
outputVolumeSpacingMm = [0.5, 0.5, 0.5]   #調整 outputVolumeSpacingMm 值來設置任何分辨率（前兩個值是切片內的圖像間距，第三個值是切片之間的圖像間距）
outputVolumeMarginMm = [10.0, 10.0, 10.0]

# Read model
inputModel = slicer.util.loadModel(inputModelFile)

# Determine output volume geometry and create a corresponding reference volume
import math
import numpy as np
bounds = np.zeros(6)
inputModel.GetBounds(bounds)
imageData = vtk.vtkImageData()
imageSize = [ int((bounds[axis*2+1]-bounds[axis*2]+outputVolumeMarginMm[axis]*2.0)/outputVolumeSpacingMm[axis]) for axis in range(3) ]
imageOrigin = [ bounds[axis*2]-outputVolumeMarginMm[axis] for axis in range(3) ]
imageData.SetDimensions(imageSize)
imageData.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 1)
imageData.GetPointData().GetScalars().Fill(0)
referenceVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
referenceVolumeNode.SetOrigin(imageOrigin)
referenceVolumeNode.SetSpacing(outputVolumeSpacingMm)
referenceVolumeNode.SetAndObserveImageData(imageData)
referenceVolumeNode.CreateDefaultDisplayNodes()

# Convert model to labelmap
seg = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
seg.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)
seg.CreateBinaryLabelmapRepresentation()
outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, outputLabelmapVolumeNode, referenceVolumeNode)
outputLabelmapVolumeArray = (slicer.util.arrayFromVolume(outputLabelmapVolumeNode) * outputVolumeLabelValue).astype("int8")

# Write labelmap volume to series of TIFF files
pip_install("imageio")

import imageio
# for i in range(len(outputLabelmapVolumeArray)):
#   imageio.imwrite(f"{outputDir}/image_{i:03}.jpg", outputLabelmapVolumeArray[i])
for i in range(80,140, 10):
  imageio.imwrite(f"{outputDir}/image_{i:03}.jpg", 255 - outputLabelmapVolumeArray[i]) # Inverting Colors
```

* * *
4. 以vedo為例



* * *
 
#### 交換切片影像的BW
若拿到的原始切片是黑白相反時，可以簡單交換回來。反之亦然。


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
