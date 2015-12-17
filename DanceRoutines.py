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
        self.hokiePokieTurnDistance = 200
        self.hokiePokieMoveDistance = 100
        self.nodDistance = 30
        self.shakeDistance = 30
        self.logger.info("Initialized Dance Routines")


    def dances(self, com):
        return {
            'rightHokiepokie':self.rightHokiePokie,
            'leftHokiepokie':self.leftHokiePokie,
            'nod':self.nod,
            'shakeNo':self.shakeNo,
            'spinRight':self.spinRight,
            'spinLeft':self.spinLeft,
        }[com]

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
        Must be a series of commands in the form of <motion> <value>
        Example Commands that can be used are:
            moveCM 20
            moveCM -20
            turnDegrees 20
            turnDegrees -20
            left 20
            right 20
        :param danceMoves:
        :return:
        '''
        my_splitter = shlex.shlex(danceMoves)
        my_splitter.whitespace += ','
        my_splitter.whitespace_split = True

        print list(my_splitter)
        self.logger.info(list(my_splitter));


        for command in my_splitter:
            print str(command)
            details = command.split()

            # Execute Command
            self.dances(details[0])()





