# github.com/cfrankovich #

import sys
import cv2
import numpy as np
from datetime import datetime
from colorama import Fore, Style

tCoord = (300,200)
capture = cv2.VideoCapture(0)
showHSV = False 
showCAM = False

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

args = sys.argv
args.pop(0)
log = open('coordlog.txt', 'a')
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

while(True):
	ret, frame = capture.read()
 
	HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL)
	lowerV = np.array([80, 230, 100])
	upperV = np.array([255, 255, 255])
	maskVid = cv2.inRange(HSV, lowerV, upperV)
 
	if showHSV is True:
		cv2.imshow('video HSV', HSV)
	if showCAM is True:
		cv2.imshow('video original', frame)

	width  = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

	coord = aPos(maskVid)
	# log.write(f'{coord}\n')

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
