__author__ = 'Alex'

import cv2


class ProcessFlashCard:
    def __init__(self, logger):
        """
        Constructor
        :param logger:
        :return:
        """
        self.logger = logger


    def load_flash_cards(self):
        """
        Load all current templates
        :return:
        """
        self.templates[0] = cv2.imread('FlashCards/save.png')

    def process_image(self, img):
        """
        Process an individual image
        :param img:
        :return: image found (-1: no match, 1: record, 2: forward, 3: left, 4: right, 5: save, 6: execute)
        """

        method = eval('cv2.TM_CCOEFF')

        for template in self.templates:
            res = cv2.matchTemplate(img,template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)



        return -1