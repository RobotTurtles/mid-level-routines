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

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
local_ip_address = s.getsockname()[0]

turtle_name = socket.gethostname()
turtle_id = '3'

config.add_section('TurtleInfo')
config.set('TurtleInfo', 'turtle_name', turtle_name)
config.set('TurtleInfo', 'turtle_id', turtle_id)
config.set('TurtleInfo', 'ip_address', local_ip_address)

# Writing our configuration file to 'example.cfg'
with open('Turtle.cfg', 'wb') as configfile:
    config.write(configfile)