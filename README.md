# TargetingSystem

### About
This is a short and quick targeting system written in Python using openCV.

### Installation / Running
Please install `opencv-contrib-python` using the command
```bash
$ python -m pip install opencv-contrib-python
```


After this is installed make sure you have a webcam. On GNU+Linux operating systems, you can check your video devices using
```bash
$ ls /dev/video*
```
With a windows machine you can check for webcams using the camera app and likewise on a Mac.


Once you have installed the module and made sure you have a webcam, you can run the following command to start the script.
```bash
$ python targeting.py
```
This should pop up three windows displaying the target window, an HSV window, and your normal webcam output.

### To-Do
  need to make it choose the brightest pixel always
  object recognition using cv::DetectionBasedTracker or
  face recognition using cv::face::BasicFaceRecognizer
