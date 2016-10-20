
from Movement import Movement

class Basics(object):

    def __init__(self, movement, logger):
        self.m = movement
        self.logger = logger
        self.logger.info("Initialized Basics")

    def execute(self, option):

        turnAmount = 180
        driveAmount = 50

        option = option.lower()

        if(option == 'left'):
            #self.logger.info("Turning Left by Amount: " + turnAmount)
            self.m.turnDegrees(-turnAmount)
        elif(option == 'right'):
            #self.logger.info("Turning Left by Amount: " + turnAmount)
            self.m.turnDegrees(turnAmount)
        elif(option == 'forward'):
            #self.logger.info("Turning Left by Amount: " + turnAmount)
            self.m.moveCM(driveAmount)
        elif(option == 'reverse'):
            #self.logger.info("Turning Left by Amount: " + turnAmount)
            self.m.moveCM(-driveAmount)

        #self.logger("Did not find option")

        pass
