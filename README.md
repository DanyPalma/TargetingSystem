# TargetingSystem

### About
This is a short and quick targeting system written in Python using openCV.

### Installation / Running
Please install `opencv-contrib-python` using the command
```bash
$ python -m pip install opencv-contrib-python
```
You may need to install colorama too
```bash
$ python -m pip install colorama
```

After this is installed make sure you have a webcam. On GNU+Linux operating systems, you can check your video devices using
```bash
$ ls /dev/video*
```
With a windows machine you can check for webcams using the camera app and likewise on a Mac.

Now you can simply run the file with the [options](#options) you want to have.
```bash
$ python targeting.py <options>
```

### Options
There are only a few options but I'll cover them one by one. If you don't put any arguments it is the same as putting [all](#all).

#### help
This just prints out the repo link so that you can reference these docs whenever you wish
```bash
$ python targeting.py help
```

#### all
This is the option if you would like to display all monitors of the webcam. The HSV, real-time footage, and the target.
```bash
$ python targeting.py all
```

#### hsv & cam
Both of these are the same essentially. If you wish to display the HSV footage, put `hsv` in. If you would like to see the camera then put the `cam` option. If you put both options like this
```bash
$ python targeting.py hsv cam
```
This is the same as running [all](#all)

Of course you can use each option in any order you wish. 

### Demo
![Demo GIF](https://i.imgur.com/LpSVKcJ.gif)

### To-Do
  need to make it choose the brightest pixel always
  object recognition using cv::DetectionBasedTracker or
  face recognition using cv::face::BasicFaceRecognizer
