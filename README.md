# UniShot
UniShot is a visual localization framework based on the "comparison neural network" architecture.
" It can be used by an eye-in-hand robot arm or a hand-held camera for precision positioning guidance.
Take a global photo of the scene at its center for the baseline.During the operation,
UniShot will predict the relative position of the camera based on the view captured by the camera.
There are Sliding_21.hdf5 model, Depth_13.hdf5, and two identification programs available.
## How To Use
Sliding_21.hdf5 modle is a dual input neural network for sliding positioning guidance need to be 
loaded in unishot_cam_SLIDING.py ,
you need to take a global photo of the scene at its center for the baseline in advance as basic image ,
then captured the photo by the camera as compare images, 
During the operation,
UniShot will automatically compare the relative sliding of the two images and give the predicted relative sliding value,
(10,10) represents view of camera is at center of basic image,
per vaule offset represent camera sliding 10 pixels.  
 
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
