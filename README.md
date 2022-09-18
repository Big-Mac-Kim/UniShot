#UniShot
UniShot is a visual localization framework based on the "comparison neural network architecture. " It can be used by an eye-in-hand robot arm or a hand-held camera for precision positioning guidance. There are Sliding_21.hdf5 model, Depth_13.hdf5, and two identification programs available.
##How To Use
The Sliding_21.hdf5 model is a dual-input neural network for plane sliding localization, which needs to be loaded in unishot_cam_SLIDING.py. You need to take a global photo of the scene at its center in advance to be the baseline image. Then capture the photo by the camera as the testing image. UniShot will automatically compare the two pictures during the operation and predict the camera's sliding position. This model has 21 labels, each representing a 10-pixel plane sliding displacement. The coordinates (10,10) indicate that the camera's viewpoint is at the center of the baseline image.
The Depth_13.hdf5 model is also a dual-input neural network used for depth localization. All operation procedures are the same as Sliding_21.hdf5, but the difference is that this model only has 13 labels. Each label represents a 5-pixel frame difference in the camera's view compared to the baseline image.
'''
##prerequisites
-Python 3.7
-Tensorflow 2.2.0
-numpy
-Keras 2.2.4
-OpenCV
This code has only been tested on Windows.

