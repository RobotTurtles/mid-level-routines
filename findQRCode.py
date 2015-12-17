from QRCodeReader import QRCodeReader
import cv2

qr = QRCodeReader(cv2.VideoCapture(0), 'test')

i = 0
old_result = ''
while(i <= 10):
    result = qr.lookForCode()
    if result != None:
        print(result)
    if result != old_result:
        i = i + 1
        old_result = result
