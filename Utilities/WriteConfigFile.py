###############################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Description:
#   Utility method to read QR Codes for debugging purposes
#
###############################################################################
import ConfigParser
import socket

config = ConfigParser.RawConfigParser()

turtle_name = socket.gethostname()
ip_address = socket.gethostbyname(socket.gethostname())
turtle_id = '3'

config.add_section('TurtleInfo')
config.set('TurtleInfo', 'ip_address', ip_address)
config.set('TurtleInfo', 'turtle_id', turtle_id)
config.set('TurtleInfo', 'turtle_name', turtle_name)

# Writing our configuration file to 'example.cfg'
with open('Turtle.cfg', 'wb') as configfile:
    config.write(configfile)