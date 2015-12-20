__author__ = 'Alex'

from Movement import Movement

class BaseCommand:
    def __init__(self, movement):
        assert isinstance(movement, Movement)
        self.name = 'unknown'
        self.m = movement

    def execute(selfself):pass

class Forward(BaseCommand):
    def __init__(self, movement):
        assert isinstance(movement, Movement)
        self.name = 'forward'
        self.m = movement

    def execute(self):
        self.m.moveCM(10)

class Reverse(BaseCommand):
    def __init__(self, movement):
        assert isinstance(movement, Movement)
        self.name = 'reverse'
        self.m = movement

    def execute(self):
        self.m.moveCM(10)

class Left(BaseCommand):
    def __init__(self, movement):
        assert isinstance(movement, Movement)
        self.name = 'left'
        self.m = movement

    def execute(self):
        self.m.turnDegrees(-90)

class Right(BaseCommand):
    def __init__(self, movement):
        assert isinstance(movement, Movement)
        self.name = 'right'
        self.m = movement

    def execute(self):
        self.m.turnDegrees(90)

