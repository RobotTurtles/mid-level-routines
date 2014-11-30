# Simple Robot Program

from msvcrt import getch
from Movement import Movement

m = Movement('testResults.txt')
distanceCM = 2
distanceDegrees = 2

while True:
    key = ord(getch())
    if key == 27: #ESC
        break
    elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
		key = ord(getch())
		
		if key == 80: #Down arrow
			print('Moving backward')
			m.moveCM(-distanceCM)
		elif key == 72: #Up arrow
			print('Moving forward')
			m.moveCM(distanceCM)
		elif key == 77: # Right Arrow
			print('Turn Right')
			m.turnDegrees(distanceDegrees)
		elif key == 75: # Left Arrow
			print('Turn Left')
			m.turnDegrees(-distanceDegrees)
		else:
			print(key)