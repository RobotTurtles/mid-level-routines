###############################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Description:
#   This is the "start" file for all robot action. All other programs will be
# called from programs.
###############################################################################

import logging
import os

from RobotMenu import RobotMenu
from Movement import Movement

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

# Instantiating Movement out of main loop in case we make it asynchronous in the future
m = Movement(logger)

# Main Action
r = RobotMenu(logger, m)
r.execute()