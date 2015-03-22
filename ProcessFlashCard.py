__author__ = 'Alex'

import cv2
import numpy as np
from matplotlib import pyplot as plt


class ProcessFlashCard:
    def __init__(self, logger):
        """
        Constructor
        :param logger:
        :return:
        """
        self.logger = logger
        self.load_flash_cards()
        self.threshold = 0.1
        self.MIN_MATCH_COUNT = 20

    def load_flash_cards(self):
        """
        Load all current templates
        :return:
        """
        self.menuTemplates = dict()
        self.menuTemplates = {1:'FlashCards/execute.jpg',2:'FlashCards/record.jpg',3:'FlashCards/FindFace.jpg'}

        self.moveTemplates = dict()
        self.moveTemplates = {0:'FlashCards/save.jpg', 1:'FlashCards/forward.jpg',2:'FlashCards/reverse.jpg',3:'FlashCards/left.jpg',4:'FlashCards/right.jpg', 5:'FlashCards/abort.jpg'}


    def get_menu_choice(self,img):
        return self.process_image(img, self.menuTemplates)

    def get_move_choice(self,img):
        return self.process_image(img, self.moveTemplates)

    def process_image(self, img, templates):
        """
        Process an individual image
        :param img:
        :return: image found (-1: no match, 1: record, 2: forward, 3: left, 4: right, 5: save, 6: execute)
        """

        method = eval('cv2.TM_SQDIFF_NORMED')

        searchResults = -1

        sift = cv2.SIFT()

        kpInput, kpDesc = sift.detectAndCompute(img, None)

        bestMatchCount = 0
        bestMatchIndex = -1

        for i in templates:
            target = cv2.imread(templates[i],0)

            # If template doesn't exist, skip to next one
            if(target is None):
                continue

            # Get Key Points and Descriptors with SIFT
            kpTarget, descTarget = sift.detectAndCompute(target, None)

            FLANN_INDEX_KDTREE = 0
            index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
            search_params = dict(checks = 50)

            flann = cv2.FlannBasedMatcher(index_params, search_params)

            matches = flann.knnMatch(descTarget,kpDesc,k=2)


            # store all the good matches as per Lowe's ratio test.
            good = []
            for m,n in matches:
                if m.distance < 0.7*n.distance:
                    good.append(m)

            if len(good)>bestMatchCount:
                bestMatchCount = len(good)
                bestMatchIndex = i

        if bestMatchCount > self.MIN_MATCH_COUNT:
            return bestMatchIndex
        else:
            return -1