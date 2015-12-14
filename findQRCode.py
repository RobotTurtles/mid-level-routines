from QRCodeReader import QRCodeReader
import cv2

qr = QRCodeReader(cv2.VideoCapture(0))

i = 0
old_result = ''
while(i <= 10):
    result = qr.lookForCode()
    print(result)
    if result != old_result:
        i = i + 1
        old_result = result
