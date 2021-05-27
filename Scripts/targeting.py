#   Author github.com/DanyPalma    #
# Forked by github.com/cfrankovich #

import sys
import cv2
import numpy as np
from datetime import datetime
from colorama import Fore, Style

trained_data = cv2.CascadeClassifier('TargetingSystem/Sources/haarcascade_frontalface_default.xml')
tCoord = (300,200)
capture = cv2.VideoCapture(0)
showHSV = False 
showCAM = False


# Helper function aPos #
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


# Arguments #
args = sys.argv
args.pop(0)
log = open('TargetingSystem/Sources/coordlog.txt', 'a')
log.truncate(0)
log.write(f'> Coord Log from {datetime.now()}\n\n')
for arg in args:
	arg = arg.lower()
	if arg == 'all':
		showHSV = True
		showCAM = True
		break	
	elif arg == 'help':
		print(f'\n{Fore.GREEN}>{Fore.CYAN}> {Fore.RESET}{Style.BRIGHT}https://github.com/DanyPalma/TargetingSystem{Style.NORMAL} {Fore.CYAN}<{Fore.GREEN}<\n')
		exit(0)
	elif arg == 'hsv':
		showHSV = True
	elif arg == 'cam':
		showCAM = True
	else:
		print(f'{Fore.RED}\nUnreconized option "{Style.BRIGHT}{arg}{Style.NORMAL}". Please run with the "{Style.BRIGHT}help{Style.NORMAL}" option for more.\n')
		exit(1)
if len(args) == 0:
	showHSV = True
	showCAM = True


# Main Loop #
# Think of some way to exit this loop. While trues are scary - gui?  # 
while True:
	ret, frame = capture.read()
	greyscale_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 
	HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL)

	lowerV = np.array([80, 230, 100])
	upperV = np.array([255, 255, 255])

	maskVid = cv2.inRange(HSV, lowerV, upperV)

	width  = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

	coord = aPos(maskVid)
	log.write(f'{coord}\n')

	cv2.imshow('FINAL DISPLAY', maskVid)

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

	# this doesnt even work to break the loop #
	if cv2.waitKey(1) == 27:
		break

capture.release()
cv2.destroyAllWindows()
