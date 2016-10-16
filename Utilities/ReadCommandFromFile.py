import os

class ReadCommandFromFile(object):

    def __init__(self, cmdFile):
        self.cmdFile = cmdFile
        pass

    def get_command(self):

        cmd = ''

        with open(self.cmdFile, 'r') as cmdFile:
            cmd = cmdFile.readline().strip()

        return cmd

