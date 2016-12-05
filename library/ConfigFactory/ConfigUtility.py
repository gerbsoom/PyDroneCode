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
# ConfigLoader offers functionialities to load, modify and store config objects.

from LoggerFactory import LogHandler

import sys
import os
import os.path
import configparser


class ConfigUtility(object):
    """ Offers the functioniality to load, modify and store config objects """
    def __init__(self, _appName, _confDir=False):
        self.app = _appName
        self.loadedConfig = 0
        self.logger = LogHandler.getLogger(__name__)

    def loadConfig(self, _configFile):
        # iterate relative/explicit path, app's conf dir and default location
        self.logger.debug("Loading config from: " + _configFile)
        self.loadedConfig = 0
        if os.path.isfile(_configFile):
            if os.access(_configFile, os.R_OK):
                try:
                    self.loadedConfig = configparser.ConfigParser()
                    self.loadedConfig.read(_configFile)
                    self.logger.debug("...Success...")
                    # due to case and options, merge the default values
                except:
                    print(("ERROR: Parsing config!!! E=", sys.exc_info()[0]))
                    self.loadedConfig = 0
            else:
                print("ERROR: Config exists but is not accessible!!!")
        else:
            print("ERROR: Config does NOT exist!!!")

        # support to run with equal configs that resist in similar locations
        return self.loadedConfig

    def validateConfig(self, _otherConfigToValidate=0):
        if _otherConfigToValidate:
        # if isinstance(_otherConfigToValidate, configparser.ConfigParser):
            configToValidate = _otherConfigToValidate
        else:
            configToValidate = self.loadedConfig
        # iterate a special validation field which asserts values in range and
        # type- (Float/String), format- (TXT/JSON) and content checks (IP4/GPIO)
        return True

    def debugConfiguration(self, _config=0):
        if _config:
            debugConfig = _config
            self.logger.debug("Debugging provided config")
        else:
            if self.hasConfigLoaded():
                debugConfig = self.loadedConfig
                self.logger.debug("Debugging underlying config")
            else:
                self.logger.debug("Error: No config for debug available")
        # iterate sections, fields and log it

#    def mergeSection(self, _mergeSection, preventOrigin):
#        for options in _mergeSection:
#            self.logger.debug("Option")
#            #

    def fillFromLoadedConfig(self, _loadedConfig):
        self.logger.notice("Modify my values to be like in _loadedConfig")
        # check if the object types (or configFiles) fit togehter
        # foreach entry in iterateMembers(_loadedConfig)
        #     self.loadedConfig.set($s, $entry, _loadedConfig.get($s,$entry)
        # try-catch and debug what is missing and what has failed
        return True

    def baseTypeFrom(self, _section):
        if _section:
            return True
        return False

    def hasConfigLoaded(self):
        if self.loadedConfig:
            return True
        return False


def create(_appName, _confDir):
    return ConfigUtility(_appName, _confDir)
