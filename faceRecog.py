import cv2
from random import randrange
#loading pre trained face data from opencv
trained_data = cv2.CascadeClassifier('C:\\Users\\danie\\Desktop\\haarcascade_frontalface_default.xml')

#grabbing webcam 
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    #reading webcam frames
    frame_read,frame = webcam.read()


# convert to black and white
    greyscale_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


# detect faces
    face_cordinates = trained_data.detectMultiScale(greyscale_frame)
    #x and y is the upper left corner coordinate and w and h are the corresponding width and height of the rectangle
    for (x,y,w,h) in face_cordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
# show image
    cv2.imshow("Final",frame)
    #agument 1 defines milliseconds
    cv2.waitKey(1) # keeps imaage in the screen