from Movement import Movement
import unittest


class TestSequenceFunctions(unittest.TestCase):
    """Tests for basic movement, currently write to/from a file"""

    def setUp(self):
        self.__targetFile = 'testResults.txt'
        self.m = Movement(self.__targetFile)

    def test_moveCM_0(self):
        # Arrange
        expected = ['0=50.0%\n', '1=50.0%\n']

        # Act
        self.m.moveCM(0)
        actual = self.readResult()

        #Assert
        self.assertEqual(expected, actual)

    def test_turnDegrees_0(self):
        # Arrange
        expected = ['0=50.0%\n', '1=50.0%\n']

        # Act
        self.m.turnDegrees(0)
        actual = self.readResult()

        #Assert
        self.assertEqual(expected, actual)

    def test_turnSpeed_0(self):
        # Arrange
        expected = ['0=50.0%\n', '1=50.0%\n']

        # Act
        self.m.turnSpeed(0)
        actual = self.readResult()

        #Assert
        self.assertEqual(expected, actual)

    def test_turnSpeed_10(self):
        # Arrange
        expected = ['0=55.0%\n', '1=55.0%\n']

        # Act
        self.m.turnSpeed(10)
        actual = self.readResult()

        #Assert
        self.assertEqual(expected, actual)

    def test_turnSpeed_neg_10(self):
        # Arrange
        expected = ['0=45.0%\n', '1=45.0%\n']

        # Act
        self.m.turnSpeed(-10)
        actual = self.readResult()

        #Assert
        self.assertEqual(expected, actual)

    def test_writeToMotor_negative(self):
        # Arrange

        # Act
        self.m.writeToMotor(0, 1, -10)
        expected = ['0=45.0%\n']
        actual = self.readResult()

        # Assert
        self.assertEqual(expected, actual)

    def test_writeToMotor_negative2(self):
        # Arrange

        # Act
        self.m.writeToMotor(0, -1, -10)
        expected = ['0=55.0%\n']
        actual = self.readResult()

        # Assert
        self.assertEqual(expected, actual)

    def test_writeToMotor_stop(self):
        # Arrange

        # Act
        self.m.writeToMotor(0, 1, 0)
        expected = ['0=50.0%\n']
        actual = self.readResult()

        # Assert
        self.assertEqual(expected, actual)

    def test_writeToMotor_stop_2nd(self):
        # Arrange
        expected = ['1=50.0%\n']

        # Act
        self.m.writeToMotor(1, 1, 0)
        actual = self.readResult()

        # Assert
        self.assertEqual(expected, actual)

    def test_writeToMotor_fullForward(self):
        # Arrange

        # Act
        self.m.writeToMotor(0, 1, 100)
        expected = ['0=100.0%\n']
        actual = self.readResult()

        # Assert
        self.assertEqual(expected, actual)

    def test_writeToMotor_fullReverse(self):
        # Arrange

        # Act
        self.m.writeToMotor(0, 1, -100)
        expected = ['0=0.0%\n']
        actual = self.readResult()

        # Assert
        self.assertEqual(expected, actual)


    def readResult(self):
        with open(self.__targetFile, 'r') as f:
            lines = f.readlines()

        return lines


if __name__ == '__main__':
    unittest.main()