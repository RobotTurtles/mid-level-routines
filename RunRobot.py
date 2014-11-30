# Simple Robot Program

import curses
from Movement import Movement

win = curses.initscr()
win.nodelay(1)
curses.noecho()

m = Movement()
distanceCM = 2
distanceDegrees = 2

while True:
	c = win.getch()
	key = ord(c)
	
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