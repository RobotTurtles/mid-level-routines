########################################################################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Released under Apache open source license
########################################################################################################################

import subprocess
import socket

baseUrl = 'https://secret-brushlands-1127.herokuapp.com'
path = '/turtleinfo?'
turtle_name = socket.gethostname()
ip_address = socket.gethostbyname(socket.gethostname())
turtle_id = '3'

sendUrl = baseUrl + path + 'turtle_name='+turtle_name + '&ip_address=' + str(ip_address)+ '&turtle_id=' + turtle_id

response = subprocess.check_output(['/usr/bin/wget',sendUrl]).split('\n')