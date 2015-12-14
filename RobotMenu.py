from TurtleCommands import Forward, Left, Right, Reverse

__author__ = 'Alex'

import cv2
import datetime
from QRCodeReader import QRCodeReader

class RobotMenu:

    def __init__(self, logger, movement):
        self.logger = logger
        self.webcam = cv2.VideoCapture(0)
        self.savedCommands = list()
        self.capturePath='captures'
        self.missedPath='misses'
        self.movement = movement
        self.qr = QRCodeReader(cv2.VideoCapture(0))


    def execute(self):


        while(True):

            self.logger.info('Getting Menu Option:')
            mode = self.qr.lookForCode()

            # Find Face
            if(mode == 'findface'):
                self.logger.info('Executing Find Face')

                pass

            # Execute Stored Program
            if(mode == 'execute'):
                self.logger.info('Executing Stored Program')

                self.logger.info('Total Steps: '+ str(len(self.savedCommands)))
                for command in self.savedCommands:
                    self.logger.info('Executing: '+command.name)
                    command.execute()
                self.logger.info('Execution Complete')

            # Save a new Program
            if(mode == 'save'):
                self.logger.info('Saving a new Program')
                self.addCommands()




    def addCommands(self):
        self.logger.info('adding commands')

        cmdBuffer = list()

        while(True):
            filename = self.capturePath + '/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")

            nextCommand = self.qr.lookForCode()

            if(nextCommand == 'save'):
                self.logger.info('Found Save Command 0, exiting')
                self.savedCommands = cmdBuffer
                return

            # Abort this save process
            if(nextCommand == 'abort'):
                self.logger.info('Found Abort Command 5, exiting')
                cmdBuffer = None
                return

            # Forward
            if(nextCommand == 'forward'):
                self.logger.info('Found Forward Command 1')
                cmdBuffer.append(Forward(self.movement))
                continue

            # Reverse
            if(nextCommand == 'reverse'):
                self.logger.info('Found Reverse Command 2')
                cmdBuffer.append(Reverse(self.movement))
                continue

            # Left
            if(nextCommand == 'left'):
                self.logger.info('Found Left Command 3')
                cmdBuffer.append(Left(self.movement))
                continue

            # Right
            if(nextCommand == 'right'):
                self.logger.info('Found Right Command 4')
                cmdBuffer.append(Right(self.movement))
                continue

            self.logger.info('No Match found')

    def getMenuOption(self):


        returnOption = self.flashCards.get_menu_choice(img)

        if(returnOption == -1):
            self.logger.info('No Match found')
            filename = self.missedPath + '/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")
            cv2.imwrite(filename, img)

        return returnOption