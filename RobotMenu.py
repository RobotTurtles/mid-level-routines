from TurtleCommands import Forward, Left, Right, Reverse

__author__ = 'Alex'

import cv2
import datetime
from QRCodeReader import QRCodeReader

class RobotMenu:

    def __init__(self, logger, movement):
        self.logger = logger
        self.savedCommands = list()
        self.capturePath='captures'
        self.missedPath='misses'
        self.movement = movement
        self.qr = QRCodeReader(cv2.VideoCapture(0))


    def execute(self):


        self.logger.info('Getting Menu Option:')
        print 'Entering Menu'
        print 'Do a little dance'
        while(True):

            qrCodes = self.qr.lookForCode()

            if(qrCodes == None):
                continue

            mode = qrCodes[0]

            # Find Face
            if(mode == 'findface'):
                self.logger.info('Executing Find Face')
                print 'Find Face'
                return

            # Execute Stored Program
            if(mode == 'execute'):
                self.logger.info('Executing Stored Program')
                print 'Execute'
                self.logger.info('Total Steps: '+ str(len(self.savedCommands)))
                for command in self.savedCommands:
                    self.logger.info('Executing: '+command.name)
                    command.execute()
                self.logger.info('Execution Complete')
                continue

            # Save a new Program
            if(mode == 'save'):
                self.logger.info('Saving a new Program')
                print 'save'
                self.addCommands()
                continue

            # No menu found, report QR code found
            self.logger.info('Found '+mode)
            print 'Found ' + str(mode)



    def addCommands(self):
        self.logger.info('adding commands')

        cmdBuffer = list()

        while(True):
            filename = self.capturePath + '/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.jpg")

            qrCodes = self.qr.lookForCode()

            if(qrCodes == None):
                continue

            nextCommand = qrCodes[0]

            if(nextCommand == 'save'):
                self.logger.info('Found Save Command 0, exiting')
                self.savedCommands = cmdBuffer
                print 'save'
                return

            # Abort this save process
            if(nextCommand == 'abort'):
                self.logger.info('Found Abort Command 5, exiting')
                print 'abort'
                cmdBuffer = None
                return

            # Forward
            if(nextCommand == 'forward'):
                self.logger.info('Found Forward Command 1')
                cmdBuffer.append(Forward(self.movement))
                print 'forward'
                continue

            # Reverse
            if(nextCommand == 'reverse'):
                self.logger.info('Found Reverse Command 2')
                cmdBuffer.append(Reverse(self.movement))
                print 'reverse'
                continue

            # Left
            if(nextCommand == 'left'):
                self.logger.info('Found Left Command 3')
                cmdBuffer.append(Left(self.movement))
                print 'left'
                continue

            # Right
            if(nextCommand == 'right'):
                self.logger.info('Found Right Command 4')
                cmdBuffer.append(Right(self.movement))
                print 'right'
                continue

            self.logger.info('No Match found')
            print 'No match found'
