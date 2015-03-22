
################
# TurnToFace.py
# Has robot automatically turn to, and move towards/away from the last face it sees
####################

from Movement import Movement
from SimMovement import SimMovement
from FaceRecognition import FaceRecognition
import time
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#directory = '/home/pi/logs'
directory = '.'

if not os.path.exists(directory):
    os.makedirs(directory)
	
handler = logging.FileHandler(directory + '/TurtleThoughts.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info('Started Turn To Face')

# m = Movement(logger)
m = SimMovement(logger)
f = FaceRecognition(logger)
center = 666
turnThreshold = 5

moveThreshold = 30
targetWidth = 280

while(True):
	faceLocation = f.FindFace()
	
	if(faceLocation[2] == 0):
		faceLocation[2] = targetWidth
	
	if(faceLocation[0] != 0 and faceLocation[1] != 0):
		width = faceLocation[2]
		delta = faceLocation[0]-center
		
		logger.info("Face is at %d, delta from center is %d:" % (faceLocation[0], delta))
		
		# turn left
		if(delta > turnThreshold + (width/4)):
                        logger.info("Turning left a bit")
			m.turnDegrees(10)
			
		#turn right
		if(delta < -turnThreshold - (width/4)):
                        logger.info("Turning right a bit")
			m.turnDegrees(-10)
		
		# target is within turnThreshold, move closer/farther
		if(delta <= (turnThreshold+(width/2)) and delta >= (-turnThreshold-(width/2))):
			
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
			
