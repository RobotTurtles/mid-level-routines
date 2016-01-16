########################################################################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Released under Apache open source license
########################################################################################################################

__author__ = 'Alex'

from subprocess import call
from Apps.DanceMarathon import DanceMarathon
from NetworkManager import NetworkManager
from UpdateManager import UpdateManager

class RobotMenu:

    def __init__(self, logger, movement):
        self.logger = logger
        self.savedCommands = list()
        self.capturePath='captures'
        self.missedPath='misses'
        self.movement = movement
        self.currentApp = 'DanceMarathon'

        # App Initialization, will be moved later
        self.dance = DanceMarathon(self.movement, self.logger)
        self.defaultRoutine = self.dance.processImage

    def application(self, functionToCall):
        return {
            'DanceMarathon':self.dance.processImage
        }[functionToCall]

    def runMethod(self, value, args):
        keyWord = str(value)

        if(keyWord == self.currentApp):
            self.currentAppMethod(args)
            return

        method_name = 'visit_' + keyWord
        method = getattr(self, method_name)

        try:
            method(args)
            # If Default System Function
        except AttributeError:
            targetAppExecutable = self.application(keyWord)
            self.currentApp = keyWord
            self.defaultRoutine = targetAppExecutable
            return targetAppExecutable


    def visit_runConnectToNetwork(self, args):
        networkDetails = args.split()
        networkName = str(networkDetails[0])
        networkProtocol = str(networkDetails[1])
        networkPassword = str(networkDetails[2])

        print 'Connecting to Network:'+ networkName
        print 'Protocol: ' + networkProtocol + ' Password: ' + networkPassword

        result = NetworkManager().find_and_connect('default',networkName,networkPassword)

        if(result == 1):
            self.dance.happyDance()
        else:
            self.dance.sadDance()


    def visit_updateCode(self, args):
        print 'Updating Code'
        UpdateManager().updateMidLevelRoutines()

    def visit_updatePackages(self, args):
        print 'Updating Packages'
        UpdateManager().updatePackages()
        UpdateManager().installPackages(args)

    def process(self, qrCode_string):
        '''
        Process a specific QR Code
        :param qrCode_string:
        :return: New Default Behavior (if applicable
        '''
        returnVal = None

        if(qrCode_string == None):
            return None

        # parse qrcode w/ arguments
        commandList = qrCode_string.split(':')

        if(commandList == None or len(commandList) == 0):
            return None

        option = commandList[0]

        if(len(commandList) == 2):
            arguments = commandList[1]
        else:
            arguments = None

        # See if qrCode is part of known options
        self.runMethod(option, arguments)

        # process QR Code

        return returnVal