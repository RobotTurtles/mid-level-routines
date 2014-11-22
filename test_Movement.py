from Movement import Movement
import unittest

class TestSequenceFunctions(unittest.TestCase):
	"""Tests for basic movement, currently write to/from a file"""
	
	def setUp(self):
		self.__targetFile = 'testResults.txt'
		self.m = Movement(self.__targetFile)
		

	def test_writeToMotor_stop(self):
		# Arrange
		
		# Act
		self.m.writeToMotor(0,1,0)
		expected = []
		expected.append('0=50.0%')
		actual = self.readResult()
		
		# Assert
		self.assertEqual(expected, actual)
		
	def test_writeToMotor_stop_2nd(self):
		# Arrange
		
		# Act
		self.m.writeToMotor(1,1,0)
		expected = []
		expected.append('1=50.0%')
		actual = self.readResult()
		
		# Assert
		self.assertEqual(expected, actual)

	def test_writeToMotor_fullForward(self):
		# Arrange
		
		# Act
		self.m.writeToMotor(0,1,100)
		expected = []
		expected.append('0=100.0%')
		actual = self.readResult()
		
		# Assert
		self.assertEqual(expected, actual)

	def test_writeToMotor_fullReverse(self):
		# Arrange
		
		# Act
		self.m.writeToMotor(0,1,-100)
		expected = []
		expected.append('0=0.0%')
		actual = self.readResult()
		
		# Assert
		self.assertEqual(expected, actual)

		
	def readResult(self):
		with open(self.__targetFile, 'r') as f:
			lines = f.readlines()
		
		return lines
		
if __name__ == '__main__':
    unittest.main()