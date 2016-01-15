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
        available_networks = subprocess.check_output(['/usr/bin/wicd-cli','-y','-S', '-l']).split('\n')

        network_count = len(available_networks)

        network_num = None

        for network in available_networks:
            # match network name to available networks
            available_network = network.split('\t')
            print str(available_network)


            network_name = available_network[3]

            if(network_name == networkName):
                print 'Matched Network: '+str(network_name)
                network_num = available_network[0]
                network_bssid = available_network[1]
                break

        network_details = None

        if(network_num != None):
            network_details = subprocess.check_output(['/usr/bin/wicd-cli','-y','-n '+ str(network_num),'-d'])

        print str(network_details)

        # Once Found, Configure that specific network
        pass

    def main(self):
        pass