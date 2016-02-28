########################################################################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Released under Apache open source license
########################################################################################################################

import subprocess
import socket

def PingServer(turtle_name, ip_address, turtle_id):
    baseUrl = 'https://secret-brushlands-1127.herokuapp.com'
    path = '/turtleinfo?'

    sendUrl = baseUrl + path + 'turtle_name='+turtle_name + '&ip_address=' + str(ip_address)+ '&turtle_id=' + turtle_id

    response = subprocess.check_output(['/usr/bin/wget', '--quiet','--spider',sendUrl]).split('\n')

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets

    turtle_name = socket.gethostname()
    ip_address = s.getsockname()[0]
    turtle_id = '3'

    PingServer(turtle_name, ip_address, turtle_id)