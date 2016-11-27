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
# import ConfigParser
import configparser


class ConfigLoader(object):
    """ Offers functioniality to convert config objects, files and strings. """

    def __init__(self):
        self.loadedConfig = 0
        self.logger = LogHandler.getLogger(__name__)

    def loadConfig(self, _configFile):
        self.logger.debug("Loading config from: " + _configFile)
        self.loadedConfig = 0
        if os.path.isfile(_configFile):
            if os.access(_configFile, os.R_OK):
                try:
                    # config = ConfigParser.RawConfigParser()
                    self.loadedConfig = configparser.RawConfigParser()

                    self.loadedConfig.read(_configFile)
                    self.logger.info("...Success...")
                    return self.loadedConfig
                except:
                    print(("ERROR: Reading config!!! E=", sys.exc_info()[0]))
        return False

#self.loadedConfig.get("lan", "targetLan")
#self.loadedConfig.get("lan", "targetWlan")
#self.loadedConfig.getint("lan", "targetPort")
#self.loadedConfig.get("lan", "listenAdress")
#self.loadedConfig.getint("lan", "listenerPort")

    def debugConfiguration(self, _config=0):
        #debugConfig = _config
        if _config:
            self.logger.debug("Debugging the provided configuration...")
        else:
            self.logger.debug("No config provided, try to use the loaded one")
            if self.hasConfigLoaded():
                self.logger.debug("Debugging the loaded configuration...")
            else:
                self.logger.debug("No loaded config for debug available")

    def fillFromLoadedConfig(self, _loadedConfig):
        self.logger.notice("Modify my values to be like in _loadedConfig")
        # check if the object types (or configFiles) fit togehter
        # foreach entry in iterateMembers(_loadedConfig)
        #     self.loadedConfig.set($s, $entry, _loadedConfig.get($s,$entry)
        # try-catch and debug what is missing and what has failed
        return True

    def hasConfigLoaded(self):
        if self.loadedConfig:
            return True
        return False
