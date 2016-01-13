########################################################################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Released under Apache open source license
########################################################################################################################

import subprocess

class NetworkManager:
    '''
    https://github.com/dpaleino/wicd/blob/master/cli/README.cli
    '''

    def __init__(self):
        pass

    def connect(self, saveID, networkName, networkType, networkPassword):
        available_networks = subprocess.check_output(['/usr/bin/wicd-cli','-y','-l']).split('\n')

        network_count = len(available_networks)

        for network in available_networks:
            # match network name to available networks
            available_network = network.split('\t')
            print str(available_network)

        # Once Found, Configure that specific network
        pass

    def main(self):
        pass