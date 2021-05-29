 # github.com/DanyPalma #
# github.com/cfrankovich #
import cv2
import tkinter
from random import randrange

# Helper Functions
def exitCallBack():
    cv2.destroyAllWindows()

# boolean var to keep track of loop
running = True
#loading pre trained face data from opencv
trained_data = cv2.CascadeClassifier('Sources/amorgocascade.xml')
#grabbing webcam 
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while running:
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
    
    if cv2.waitKey(33) == ord('q'):
        cv2.destroyAllWindows()
        running = False

