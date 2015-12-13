from Movement import Movement

m = Movement('nonfile')

while True:
    m.writeToMotor(0, 0, 0)
    m.writeToMotor(1, 0, 0)
