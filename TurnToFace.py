
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
		delta = faceLocation[0]-320
		
		print "delta:" + str(delta)
		
		# turn left
		if(delta > threshold):
			m.turnDegrees(delta/10)
			
		#turn right
		if(delta < -threshold):
			m.turnDegrees(delta/10)
		
		
	time.sleep(2)
