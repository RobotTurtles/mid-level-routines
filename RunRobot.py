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

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if(os.name == "nt"):
    directory = r"c:\tmp\logs"
    targetFile = r"c:\tmp\servoCommands.txt"
    configFile=r"c:\tmp\Turtle.cfg"
else:
    directory = r"/home/pi/logs"
    targetFile = '/dev/servoblaster'
    configFile=r"/etc/turtles/Turtle.cfg"

if not os.path.exists(directory):
    os.makedirs(directory)

handler = logging.FileHandler(directory + '/TurtleThoughts.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info('Started Run Robot')
m = Movement(logger, targetFile)

# Main Action
r = WebRobot(logger, m, ConfigFileManager(logger, configFile))

r.execute()

logger.info('Turtle Has stopped running')