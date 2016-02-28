###############################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Description:
#   Main turtle execution
#
###############################################################################

import cv2
from QRCodeReader import QRCodeReader
from RobotMenu import RobotMenu
__author__ = 'Alex'


class CoreRobot:

    def __init__(self, logger, movement, config):

        # Input Parameters
        self.m = movement
        self.logger = logger
        self.config = config

        # Created Parameters
        self.webcam = cv2.VideoCapture(0)
        self.webcam.set(10,0.01) # Set brightness

        self.RobotMenu = RobotMenu(logger, movement,config)
        self.defaultRoutine = self.RobotMenu.defaultRoutine
        self.lastQRCode = None

        self.qrCodeReader = QRCodeReader(self.webcam, logger)

    def execute(self):

        counter = 0

        while(True):
            ret, img = self.webcam.read()

            # get QR Code if it exists
            qrCode = self.qrCodeReader.readImage(img)

            print(qrCode)

            if(qrCode == None or qrCode == self.lastQRCode):
                self.logger.debug('No QR Code Found')
                self.defaultRoutine(img)
                counter = counter + 1

                # Reset QR Code Counter
                if(counter>50):
                    self.lastQRCode = None
                    counter = 0
            else:
                counter = 0
                self.lastQRCode = qrCode
                self.logger.info('Detected QR Code: '+str(qrCode))

                try:
                    print("Attempting to process QR Code")
                    newDefault = self.RobotMenu.process(qrCode)
                    if(newDefault != None):
                        self.defaultRoutine = newDefault
                except:
                    self.logger.error('Problem processing: '+str(qrCode))


