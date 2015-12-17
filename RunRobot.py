# Simple Robot Program
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

m = Movement(logger)
r = RobotMenu(logger, m)

r.execute()

from Movement import Movement
from DanceRoutines import  DanceRoutines
import logging

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
logger = logging.getLogger('basic')


m = Movement('test')
d = DanceRoutines(m, logger)