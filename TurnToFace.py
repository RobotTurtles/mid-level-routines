
################
# TurnToFace.py
# Has robot automatically turn to the last face it sees
####################

from Movement import Movement
from FaceRecognition import FaceRecognition
import time

m = Movement()
f = FaceRecognition()
threshold = 10

while(true):
	faceLocation = f.FindFace()
	
	if(faceLocation[0] != 0 && faceLocation[1] != 0):
		delta = 240 - faceLocation[0]
		
		if(abs(delta) > threshold):
			m.turnDegrees(-delta)
			
	time.sleep(2)