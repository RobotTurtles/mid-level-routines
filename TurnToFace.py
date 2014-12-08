
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

while(True):
	faceLocation = f.FindFace()
	
	if(faceLocation[0] != 0 and faceLocation[1] != 0):
		delta = 240 - faceLocation[0]
		
		print "delta:" + str(delta)
		
		# turn left
		if(delta > threshold):
			m.turnDegrees(delta)
			
		#turn right
		if(delta < -threshold):
			m.turnDegrees(delta)
		
		
	time.sleep(2)