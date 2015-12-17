from FaceRecognition import FaceRecognition

class Follow:

    def __init__(self, logger, qr, movement):
        '''
        Constructor
        :return:
        '''
        self.qr = qr
        self.logger = logger
        self.targetWidth = 160
        self.center = 320
        self.turnThreshold = 5
        self.moveThreshold = 10
        self.m = movement

    def moveToTarget(self, targetFunction):
        while (True):
            qrCode = self.qr.lookForCode()

            if(qrCode != None):
                return qrCode

            targetLocation = targetFunction()

            if(targetLocation == None):
		print 'No Ball Found'
                continue

            print str(targetLocation)
            if (targetLocation[2] == 0):
                targetLocation[2] = self.targetWidth

            if (targetLocation[0] != 0 and targetLocation[1] != 0):
                width = targetLocation[2]
                delta = targetLocation[0] - self.center

                self.logger.info("Target Delta from center is:" + str(delta))

                # turn left
                if (delta > self.turnThreshold + (width / 2)):
                    self.m.turnDegrees(10)

                    # turn right
                if (delta < -self.turnThreshold - (width / 2)):
                    self.m.turnDegrees(-10)

                # target is within turnThreshold, move closer/farther
                if (delta <= (self.turnThreshold + (width / 2)) and delta >= (-self.turnThreshold - (width / 2))):

                    self.logger.info('Movement Width is:' + str(width))

                    self.logger.info("Inside Turn Threshold")
                    self.m.turnSpeed(0)

                    if (width < self.targetWidth - self.moveThreshold):
                        self.logger.info("Moving Forward")
                        self.m.moveCM(8)

                    if (width > self.targetWidth + self.moveThreshold):
                        self.logger.info("Moving Backward")
                        self.m.moveCM(-8)

                    if (width > self.targetWidth - self.moveThreshold and width < self.targetWidth + self.moveThreshold):
                        self.logger.info("Staying Still")
                        self.m.moveCM(0)
