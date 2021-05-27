import cv2
import numpy as np

trained_data = cv2.CascadeClassifier('C:\\Users\\danie\\Desktop\\haarcascade_frontalface_default.xml')



tCoord = (300,200)

def aPos(mask):
    xA = 0
    yA = 0
    count = 0
    resolution = 10
    for y in range(0, height, resolution):
        for x in range(0, width, resolution):
            if mask[y][x] == 255:
                xA += x
                yA += y
                count += 1

    if count > 0:
        xA = xA / count
        yA = yA / count
    return (int(xA), int(yA))

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(True):

    ret, frame = capture.read()
    greyscale_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

 
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL)

    lowerV = np.array([80, 230, 100])
    upperV = np.array([255, 255, 255])

    maskVid = cv2.inRange(HSV, lowerV, upperV)

    cv2.imshow('video HSV', HSV)
    cv2.imshow('video original', frame)

    width  = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))


    coord = aPos(maskVid)
    print(coord)



    if coord != (0, 0):
        tCoord = coord
        roundBoi = cv2.circle(maskVid, coord, 25, (255, 255, 0), 2)
        roundBoii = cv2.circle(frame, coord, 25, (255, 255 , 0), 2) 
    else:
        roundBoi = cv2.circle(maskVid, tCoord, 25, (255, 255, 0), 2)
        roundBoii = cv2.circle(frame, tCoord, 25, (255, 255 , 0), 2) 
    

    cv2.imshow('FINAL DISPLAY', maskVid)
    cv2.imshow('final bruh', frame) 

    #detect faces
    face_coordinates = trained_data.detectMultiScale(greyscale_frame)
    # x and y is the upper left corner, and w and h are the corresponding width
    # and length of the rectangle
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0, 255, 0),2)
        print("bruh")

    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()