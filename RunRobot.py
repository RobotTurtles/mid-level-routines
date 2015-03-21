# Simple Robot Program

from Movement import Movement


def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt

        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty

    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch


def _find_movement():
    try:
        import termios

        return Movement()
    except ImportError:
        return Movement('temptFile.txt')


getch = _find_getch()

m = _find_movement();

distanceCM = 2
distanceDegrees = 2

while True:
    key = ord(getch())

    if key == 27:  # ESC
        break
    elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
        key = ord(getch())

        if key == 80:  # Down arrow
            print('Moving backward')
            m.moveCM(-distanceCM)
        elif key == 72:  # Up arrow
            print('Moving forward')
            m.moveCM(distanceCM)
        elif key == 77:  # Right Arrow
            print('Turn Right')
            m.turnDegrees(distanceDegrees)
        elif key == 75:  # Left Arrow
            print('Turn Left')
            m.turnDegrees(-distanceDegrees)
        else:
            print(key)
				
