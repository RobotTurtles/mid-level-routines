# Script simply writes to both motors the zero position. Both motors should not be turning.
from Movement import Movement

m = Movement('nonfile')

while True:
    m.writeToMotor(0, 0, 0)
    m.writeToMotor(1, 0, 0)
