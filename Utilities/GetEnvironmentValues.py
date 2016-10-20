import os

class GetEnvironmentValues(object):

    @staticmethod
    def getRootDirectory():
        if(os.name == "nt"):
            directory = r"c:\tmp\logs"
        else:
            directory = r"/home/pi/logs"
        return  directory

    @staticmethod
    def getTargetMotorFile():
        if(os.name == "nt"):
            targetFile = r"c:\tmp\servoCommands.txt"
        else:
            targetFile = '/dev/servoblaster'
        return  targetFile

    @staticmethod
    def getConfigFile():
        if(os.name == "nt"):
            configFile=r"c:\tmp\Turtle.cfg"
        else:
            configFile=r"/etc/turtles/Turtle.cfg"

        return configFile

    @staticmethod
    def getRobotCmdFile():
        if(os.name == "nt"):
            robotCmdFile = r"c:\tmp\robotCmdFile.txt"
        else:
            robotCmdFile = r"/var/www/robotCommand.txt"

        return robotCmdFile
