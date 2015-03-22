from TurtleCommands import Forward, Left, Right, Reverse

__author__ = 'Alex'

import cv2
from ProcessFlashCard import ProcessFlashCard


class RobotMenu:

    def __init__(self, logger):
        self.logger = logger
        self.webcam = cv2.VideoCapture(0)
        self.flashCards = ProcessFlashCard(logger)
        self.savedCommands = list()


    def execute(self):


        while(True):

            mode = self.getMenuOption()

            # Find Face
            if(mode == 0):
                pass

            # Execute Stored Program
            if(mode == 1):
                for command in self.savedCommands:
                    command.execute()

            # Save a new Program
            if(mode == 2):
                self.addCommands()



    def addCommands(self):

        cmdBuffer = list()

        while(True):
            self.webcam.read()
            self.webcam.read()
            self.webcam.read()
            self.webcam.read()
            ret, img = self.webcam.read()

            nextCommand = self.flashCards.get_move_choice(img)

            if(nextCommand == 0):
                self.savedCommands = cmdBuffer
                return

            # Abort this save process
            if(nextCommand == 5):
                cmdBuffer = None
                return

            # Forward
            if(nextCommand == 1):
                cmdBuffer.append(Forward())

            # Reverse
            if(nextCommand == 2):
                cmdBuffer.append(Reverse())

            # Left
            if(nextCommand == 3):
                cmdBuffer.append(Left())

            # Right
            if(nextCommand == 4):
                cmdBuffer.append(Right())


    def getMenuOption(self):
        self.webcam.read()
        self.webcam.read()
        self.webcam.read()
        self.webcam.read()
        ret, img = self.webcam.read()

        return self.flashCards.get_menu_choice(img)