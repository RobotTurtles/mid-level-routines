__author__ = 'Alex'

class BaseCommand:
    def __init__(self, movement):
        assert isinstance(movement, Movement)
        self.m = movement

    def execute(selfself):pass

class Forward(BaseCommand):
    def execute(self):
        self.m.moveCM(10)

class Reverse(BaseCommand):
    def execute(self):
        self.m.moveCM(10)

class Left(BaseCommand):
    def execute(self):
        self.m.turnDegrees(-90)

class Right(BaseCommand):
    def execute(self):
        self.m.turnDegrees(90)

