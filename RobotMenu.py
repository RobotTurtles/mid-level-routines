########################################################################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Released under Apache open source license
########################################################################################################################

__author__ = 'Alex'

from subprocess import call
from Apps.DanceMarathon import DanceMarathon
from Apps.Basics import Basics
from NetworkManager import NetworkManager
from UpdateManager import UpdateManager
import Utilities.TurtleInfo
import Utilities.ConnectToServer
import Utilities.ConfigFileManager
import sys

class RobotMenu:

    def __init__(self, logger, movement, config):
        self.logger = logger
        self.savedCommands = list()
        self.capturePath='captures'
        self.missedPath='misses'
        self.movement = movement
        self.currentApp = 'dance'
        self.config = config

        # App Initialization, will be moved later
        self.dance = DanceMarathon(self.movement, self.logger)
        self.basics = Basics(self.movement, self.logger)
        self.defaultRoutine = self.dance.processImage
        self.currentAppMethod = self.dance.executeDance

        self.applications = {
            'dance':self.dance.processImage,
            'basics':self.basics.execute
        }

    def runMethod(self, value, args):
        keyWord = str(value)

        if(keyWord == self.currentApp):
            self.currentAppMethod(args)
            return

        if(keyWord in self.applications):
            try:
                self.applications[keyWord](args)
            except:
                print("Unable to launch: "+str(self.applications[keyWord]))
                pass
        else:
            method_name = 'visit_' + keyWord

            print("going to method: "+method_name)

            method = getattr(self, method_name)

            try:
                method(args)
                # If Default System Function
            except AttributeError:
                print("Failed to find method: "+method)
                targetAppExecutable = self.application(keyWord)
                self.currentApp = keyWord
                self.defaultRoutine = targetAppExecutable
                return targetAppExecutable


    def visit_connect(self, args):
        networkDetails = args.split('&')

        turtleId = str(networkDetails[0].split('=')[1])
        networkName = str(networkDetails[1].split('=')[1])
        networkPassword = str(networkDetails[2].split('=')[1])

        self.logger.info('Connecting to Network:'+ networkName)
        self.logger.info('Password: ' + networkPassword)

        print("Attempting to connect to: "+networkName+" , password: "+str(networkPassword))

        try:
            result = NetworkManager().find_and_connect('default',networkName,networkPassword)
        except:
            e = sys.exc_info()[0]
            print("Error: "+ str(e))
            result = 0

        if(result == 1):
            self.logger.info('Successfully Connected!')
            print("Successfully Connected!")
            self.dance.happyDance()
        else:
            self.logger.info('Failed to Connect =(')
            print("Failed to connect!")
            self.dance.sadDance()

        # Ping Home
        turtleName = Utilities.TurtleInfo.GetTurtleName()
        turtleIP = Utilities.TurtleInfo.GetCurrentAddress()

        self.config.WriteParams(turtleName, turtleId, turtleIP)



    def visit_ping(self, args):
        print("In Visit Ping")
        turtleName, turtleID, turtleIP = self.config.ReadParams()

        Utilities.ConnectToServer.PingServer(turtleName,turtleIP,turtleID)
        pass

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

        print("Processing: "+qrCode_string)

        if(qrCode_string == None):
            return None

        # parse qrcode w/ arguments
        commandList = qrCode_string.split(':')

        if(commandList == None or len(commandList) == 0):
            print("No Commands Found")
            return None

        option = commandList[0]

        print("Option is: "+str(option))

        if(len(commandList) == 2):
            arguments = commandList[1]
            print('Found Arguments: '+str(arguments))
        else:
            arguments = None
            print('Found no Arguments')

        # See if qrCode is part of known options
        self.runMethod(option, arguments)

        # process QR Code

        return returnVal
