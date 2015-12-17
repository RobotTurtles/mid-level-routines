################
# TurnToFace.py
# Has robot automatically turn to, and move towards/away from the last face it sees
####################

from Movement import Movement
from FaceRecognition import FaceRecognition
from QRCodeReader import QRCodeReader
from RobotMenu import RobotMenu
from DanceRoutines import DanceRoutines
from BallTracking import BallTracking
from Follow import Follow

import time
import logging
import os
import cv2

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

webcam = cv2.VideoCapture(0)

m = Movement(logger)
f = FaceRecognition(logger, webcam)
ball = BallTracking(logger, webcam)
qr = QRCodeReader(webcam, logger)
danceRoutines = DanceRoutines(m,logger)
menu = RobotMenu(logger, m,qr)
followRoutine = Follow(logger, qr, m)

while(True):
    qrCode = followRoutine.moveToTarget(ball.ballCenter('green'))
    time.sleep(5)
    print str(qrCode) 
    menu.execute()
			
