###############################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Description:
#   Utility method to read QR Codes for debugging purposes
#
###############################################################################

import cv2
import logging
import os
import sys

sys.path.append('/home/pi/mid-level-routines')

from QRCodeReader import QRCodeReader
from RobotMenu import RobotMenu
__author__ = 'Alex'


class ReadQRCodes:

    def __init__(self, logger):

        # Input Parameters
        self.logger = logger

        # Created Parameters
        self.webcam = cv2.VideoCapture(0)
        self.webcam.set(10,0.01) # Set brightness
        self.qrReader = QRCodeReader(self.webcam, logger)
        self.lastQRCode = None

    def execute(self):

        counter = 0

        while(True):
            ret, img = self.webcam.read()

            # get QR Code if it exists
            qrCode = self.qrReader.readImage(img)

            print(qrCode)

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    c = ReadQRCodes(logger)
    c.execute()
