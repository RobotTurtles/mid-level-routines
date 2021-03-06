###############################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015, 2016
#
# Description:
#   This is the "start" file for all robot action. All other programs will be
# called from programs.
###############################################################################

import logging
import os

from WebRobot import WebRobot
from Movement import Movement
from Utilities.ConfigFileManager import ConfigFileManager
from Utilities.GetEnvironmentValues import GetEnvironmentValues

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

directory = GetEnvironmentValues.getRootDirectory()
targetDevice = GetEnvironmentValues.getTargetMotorFile()
configFile = GetEnvironmentValues.getConfigFile()
robotCmdFile = GetEnvironmentValues.getRobotCmdFile()

if not os.path.exists(directory):
    os.makedirs(directory)

targetLog = directory + '/TurtleThoughts.log'
print("Writing Log to: " + targetLog)
handler = logging.FileHandler(targetLog)
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info('Started Run Robot')
m = Movement(logger, targetDevice)

# Main Action
r = WebRobot(logger, m, ConfigFileManager(logger, configFile), robotCmdFile)

r.execute()

logger.info('Turtle Has stopped running')
