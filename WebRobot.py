###############################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Description:
#   Main turtle execution
#
###############################################################################

import os
from Utilities.ManageCommandsFromFile import ReadCommandFromFile
from RobotMenu import RobotMenu
from Movement import Movement
import time

__author__ = 'Alex'


class WebRobot:

    def __init__(self, logger, movement, config, robotCmdFile):


        self.robotCmdFile = robotCmdFile

        # Input Parameters
        self.m = movement
        self.logger = logger
        self.config = config

        self.readCmd = ReadCommandFromFile(self.robotCmdFile)
        self.RobotMenu = RobotMenu(logger, movement,config)


    def execute(self):

        counter = 0

        while(True):
            cmd = self.readCmd.read_command()
            if (cmd):
                self.RobotMenu.process(cmd)
                self.readCmd.clear_commands()
            else:
                time.sleep(2)


if __name__ == '__main__':
    targetFile = 'testResults.txt'
    m = Movement("", targetFile)
    w = WebRobot("",m,"","")
    w.execute()
