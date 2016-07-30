#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# This file is part of PyDroneCode.
# Please check the file LICENSE.MD for information about the license. 
#
# @file
# @version 0.3
# @copyright 2016 Desmodul
# @author Markus Riegert <desmodul@drow-land.de>
# _______________________________________________________________
# Offers basic functionalities to retrieve suitable loggers from
# a valid configuration file, provided as constructor parameters.
# Without config file logging falls back to print debug on STDout.

import os, sys
import os.path
import logging
import logging.config


class LogHandler(object):
    """ Tries to read the log configuration from a provided config file
        and defaults otherwise to a simple STDout logging of all levels. """

    def __init__(self, _logConfig="_log.conf"):

        self.defaultFormat = "%(asctime)s [%(levelname)s] %(name)s %(message)s"

        logOk = False
        if os.path.isfile(_logConfig):
            if os.access(_logConfig, os.R_OK):
                try:
                    logging.config.fileConfig(_logConfig)
                    logOk = True
                except:
                    print(("ERROR: Parsing config!!! E=", sys.exc_info()[0]))
            else:
                print("ERROR: Config exists but is not accessible!!!")
        else:
            print("ERROR: Config does NOT exist!!!")

        if logOk:
            logging.getLogger(__name__).info("Config parsed successfully.")
        else:
            logging.basicConfig(format=self.defaultFormat, level='DEBUG')
            logging.warn("Falling back to default log on STDout")

    def getLogger(self, _name=""):
        """ Returns a specific log instance the caller's name as channel. """
        return logging.getLogger(_name)

def getLogger(_name="", _logConfig="_log.conf"):
    logHandler = LogHandler(_logConfig)
    return logHandler.getLogger(_name)
