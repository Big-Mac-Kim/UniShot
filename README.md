# UniShot
UniShot is a visual localization framework based on the "comparison neural network" architecture.
" It can be used by an eye-in-hand robot arm or a hand-held camera for precision positioning guidance.
There are Sliding_21.hdf5 model, Depth_13.hdf5, and two identification programs available.
## How To Use
The Sliding_21.hdf5 model is a dual-input neural network for plane Sliding localization guidance, which needs to be loaded in 
unishot_cam_SLIDING.py,
you need to take a global photo of the scene at its center in advance for the baseline as the basic image ,
then captured the photo by the camera as the compare images, 
During the operation,
UniShot will automatically compare the relative sliding of the two images and give the predicted relative sliding value,
This model has 21 labels and each label change represents a 10-pixel plane Sliding displacement.
,(10,10) indicates that the camera's viewpoint is at the center of the basic image.

 The Depth_13.hdf5 model is also a dual-input neural network, but it is used for depth Sliding sliding localization guidance.
All  operation processes are same of Sliding_21.hdf5, but different is this model has 13 labels 
Each label change represents a 5-pixel depth Sliding of the camera's view compared to the base image



## prerequisites
```
-Python 3.7
-Tensorflow 2.2.0
-numpy
-Keras 2.2.4
-OpenCV
This code has only been tested on Windows.
