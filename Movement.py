import time

class Movement:
	"""Basic Robot Movement"""
	
	def __init__(self, servoDevice = '/dev/servoblaster'):
		
		self.__servoDevice = servoDevice
		self.__MotorController = open(self.__servoDevice, 'w')
		
		self.__leftServo = 0
		self.__rightServo = 1
	
		self.__leftFwdDir = 1
		self.__rightFwdDir = -1
		
		self.__defaultSpeed = 80
	
		self.__degreesToSecs = 1
		self.__cmsToSecs = 1
	
	def turnDegrees(self, distance):
		"""Turn Robot left/right by distance in degrees"""
		targetSecs = abs(distance * self.__degreesToSecs)
		currentSecs = 0
		
		if(distance < 0):
			leftDir = self.__leftFwdDir * -1
			rightDir = self.__rightFwdDir
		else:
			leftDir = self.__leftFwdDir
			rightDir = self.__rightFwdDir * -1
		
		while(currentSecs < targetSecs):
			time.sleep(1)
			currentSecs += 1
			
			self.writeToMotor(self.__leftServo, leftDir, self.__defaultSpeed)
			self.writeToMotor(self.__rightServo, rightDir, self.__defaultSpeed)
			
		self.writeToMotor(self.__leftServo, self.__leftFwdDir, 0)
		self.writeToMotor(self.__rightServo, self.__rightFwdDir, 0)
		return True
		
	def moveCM(self, distance):
		"""Move Robot forward/backward by distance in cms"""
		targetSecs = abs(distance * self.__cmsToSecs)
		currentSecs = 0
		
		if(distance < 0):
			leftDir = self.__leftFwdDir * -1
			rightDir = self.__rightFwdDir -1
		else:
			leftDir = self.__leftFwdDir
			rightDir = self.__rightFwdDir
		
		while(currentSecs < targetSecs):
			time.sleep(1)
			currentSecs += 1
			
			self.writeToMotor(self.__leftServo, leftDir, self.__defaultSpeed)
			self.writeToMotor(self.__rightServo, rightDir, self.__defaultSpeed)
			
		self.writeToMotor(self.__leftServo, self.__leftFwdDir, 0)
		self.writeToMotor(self.__rightServo, self.__rightFwdDir, 0)
		return True
	
	def writeToMotor(self, motor, direction, speed):
		""" Write to Motor a speed, +/- 0-100%"""
		pwmValue = 50 + round(direction*speed/2)
		stringToWrite = str(motor) + '=' + str(pwmValue) + '%\n'
		self.__MotorController.write(stringToWrite)
		self.__MotorController.flush()
		return True
		