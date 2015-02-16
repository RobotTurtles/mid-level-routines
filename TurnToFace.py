
################
# TurnToFace.py
# Has robot automatically turn to, and move towards/away from the last face it sees
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

logger.addHandler(handler)

logger.info('Started Turn To Face')

m = Movement(logger)
f = FaceRecognition(logger)
center = 320
turnThreshold = 25

moveThreshold = 10
targetWidth = 180

while(True):
	faceLocation = f.FindFace()
	
	if(faceLocation[2] == 0):
		faceLocation[2] = targetWidth
	
	if(faceLocation[0] != 0 and faceLocation[1] != 0):
		delta = faceLocation[0]-center
		
		logger.info("Face Delta from center is:" + str(delta))
		
		# turn left
		if(delta > turnThreshold):
			m.turnDegrees(10)
			
		#turn right
		if(delta < -turnThreshold):
			m.turnDegrees(-10)
		
		# target is within turnThreshold, move closer/farther
		if(delta <= turnThreshold and delta > -turnThreshold):
			width = faceLocation[2]
			logger.info('Movement Width is:' + str(width))
			
			logger.info("Inside Turn Threshold")
			m.turnSpeed(0)
			
			if(width < targetWidth-moveThreshold):
				logger.info("Moving Forward")
				m.moveCM(8)
			
			if(width > targetWidth+moveThreshold):
				logger.info("Moving Backward")
				m.moveCM(-8)

			if(width > targetWidth-moveThreshold and width < targetWidth+moveThreshold):
				logger.info("Staying Still")
				m.moveCM(0)
			
