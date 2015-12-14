from PIL import Image
import cv2
import zbarlight

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

        timeout = 100

        while(timeout>0):
            ret, img = self.webcam.read()

                cv2.imwrite('/tmp/lastImage.jpg', img)
                image = Image.open('/tmp/lastImage.jpg')
                image.load()
                codes = zbarlight.scan_codes('qrcode', image)
            
            if codes != None:
                return codes

        return None
