########################################################################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Released under Apache open source license
########################################################################################################################
from PIL import Image
import cv2
import zbarlight
import sys

class QRCodeReader:
    def __init__(self, webcam, logger):
        '''
        Constructor
        :return:
        '''
        self.webcam = webcam
        self.logger = logger
        self.lastCodeRead = None
        self.count = 0


    def lookForCode(self):
        '''
        :return: empty string if nothing found, value of qr code if found
        '''
        self.webcam.set(10,0.01)
        moreFramesToRead = True

        # Clear any frames in the buffer
        while(moreFramesToRead):
            ret, new_img = self.webcam.read()
            if(ret == False):
                break
            img = new_img
            moreFramesToRead = False

        try:
            img
        except NameError:
            print 'Unable to find image'
            return None

        filename = '/tmp/lastQRImage.jpg'
        cv2.imwrite(filename, img)
        image = Image.open(filename)
        image.load()
        codes = zbarlight.scan_codes('qrcode', image)
            
        if codes != None:
            if(codes[0] != self.lastCodeRead):
                self.lastCodeRead = codes[0]
                return codes[0]
            else:
                self.count = self.count + 1
                return None

        if self.count > 100:
            self.count = 0
            self.lastCodeRead = None
        self.count = self.count + 1
        return None
