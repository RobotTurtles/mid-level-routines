import time


class Movement:
    """Basic Robot Movement"""

    def __init__(self, logger, servoDevice='/dev/servoblaster'):
        self.logger = logger

        self.__servoDevice = servoDevice
        self.__MotorController = open(self.__servoDevice, 'w')

        self.__leftServo = 0
        self.__rightServo = 1

        self.__leftFwdDir = 1
        self.__rightFwdDir = -1

        self.__defaultSpeed = 80

        self.__degreesToMilliSecs = 5.5
        self.__cmsToMilliSecs = 50

    def turnDegrees(self, distance):
        """Turn Robot left/right by distance in degrees"""
        targetMilliSecs = abs(distance * self.__degreesToMilliSecs)
        currentMilliSecs = 0

        if (distance < 0):
            leftDir = self.__leftFwdDir * -1
            rightDir = self.__rightFwdDir
        else:
            leftDir = self.__leftFwdDir
            rightDir = self.__rightFwdDir * -1

        while (currentMilliSecs < targetMilliSecs):
            time.sleep(0.001)
            currentMilliSecs += 1

            self.writeToMotor(self.__leftServo, leftDir, self.__defaultSpeed)
            self.writeToMotor(self.__rightServo, rightDir, self.__defaultSpeed)

        self.writeToMotor(self.__leftServo, self.__leftFwdDir, 0)
        self.writeToMotor(self.__rightServo, self.__rightFwdDir, 0)
        return True

    def turnLeftArm(self, distance):
        """
        Turn Left arm some # of degrees
        :param distance: Degrees
        :return: None
        """
        targetMilliSecs = abs(distance * self.__degreesToMilliSecs)
        currentMilliSecs = 0

        if (distance < 0):
            leftDir = self.__leftFwdDir * -1
        else:
            leftDir = self.__leftFwdDir

        while (currentMilliSecs < targetMilliSecs):
            time.sleep(0.001)
            currentMilliSecs += 1

            self.writeToMotor(self.__leftServo, leftDir, self.__defaultSpeed)

        self.writeToMotor(self.__leftServo, self.__leftFwdDir, 0)

        return True

    def turnRightArm(self, distance):
        """
        Turn Right arm some # of degrees
        :param distance: Degrees
        :return: None
        """
        targetMilliSecs = abs(distance * self.__degreesToMilliSecs)
        currentMilliSecs = 0

        if (distance < 0):
            rightDir = self.__rightFwdDir
        else:
            rightDir = self.__rightFwdDir * -1

        while (currentMilliSecs < targetMilliSecs):
            time.sleep(0.001)
            currentMilliSecs += 1

            self.writeToMotor(self.__rightServo, rightDir, self.__defaultSpeed)

        self.writeToMotor(self.__rightServo, self.__rightFwdDir, 0)
        return True


    def turnSpeed(self, velocity):
        if (velocity < 0):
            leftDir = self.__leftFwdDir * -1
            rightDir = self.__rightFwdDir
            speed = abs(velocity)
        else:
            leftDir = self.__leftFwdDir
            rightDir = self.__rightFwdDir * -1
            speed = velocity

        self.writeToMotor(self.__leftServo, leftDir, speed)
        self.writeToMotor(self.__rightServo, rightDir, speed)

    def moveCM(self, distance):
        """Move Robot forward/backward by distance in cms"""
        targetMilliSecs = abs(distance * self.__cmsToMilliSecs)
        currentMilliSecs = 0

        if (distance < 0):
            leftDir = self.__leftFwdDir * -1
            rightDir = self.__rightFwdDir * -1
        else:
            leftDir = self.__leftFwdDir
            rightDir = self.__rightFwdDir

        while (currentMilliSecs < targetMilliSecs):
            time.sleep(.001)
            currentMilliSecs += 1

            self.writeToMotor(self.__leftServo, leftDir, self.__defaultSpeed)
            self.writeToMotor(self.__rightServo, rightDir, self.__defaultSpeed)

        self.writeToMotor(self.__leftServo, self.__leftFwdDir, 0)
        self.writeToMotor(self.__rightServo, self.__rightFwdDir, 0)
        return True

    def writeToMotor(self, motor, direction, speed):
        """ Write to Motor a speed, +/- 0-100%"""
        pwmValue = 50 + round(direction * speed / 2)
        stringToWrite = str(motor) + '=' + str(pwmValue) + '%\n'
        self.__MotorController.write(stringToWrite)
        self.__MotorController.flush()
        return True
		
