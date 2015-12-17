from Movement import Movement
import shlex

class DanceRoutines:
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


    def dances(self, functionToCall):
        return {
            'rightHokiePokie':self.rightHokiePokie,
            'leftHockeyPokie':self.leftHokiePokie,
            'nod':self.nod,
            'shakeNo':self.shakeNo,
            'spinRight':self.spinRight,
            'spinLeft':self.spinLeft,
        }[functionToCall]

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

        # Left Hand In
        self.m.turnLeftArm(turnDistance)

        # Left Hand Out
        self.m.turnLeftArm(-turnDistance)

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




