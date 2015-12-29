########################################################################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Released under Apache open source license
########################################################################################################################
import datetime

import cv2


class FaceRecognition:
    def __init__(self, logger, videoStream):
        """

        :type self: object
        """
        self.logger = logger
        self.frontalface = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
        self.webcam = videoStream
        self.Cface = [0, 0, 0]

    def FindFace(self, filename='lastFaceFound.jpg', capturePath='captures', missedPath='misses'):
        '''
        Finds a face in the current video frame
        :param filename:
        :param capturePath:
        :param missedPath:
        :return:
        '''
        self.Cface = [0, 0, 0]

        moreFramesToRead = True

        # Clear any frames in the buffer
        while(moreFramesToRead):
            ret, new_img = self.webcam.read()
            if(ret == False):
                break
            img = new_img
            moreFramesToRead = False

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = self.frontalface.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            self.Cface = [(w / 2 + x), (h / 2 + y), w]

            if (x != 0 and y != 0):
                filename = capturePath + '/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")
                self.logger.info(filename)
                cv2.imwrite(filename, img)

        if (self.Cface[2] == 0):
            filename = missedPath + '/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")
            self.logger.info(filename)
            cv2.imwrite(filename, img)

        self.logger.info(str(self.Cface[0]) + "," + str(self.Cface[1]) + ",width:" + str(self.Cface[2]))
        return self.Cface
