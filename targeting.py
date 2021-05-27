import cv2
import numpy as np


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

capture = cv2.VideoCapture(0)

while(True):

    ret, frame = capture.read()
 
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
    else:
        roundBoi = cv2.circle(maskVid, tCoord, 25, (255, 0, 0), 2)

    cv2.imshow('FINAL DISPLAY', maskVid)

    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()