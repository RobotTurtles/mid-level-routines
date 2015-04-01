from TurtleCommands import Forward, Left, Right, Reverse

__author__ = 'Alex'

import cv2
import datetime
from ProcessFlashCard import ProcessFlashCard


class RobotMenu:

    def __init__(self, logger, movement):
        self.logger = logger
        self.webcam = cv2.VideoCapture(0)
        self.flashCards = ProcessFlashCard(logger)
        self.savedCommands = list()
        self.capturePath='captures'
        self.missedPath='misses'
        self.movement = movement


    def execute(self):


        while(True):

            self.logger.info('Getting Menu Option:')
            mode = self.getMenuOption()

            # Find Face
            if(mode == 0):
                self.logger.info('Executing Find Face')

                pass

            # Execute Stored Program
            if(mode == 1):
                self.logger.info('Executing Stored Program')

                self.logger.info('Total Steps: '+ str(len(self.savedCommands)))
                for command in self.savedCommands:
                    self.logger.info('Executing: '+command.name)
                    command.execute()
                self.logger.info('Execution Complete')

            # Save a new Program
            if(mode == 2):
                self.logger.info('Saving a new Program')
                self.addCommands()




    def addCommands(self):
        self.logger.info('adding commands')

        cmdBuffer = list()

        while(True):
            filename = self.capturePath + '/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")

            self.webcam.read()
            self.webcam.read()
            self.webcam.read()
            self.webcam.read()
            ret, img = self.webcam.read()

            nextCommand = self.flashCards.get_move_choice(img)

            if(nextCommand == 0):
                self.logger.info('Found Save Command 0, exiting')
                filename = self.capturePath + '/save_' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")
                cv2.imwrite(filename, img)
                self.savedCommands = cmdBuffer
                return

            # Abort this save process
            if(nextCommand == 5):
                self.logger.info('Found Abort Command 5, exiting')
                filename = self.capturePath + '/abort_' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")
                cv2.imwrite(filename, img)
                cmdBuffer = None
                return

            # Forward
            if(nextCommand == 1):
                self.logger.info('Found Forward Command 1')
                filename = self.capturePath + '/forward_' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")
                cv2.imwrite(filename, img)
                cmdBuffer.append(Forward(self.movement))
                continue

            # Reverse
            if(nextCommand == 2):
                self.logger.info('Found Reverse Command 2')
                filename = self.capturePath + '/reverse_' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")
                cv2.imwrite(filename, img)
                cmdBuffer.append(Reverse(self.movement))
                continue

            # Left
            if(nextCommand == 3):
                self.logger.info('Found Left Command 3')
                filename = self.capturePath + '/left_' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")
                cv2.imwrite(filename, img)
                cmdBuffer.append(Left(self.movement))
                continue

            # Right
            if(nextCommand == 4):
                self.logger.info('Found Right Command 4')
                filename = self.capturePath + '/right_' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")
                cv2.imwrite(filename, img)
                cmdBuffer.append(Right(self.movement))
                continue

            self.logger.info('No Match found')
            filename = self.missedPath + '/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")
            cv2.imwrite(filename, img)


    def getMenuOption(self):
        self.webcam.read()
        self.webcam.read()
        self.webcam.read()
        self.webcam.read()
        ret, img = self.webcam.read()

        returnOption = self.flashCards.get_menu_choice(img)

        if(returnOption == -1):
            self.logger.info('No Match found')
            filename = self.missedPath + '/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")
            cv2.imwrite(filename, img)

        return returnOption