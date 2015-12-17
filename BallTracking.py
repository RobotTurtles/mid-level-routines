# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2

class BallTracking:

    def __init__(self, logger, camera):
        '''
        Constructor
        :return:
        '''

        # HSV Color Space
        self.GREEN_LOWER = (29, 86, 6)
        self.GREEN_UPPER = (64, 255, 255)

        self.cam = camera

    def colorLimits(self, color):
        return {
            'green': {self.GREEN_LOWER, self.GREEN_UPPER}
        }[color]

    def ballCenter(self, targetColor):
        (grabbed, frame) = self.cam.read()

        if not grabbed:
            return

        [lower, upper] = self.colorLimits(targetColor)

        # resize the frame, blur it, and convert it to the HSV
        # color space
        frame = imutils.resize(frame, width=600)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # construct a mask for the color "green", then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        mask = cv2.inRange(hsv, lower, upper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]), int(radius*2))

            # only proceed if the radius meets a minimum size
            if radius > 10:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(frame, (int(x), int(y)), int(radius),
                    (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

        return center