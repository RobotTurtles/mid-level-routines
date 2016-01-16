########################################################################################################################
# Robot Turtles
# Copyright Alexander L Gutierrez 2015
#
# Released under Apache open source license
########################################################################################################################

import subprocess

class UpdateManager:
    '''
    https://github.com/dpaleino/wicd/blob/master/cli/README.cli
    '''

    def __init__(self, logger):
        self.logger = logger

    def updateMidLevelRoutines(self):
        self.logger.info(subprocess.check_output(['git','reset','--hard']))
        self.logger.info(subprocess.check_output(['git','clean','-df']))
        self.logger.info(subprocess.check_output(['git','pull']))


    def updatePackages(self):
        self.logger.info(subprocess.check_output(['sudo','/usr/bin/apt-get','update']))

    def installPackages(self, install_list):
        self.logger.info(subprocess.check_output(['sudo','/usr/bin/apt-get','install', install_list]))

    def upgradePackages(self):
        self.logger.info(subprocess.check_output(['sudo','/usr/bin/apt-get','upgrade', '-y']))



if(__name__ == '__main__'):
    pass