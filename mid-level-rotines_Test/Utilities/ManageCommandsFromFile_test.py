import unittest
import os
import filecmp
from Utilities.ManageCommandsFromFile import ReadCommandFromFile
from Utilities.GetEnvironmentValues import GetEnvironmentValues

class ReadCommandFromFile_Test(unittest.TestCase):

    def test_read_command(self):
        robotFile = os.path.join(os.path.dirname(__file__),"../test_files/basicsLeft.txt")
        config = ReadCommandFromFile(robotFile)
        expected = r"basics:left"
        actual = config.read_command()
        self.assertEqual(expected, actual)

    def test_write_command(self):
        actual = os.path.join(os.path.dirname(__file__),"../test_files/tmp.txt")
        expected = os.path.join(os.path.dirname(__file__),"../test_files/basicsLeft.txt")
        config = ReadCommandFromFile(actual)
        cmd = r"basics:left"
        result = config.write_command(cmd)
        self.assertTrue(filecmp.cmp(expected,actual))

    def test_read_2commands(self):
        robotFile = os.path.join(os.path.dirname(__file__),"../test_files/basicsLeftRight_win.txt")
        config = ReadCommandFromFile(robotFile)
        expected = ["basics:left","basics:right"]
        actual = config.read_commands()
        self.assertEqual(expected, actual)

    def test_write_2commands(self):
        actual = os.path.join(os.path.dirname(__file__),"../test_files/tmp.txt")
        expected = os.path.join(os.path.dirname(__file__),"../test_files/basicsLeftRight_win.txt")
        config = ReadCommandFromFile(actual)
        cmd = "basics:left\nbasics:right"
        result = config.write_command(cmd)
        self.assertTrue(filecmp.cmp(expected,actual))

if __name__ == '__main__':
    unittest.main()
