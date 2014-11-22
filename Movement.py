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
		targetSecs = abs(distance * __degreesToSecs)
		currentSecs = 0
		
		if(distance < 0):
			leftDir = __leftFwdDir * -1
			rightDir = __rightFwdDir
		else:
			leftDir = __leftFwdDir
			rightDir = __rightFwdDir * -1
		
		while(currentSecs < targetSecs):
			time.sleep(1)
			currentSecs += 1
			
			writeToMotor(__leftServo, leftDir, __defaultSpeed)
			writeToMotor(__rightServo, rightDir, __defaultSpeed)
			
		writeToMotor(__leftServo, __leftFwdDir, 0)
		writeToMotor(__rightServo, __rightFwdDir, 0)
		return True
		
	def moveCM(self, distance):
		"""Move Robot forward/backward by distance in cms"""
		targetSecs = abs(distance * __cmsToSecs)
		currentSecs = 0
		
		if(distance < 0):
			leftDir = __leftFwdDir * -1
			rightDir = __rightFwdDir -1
		else:
			leftDir = __leftFwdDir
			rightDir = __rightFwdDir
		
		while(currentSecs < targetSecs):
			time.sleep(1)
			currentSecs += 1
			
			writeToMotor(__leftServo, leftDir, __defaultSpeed)
			writeToMotor(__rightServo, rightDir, __defaultSpeed)
			
		writeToMotor(__leftServo, __leftFwdDir, 0)
		writeToMotor(__rightServo, __rightFwdDir, 0)
		return True
	
	def writeToMotor(self, motor, direction, speed):
		""" Write to Motor a speed, +/- 0-100%"""
		pwmValue = 50 + round(direction*speed/2)
		stringToWrite = str(motor) + '=' + str(pwmValue) + '%'
		self.__MotorController.write(stringToWrite)
		self.__MotorController.flush()
		return True
		