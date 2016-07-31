# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of PyDroneCode.
# Please check the file LICENSE.MD for information about the license.
#
# @file
# @version 0.1
# @copyright 2016 Desmodul
# @author Markus Riegert <desmodul@drow-land.de>
# ______________________________________________________________________________
# Holds the current network configuration which is initially loaded from config.

from LoggerFactory import LogHandler

import sys
import os
import os.path
import configparser


class NetConf(object):
    """ Holds the current network configuration. """

    def __init__(self, _config="_net.conf"):
        self.logger = LogHandler.getLogger(__name__)
        self.logger.debug("Parsing config at: " + _config)
        if os.path.isfile(_config):
            if os.access(_config, os.R_OK):
                try:
                    config = configparser.RawConfigParser()
                    config.read(_config)
                    self.targetLan = config.get("lan", "targetLan")
                    self.targetWlan = config.get("lan", "targetWlan")
                    self.targetPort = config.getint("lan", "targetPort")
                    self.listenAdress = config.get("lan", "listenAdress")
                    self.listenerPort = config.getint("lan", "listenerPort")
                    self.logger.info("Config parsed successfully.")

                except:
                    print(("ERROR: Parsing config!!! E=", sys.exc_info()[0]))
                    self.logger.info("Using default values from memory")
                    self.targetLan = "192.168.1.199"
                    self.targetWlan = "192.168.23.199"
                    self.targetPort = 20050
                    self.listenAdress = "192.168.23.198"
                    self.listenerPort = 20040
            else:
                print("ERROR: Config exists but is not accessible!!!")
        else:
            print("ERROR: Config does NOT exist!!!")


def create(_config):
    netConf = NetConf(_config)
    return netConf
