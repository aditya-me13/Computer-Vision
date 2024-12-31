# Computer-Vision Tasks (from scratch):
---


## Pre-requisites:
To run the project, it is advised to make a virtual environment and install the required packages. To do so, follow the steps below:

1. Create a virtual environment using the following command:
``` bash
conda create --name CV python=3.10
```
2. Activate the virtual environment using the following command:
``` bash
conda activate CV
```
3. Install the required packages using the following command:
``` bash
pip install -r requirements.txt
```

## Task A:
Add noise to the images and remove it using various smoothening filters. Apply Canny Edge Detection to the images.

<image src="src/taskA/results/original.png" height="250"> <image src="src/taskA/results/self.png" height="250"> <image src="src/taskA/results/heatmap.png" height="250">

## Task B:
Implement Gaussian Pyramid Downsampling from scratch. Implement Image Blending using Laplacian Pyramid. Finally apply Harris and Hessian Corner Detection algorithm.

<image src="src/taskB/results/blend.png" width="880">

<img src="src/taskB/results/harris/parrot.png" alt="Image description"  width="220"><img src="src/taskB/results/harris/chess.png" alt="Image description"  width="220"><img src="src/taskB/results/harris/cat.png" alt="Image description"  width="220"><img src="src/taskB/results/harris/rome.png" alt="Image description"  width="220">

## Task C:
Implement Panorama Stitching from scratch.

<div style="display: inline-block;">
    <img src="data/images/C/I6/1_1.JPG" alt="Image 1" style="height: 120px; margin-right: 5px;">
    <img src="data/images/C/I6/1_2.JPG" alt="Image 2" style="height: 120px; margin-right: 5px;">
    <img src="data/images/C/I6/1_3.JPG" alt="Image 3" style="height: 120px; margin-right: 5px;">
    <img src="data/images/C/I6/1_4.JPG" alt="Image 4" style="height: 120px; margin-right: 5px;">
    <img src="data/images/C/I6/1_5.JPG" alt="Image 5" style="height: 120px;">
</div>
<img src="src/taskC/results/I6.png" alt="Image description" width="660">

## Task D:
Implement Lucas-Kanade Optical Flow Algorithm from Scratch

![video](src/taskD/results/flow/2.gif)
![video](src/taskD/results/flow/5.gif)  

![video](src/taskD/results/flow/6.gif)
![video](src/taskD/results/flow/7.gif)

## Task E:
Estimate the Camera Matrix between pair of Stereo Images by finding the matching points. Finally find the disparity map for the stereo images.

 <image src="src/taskE/results/disparity/1.png" height="250"> <image src="src/taskE/results/disparity/2.png" height="250"> <image src="src/taskE/results/disparity/3.png" height="250"> 