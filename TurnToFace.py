
################
# TurnToFace.py
# Has robot automatically turn to the last face it sees
####################

from Movement import Movement
from FaceRecognition import FaceRecognition
import time
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

directory = '/home/pi/logs'

if not os.path.exists(directory):
    os.makedirs(directory)
	
handler = logging.FileHandler(directory + '/TurtleThoughts.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler()

logger.info('Started Turn To Face')

m = Movement()
f = FaceRecognition(logger)
threshold = 5
targetWidth = 150


while(True):
	faceLocation = f.FindFace()
	
	if(faceLocation[2] == 0):
		faceLocation[2] = targetWidth
	
	if(faceLocation[0] != 0 and faceLocation[1] != 0):
		delta = faceLocation[0]-320
		
		print "delta:" + str(delta)
		
		# turn left
		if(delta > threshold):
			m.turnDegrees(-5)
			
		#turn right
		if(delta < -threshold):
			m.turnDegrees(5)
		
		# target is within threshold, move closer/farther
		if(delta <= threshold and delta > -threshold):
			
			print "Inside Threshold"	
			m.turnSpeed(0)
			
			if(faceLocation[2] < targetWidth-2):
				print "Moving Forward"
				m.moveCM(2)
			
			if(faceLocation[2] > targetWidth+2):
				print "Moving Backward"
				m.moveCM(-2)

			if(faceLocation[2] > targetWidth-2 and faceLocation[2] < targetWidth+2):
				print "Staying Still"
				m.moveCM(0)
			
