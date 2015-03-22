import time
import math

class SimMovement:
	"""Simulated Robot Movement"""

	def __init__(self, logger, servoDevice = '/dev/servoblaster'):
            self.logger = logger
            self._x = 0
            self._y = 0
            self._heading = 0

        def turnDegrees(self, distance):
            self._heading += distance
            self._heading = self._heading % 360
            self.printLocation()
            
        def turnSpeed(self, velocity):
            self._heading = self._heading # do nothing

        def moveCM(self, distance):
            headingRadians = math.pi * self._heading / 180
            dx = math.cos(headingRadians) * distance
            dy = math.sin(headingRadians) * distance
            self._x += dx
            self._y += dy
            self.printLocation()
            
        def printLocation(self):
            self.logger.info( "(%f,%f) @ %d" % (self._x, self._y, self._heading) )
            
