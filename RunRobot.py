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

from CoreRobot import CoreRobot
from Movement import Movement
from Utilities.ConfigFileManager import ConfigFileManager

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

directory = '/home/pi/logs'

if not os.path.exists(directory):
    os.makedirs(directory)

handler = logging.FileHandler(directory + '/TurtleThoughts.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info('Started Run Robot')

# Main Action
r = CoreRobot(logger, Movement(logger), ConfigFileManager(logger))

r.execute()

logger.info('Turtle Has stopped running')