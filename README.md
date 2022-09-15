# UniShot
UniShot is a visual localization framework based on the "comparison neural network" architecture.
" It can be used by an eye-in-hand robot arm or a hand-held camera for precision positioning guidance.
Take a global photo of the scene at its center for the baseline.During the operation,
UniShot will predict the relative position of the camera based on the view captured by the camera.
There are Sliding_21.hdf5 model, Depth_13.hdf5, and two identification programs available.
## How To Use
Sliding_21.hdf5 modle is a dual input neural network for sliding positioning guidance,
input one need to take a global photo of the scene at its center for the baseline,
input two is view captured by the camera, 
During the operation,
UniShot will automatically compare the relative sliding of the two inputs and give the predicted value
The pred
 
LIDING.py is a siding identification program, Needs to be used with  Sliding_21.hdf5 modle,
you could  set up your camera on eye-in-hand robot arm or just hold it,



## prerequisites
```
-Python 3.7
-Tensorflow 2.2.0
-numpy
-Keras 2.2.4
-OpenCV
This code has only been tested on Windows.
