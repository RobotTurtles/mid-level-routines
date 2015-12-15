from PIL import Image
import cv2
import zbarlight
import sys

class QRCodeReader:
    def __init__(self, webcam):
        '''
        Constructor
        :return:
        '''
        self.webcam = webcam
        self.webcam.set(10,0.01)



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
            return codes

        return None
