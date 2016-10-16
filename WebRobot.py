###############################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Description:
#   Main turtle execution
#
###############################################################################

import os
from Utilities.ReadCommandFromFile import ReadCommandFromFile
from RobotMenu import RobotMenu
from Movement import Movement

__author__ = 'Alex'


class WebRobot:

    def __init__(self, logger, movement, config):

        if(os.name == "nt"):
            self.robotCmdFile = r"c:\tmp\command.txt"
        else:
            self.robotCmdFile = r"/var/www/command.txt"

        # Input Parameters
        self.m = movement
        self.logger = logger
        self.config = config

        self.readCmd = ReadCommandFromFile(self.robotCmdFile)
        self.RobotMenu = RobotMenu(logger, movement,config)


    def execute(self):

        counter = 0

        while(True):
            cmd = self.readCmd.get_command()
            self.RobotMenu.process(cmd)
            pass

if __name__ == '__main__':
    targetFile = 'testResults.txt'
    m = Movement("", targetFile)
    w = WebRobot("",m,"")
    w.execute()
