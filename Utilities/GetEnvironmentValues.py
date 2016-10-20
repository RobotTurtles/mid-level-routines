import os

class GetEnvironmentValues(object):

    @staticmethod
    def getRootDirectory():
        if(os.name == "nt"):
            directory = r"c:\tmp\logs"
        elif(os.name == "posix"):
            rootPath = os.path.abspath("../info")
            directory = rootPath+r"/logs"
        else:
            directory = r"/home/pi/logs"
        return  directory

    @staticmethod
    def getTargetMotorFile():
        if(os.name == "nt"):
            targetFile = r"c:\tmp\servoCommands.txt"
        elif(os.name == "posix"):
            rootPath = os.path.abspath("../info")
            targetFile = rootPath+r"/servoCommands.txt"
        else:
            targetFile = '/dev/servoblaster'
        return  targetFile

    @staticmethod
    def getConfigFile():
        if(os.name == "nt"):
            configFile=r"c:\tmp\Turtle.cfg"
        elif(os.name == "posix"):
            rootPath = os.path.abspath("../info")
            configFile=rootPath+r"/Turtle.cfg"
        else:
            configFile=r"/etc/turtles/Turtle.cfg"

        return configFile

    @staticmethod
    def getRobotCmdFile():
        if(os.name == "nt"):
            robotCmdFile = r"c:\tmp\robotCmdFile.txt"
        elif(os.name == "posix"):
            rootPath = os.path.abspath("../info")
            robotCmdFile = rootPath+r"/robotCommand.txt"
        else:
            robotCmdFile = r"/var/www/robotCommand.txt"

        return robotCmdFile
