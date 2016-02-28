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
import sys
import ConnectToServer
import socket


sys.path.append('/home/pi/mid-level-routines')

from QRCodeReader import QRCodeReader
from RobotMenu import RobotMenu
__author__ = 'Alex'


class ReadQRCodeAndReport:

    def __init__(self, logger):

        # Input Parameters
        self.logger = logger

        # Created Parameters
        self.webcam = cv2.VideoCapture(0)
        self.webcam.set(10,0.01) # Set brightness
        self.qrReader = QRCodeReader(self.webcam, logger)
        self.lastQRCode = None

    def execute(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets

        turtle_name = socket.gethostname()
        ip_address = s.getsockname()[0]
        turtle_id = '3'

        while(True):
            ret, img = self.webcam.read()

            # get QR Code if it exists
            qrCode = self.qrReader.readImage(img)

            if(qrCode != None):
                print(qrCode)
                if(qrCode.startswith('connect:')):
                    arguments = qrCode[8:].split('&')
                    turtle_id = arguments[0].split('=')[1]
                    print('Turtle_id:'+turtle_id)
                    ConnectToServer.PingServer(turtle_name, ip_address, turtle_id)

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    c = ReadQRCodeAndReport(logger)
    c.execute()