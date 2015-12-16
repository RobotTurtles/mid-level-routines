################
# TurnToFace.py
# Has robot automatically turn to, and move towards/away from the last face it sees
####################

from Movement import Movement
from FaceRecognition import FaceRecognition
from QRCodeReader import QRCodeReader
from RobotMenu import RobotMenu
from DanceRoutines import DanceRoutines

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
qr = QRCodeReader(webcam, logger)
danceRoutines = DanceRoutines(m,logger)
menu = RobotMenu(logger, m,qr,danceRoutines)

center = 320
turnThreshold = 5

moveThreshold = 10
targetWidth = 160


def moveToFace():
    while (True):
        qrCode = qr.lookForCode()

        if(qrCode != None):
            return qrCode

        faceLocation = f.FindFace()

        if (faceLocation[2] == 0):
            faceLocation[2] = targetWidth

        if (faceLocation[0] != 0 and faceLocation[1] != 0):
            width = faceLocation[2]
            delta = faceLocation[0] - center

            logger.info("Face Delta from center is:" + str(delta))

            # turn left
            if (delta > turnThreshold + (width / 2)):
                m.turnDegrees(10)

                # turn right
            if (delta < -turnThreshold - (width / 2)):
                m.turnDegrees(-10)

            # target is within turnThreshold, move closer/farther
            if (delta <= (turnThreshold + (width / 2)) and delta >= (-turnThreshold - (width / 2))):

                logger.info('Movement Width is:' + str(width))

                logger.info("Inside Turn Threshold")
                m.turnSpeed(0)

                if (width < targetWidth - moveThreshold):
                    logger.info("Moving Forward")
                    m.moveCM(8)

                if (width > targetWidth + moveThreshold):
                    logger.info("Moving Backward")
                    m.moveCM(-8)

                if (width > targetWidth - moveThreshold and width < targetWidth + moveThreshold):
                    logger.info("Staying Still")
                    m.moveCM(0)


while(True):
    qrCode = moveToFace()
    time.sleep(5)
    print str(qrCode) 
    menu.execute()
			
