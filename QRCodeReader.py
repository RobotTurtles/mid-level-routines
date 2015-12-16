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
        self.webcam.set(10,0.01)
        self.logger = logger
        self.lastCodeRead = None


    def lookForCode(self):
        '''
        :return: empty string if nothing found, value of qr code if found
        '''
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
                return None

        self.lastCodeRead = None
        return None
