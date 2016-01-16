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

    def find_and_connect(self, saveID, networkName, networkPassword):
        available_networks = subprocess.check_output(['/usr/bin/wicd-cli','-y','-S', '-l']).split('\n')

        network_num = None

        for network in available_networks:
            # match network name to available networks
            available_network = network.split('\t')
            print str(available_network)

            network_name = available_network[3]
            network_num = available_network[0]

            if(network_name == networkName):
                print 'Matched Network: '+str(network_name)
                network_num = available_network[0]
                network_bssid = available_network[1]
                break

        network_details = None

        if(network_num == None):
            raise ValueError('Network ' + str(networkName) + ' not found')

        network_details = subprocess.check_output(['/usr/bin/wicd-cli','-y','-n '+ str(network_num),'-d']).split('\n')

        properties = dict()

        for detail in network_details:
            if(detail != ''):
                propertyPair = detail.split(':')
                properties[str(propertyPair[0])] = str(propertyPair[1]).strip()

        encryptionMethod = None
        if(properties.has_key('Encryption')):
            if(properties['Encryption'] == 'On'):
                encryptionMethod = properties['Encryption Method']

        print(properties)

        if(encryptionMethod != None):
            print 'Encryption: ' + str(encryptionMethod)

        self.connect(network_num, encryptionMethod, networkPassword)

        # Once Found, Configure that specific network
        pass

    def getEncType(self,network_type):
        print 'network type: '+str(network_type)
        return {
            'WPA2':{'apsk','wpa-psk'},
            'WEP':{'passphrase','wep-passphrase'},
        }[network_type]

    def connect(self, network_num, encryption_type, network_password):
        print 'Connecting to: '+str(network_num)+', encryption type: '+str(encryption_type)+', password:'+str(network_password) 
        if(encryption_type != None):
            encType, passType = self.getEncType(encryption_type)

            print 'PassType: '+str(passType) + ' encType: '+encType

            print(subprocess.check_output(['/usr/bin/wicd-cli','-y','-n '+ str(network_num), '-p encType', '-s '+str(encType)]))
            print(subprocess.check_output(['/usr/bin/wicd-cli','-y','-n '+ str(network_num), '-p '+str(passType), '-s '+str(network_password)]))

        print(subprocess.check_output(['/usr/bin/wicd-cli','-y','-n '+ str(network_num), '--connect']))

if(__name__ == '__main__'):
    NetworkManager().find_and_connect('default','Demos','mysteryspot2')
