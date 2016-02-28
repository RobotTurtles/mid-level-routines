########################################################################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Released under Apache open source license
########################################################################################################################
from Movement import Movement
import shlex

class DanceMarathon:
    '''
    Class for various Dance Routines
    '''

    def __init__(self, movement, logger):
        self.m = movement
        self.logger = logger
        self.turnAboutDegrees = 360
        self.hokiePokieTurnDistance = 100
        self.hokiePokieMoveDistance = 20
        self.nodDistance = 30
        self.shakeDistance = 30
        self.logger.info("Initialized Dance Routines")

    def processImage(self, img):
        #print 'NoOp for process Image in Dance Marathon'
        pass

    def dances(self, functionToCall):
        return {
            'rightHokiePokie':self.rightHokiePokie,
            'leftHockeyPokie':self.leftHokiePokie,
            'nod':self.nod,
            'shakeNo':self.shakeNo,
            'spinRight':self.spinRight,
            'spinLeft':self.spinLeft,
        }[functionToCall]

    def happyDance(self):
        self.logger.info("DanceRoutines: Happy Dance")
        self.m.turnDegrees(self.shakeDistance)
        self.m.turnDegrees(-self.shakeDistance)
        self.m.turnDegrees(self.shakeDistance)
        self.m.turnDegrees(-self.shakeDistance)

        # Wag Left Arm
        self.m.turnLeftArm(80)
        self.m.turnLeftArm(-80)
        self.m.turnLeftArm(80)
        self.m.turnLeftArm(-80)

    def sadDance(self):
        self.logger.info("DanceRoutines: Sad Dance")
        self.m.moveCM(self.nodDistance)
        self.m.moveCM(-self.nodDistance)
        self.m.moveCM(self.nodDistance)
        self.m.moveCM(-self.nodDistance)

        # Wag Left Arm
        self.m.turnRightArm(80)
        self.m.turnRightArm(-80)
        self.m.turnRightArm(80)
        self.m.turnRightArm(-80)


    def spinRight(self):
        self.logger.info("DanceRoutines: Spin Right")
        self.m.turnDegrees(self.turnAboutDegrees)

    def spinLeft(self):
        self.logger.info("DanceRoutines: Spin Left")
        self.m.turnDegrees(self.turnAboutDegrees)

    def nod(self):
        self.logger.info("DanceRoutines: Nod")
        self.m.moveCM(self.nodDistance)
        self.m.moveCM(-self.nodDistance)
        self.m.moveCM(self.nodDistance)
        self.m.moveCM(-self.nodDistance)

    def shakeNo(self):
        self.logger.info("DanceRoutines: Shake No")
        self.m.turnDegrees(self.shakeDistance)
        self.m.turnDegrees(-self.shakeDistance)
        self.m.turnDegrees(self.shakeDistance)
        self.m.turnDegrees(-self.shakeDistance)

    def leftHokiePokie(self):
        self.logger.info("DanceRoutines: Left Hokie Pokie")
        turnDistance = self.hokiePokieTurnDistance
        moveDistance = self.hokiePokieMoveDistance

        # Left Hand In
        self.m.turnLeftArm(turnDistance)

        # Left Hand Out
        self.m.turnLeftArm(-turnDistance)

        # Do the hokie Pokie (and spin yourself about
        self.m.turnDegrees(self.turnAboutDegrees)

        # That is what it is all about :)
        self.m.moveCM(moveDistance)
        self.m.moveCM(-moveDistance)

    def rightHokiePokie(self):
        self.logger.info("DanceRoutines: Right Hokie Pokie")
        turnDistance = self.hokiePokieTurnDistance
        moveDistance = self.hokiePokieMoveDistance

        # Right Hand In
        self.m.turnRightArm(turnDistance)

        # Right Hand Out
        self.m.turnRightArm(-turnDistance)

        # Do the hokie Pokie (and spin yourself about
        self.m.turnDegrees(self.turnAboutDegrees)

        # That is what it is all about :)
        self.m.moveCM(moveDistance)
        self.m.moveCM(-moveDistance)



    def executeDance(self, danceMoves):
        '''
        Executes stored danced routines
        :param danceMoves:
        :return:
        '''
        print("Entering Dance Execute using QRCode: "+danceMoves)

        self.logger.info("running dance moves: "+danceMoves);

        function = self.dances(danceMoves)

        print str(function)

        function()





