
from Movement import Movement

class Basics(object):

    def __init__(self, movement, logger):
        self.m = movement
        self.logger = logger
        self.logger.info("Initialized Basics")

    def execute(self, args):

        if(len(args) == 0):
            self.logger.info("No arguments found!")
            return

        turnAmount = 90
        driveAmount = 15

        option = args.lower()

        if(option == 'left'):
            self.m.turnDegrees(-turnAmount)
        elif(option == 'right'):
            self.m.turnDegrees(turnAmount)
        elif(option == 'forward'):
            self.m.moveCM(driveAmount)
        elif(option == 'reverse'):
            self.m.moveCM(-driveAmount)

        pass