###############################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Description:
#   Utility method to read QR Codes for debugging purposes
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

        self.RobotMenu = RobotMenu(logger, movement)
        self.defaultRoutine = self.RobotMenu.defaultRoutine()
        self.lastQRCode = None

    def execute(self):

        counter = 0

        while(True):
            ret, img = self.webcam.read()

            # get QR Code if it exists
            qrCode = QRCodeReader.readImage(img)

            print(qrCode)