###############################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Description:
#   Utility method to read Config File Properties
#
###############################################################################
import ConfigParser

class ConfigFileManager:

    def __init__(self):
        self.config = ConfigParser.RawConfigParser()

        # Writing our configuration file to 'example.cfg'
        self.configFile = '/etc/turtles/Turtle.cfg'

        self.config.read(self.configFile)

        if(not ('TurtleInfo' in self.config)):
            self.config.add_section('TurtleInfo')
            self.config.set('TurtleInfo', 'turtle_name', 'unnamed_turtle')
            self.config.set('TurtleInfo', 'turtle_id', '-99')
            self.config.set('TurtleInfo', 'ip_address', '1.1.1.1')

            with open(self.configFile, 'wb') as configfile:
                self.config.write(configfile)
        pass

    def WriteParams(self, turtle_name, turtle_id, local_ip_address):
        self.config.read(self.configFile)

        self.config.set('TurtleInfo', 'turtle_name', turtle_name)
        self.config.set('TurtleInfo', 'turtle_id', turtle_id)
        self.config.set('TurtleInfo', 'ip_address', local_ip_address)

        with open(self.configFile, 'wb') as configfile:
            self.config.write(configfile)

    def ReadParams(self):
        self.config.read(self.configFile)

        return self.config.get('TurtleInfo', 'turtle_name'),self.config.get('TurtleInfo', 'turtle_id'), self.config.get('TurtleInfo', 'ip_address')

    def SetId(self, turtle_id):
        self.config.read(self.configFile)

        self.config.set('TurtleInfo', 'turtle_id', turtle_id)

        with open(self.configFile, 'wb') as configfile:
            self.config.write(configfile)


if(__name__ == '__main__'):
    cm = ConfigFileManager()
    print cm

    turtle_name, turtle_id, turtle_ipAddress = cm.ReadParams()
    print('Turtle Name: '+turtle_name)
    print('Turtle ID: '+turtle_id)
    print('Turtle IP Address: '+turtle_ipAddress)