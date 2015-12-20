from RobotMenu import RobotMenu
import unittest
import logging


class TestSequenceFunctions(unittest.TestCase):
    """Tests for basic movement, currently write to/from a file"""

    def setUp(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        self.__targetFile = 'testResults.txt'
        self.menu = RobotMenu(logger, 'movement')

    def test_connect_wifi(self):
        # Arrange
        qrCode = 'runConnectToNetwork:bananas wpa2 mysteryspot2'

        # Act
        self.menu.process(qrCode)

        #Assert
        self.assertTrue(True, 'some message')


if __name__ == '__main__':
    unittest.main()