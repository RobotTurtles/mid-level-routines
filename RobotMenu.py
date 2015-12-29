########################################################################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Released under Apache open source license
########################################################################################################################

__author__ = 'Alex'


class RobotMenu:

    def __init__(self, logger, movement):
        self.logger = logger
        self.savedCommands = list()
        self.capturePath='captures'
        self.missedPath='misses'
        self.movement = movement

    def process(self, qrCode):
        '''
        Process a specific QR Code
        :param qrCode:
        :return: New Default Behavior (if applicable
        '''
        returnVal = None

        if(qrCode == None):
            return None

        # parse qrcode w/ arguments

        # See if qrCode is part of known options

        # process QR Code

        return returnVal