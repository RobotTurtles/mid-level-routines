
################
# TurnToFace.py
# Has robot automatically turn to the last face it sees
####################

from Movement import Movement
from FaceRecognition import FaceRecognition
import time

m = Movement()
f = FaceRecognition()
threshold = 5
targetWidth = 10

while(True):
	faceLocation = f.FindFace()
	
	if(faceLocation[2] == 0):
		faceLocation[2] = targetWidth
	
	if(faceLocation[0] != 0 and faceLocation[1] != 0):
		delta = faceLocation[0]-320
		
		print "delta:" + str(delta)
		
		# turn left
		if(delta > threshold):
			m.turnSpeed(delta/10)
			
		#turn right
		if(delta < -threshold):
			m.turnSpeed(delta/10)
		
		# target is within threshold, move closer/farther
		if(delta <= threshold and delta > -threshold):
			m.turnSpeed(0)
			
			if(faceLocation[2] < targetWidth-2):
				m.moveCM(2)
			
			if(faceLocation[2] > targetWidth+2):
				m.moveCM(-2)

			if(faceLocation[2] > targetWidth-2 and faceLocation[2] < targetWidth+2):
				m.moveCM(0)
			
