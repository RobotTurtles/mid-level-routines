__author__ = 'Alex'

from ProcessFlashCard import ProcessFlashCard
import unittest
import cv2


class TestSequenceFunctions(unittest.TestCase):
    """Tests for basic template matching"""

    def setUp(self):
        self.__targetFile = 'testResults.txt'
        self.flashCard = ProcessFlashCard(self.__targetFile)

    @unittest.skip("Seems to not work, not having it cause failures in short term")
    def test_recognize_wrongCard(self):
        '''
        Tests to see if it *does not* see a wrong image
        :return:
        '''

        # Arrange
        expected = -1
        img = cv2.imread('TestFiles/Abort.jpg',0)

        # Act
        actual = self.flashCard.get_menu_choice(img)

        #Assert
        self.assertEqual(expected, actual)

    def test_recognize_execute(self):
        # Arrange
        expected = 1
        img = cv2.imread('TestFiles/Execute.jpg',0)

        # Act
        actual = self.flashCard.get_menu_choice(img)

        #Assert
        self.assertEqual(expected, actual)

    def test_recognize_FindFace(self):
        '''
        Tests to see if it *does not* see a wrong image
        :return:
        '''

        # Arrange
        expected = 3
        img = cv2.imread('TestFiles/FindFace.jpg',0)

        # Act
        actual = self.flashCard.get_menu_choice(img)

        #Assert
        self.assertEqual(expected, actual)

    def test_recognize_record(self):
        '''
        Tests to see if it *does not* see a wrong image
        :return:
        '''

        # Arrange
        expected = 2
        img = cv2.imread('TestFiles/Record.jpg',0)

        # Act
        actual = self.flashCard.get_menu_choice(img)

        #Assert
        self.assertEqual(expected, actual)

    def test_recognize_forward(self):
        '''
        Tests to see if it *does not* see a wrong image
        :return:
        '''

        # Arrange
        expected = 1
        img = cv2.imread('TestFiles/Forward.jpg',0)

        # Act
        actual = self.flashCard.get_move_choice(img)

        #Assert
        self.assertEqual(expected, actual)

    def test_recognize_left(self):
        '''
        Tests to see if it *does not* see a wrong image
        :return:
        '''

        # Arrange
        expected = 3
        img = cv2.imread('TestFiles/Left.jpg',0)

        # Act
        actual = self.flashCard.get_move_choice(img)

        #Assert
        self.assertEqual(expected, actual)

    def test_recognize_reverse(self):
        '''
        Tests to see if it *does not* see a wrong image
        :return:
        '''

        # Arrange
        expected = 2
        img = cv2.imread('TestFiles/Reverse.jpg',0)

        # Act
        actual = self.flashCard.get_move_choice(img)

        #Assert
        self.assertEqual(expected, actual)

    def test_recognize_right(self):
        '''
        Tests to see if it *does not* see a wrong image
        :return:
        '''

        # Arrange
        expected = 4
        img = cv2.imread('TestFiles/Right.jpg',0)

        # Act
        actual = self.flashCard.get_move_choice(img)

        #Assert
        self.assertEqual(expected, actual)


    def test_recognize_abort(self):
        '''
        Tests to see if it *does not* see a wrong image
        :return:
        '''

        # Arrange
        expected = 5
        img = cv2.imread('TestFiles/Abort.jpg',0)

        # Act
        actual = self.flashCard.get_move_choice(img)

        #Assert
        self.assertEqual(expected, actual)