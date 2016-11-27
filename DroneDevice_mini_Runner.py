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
#
# ________________________________________________________________________________
# Starter for the DroneDevice App configured in: config/<application>.conf
#
# Runner ID
application = "drone-device_mini"

import os
import sys
# append libs to module loading path
sys.path.insert(0, "launcher/")
sys.path.insert(0, "lib/")

from Application import DroneDeviceApp
#import ConfigParser
import configparser

# setup the logging from a config
from LoggerFactory import LogHandler
LogHandler.initialize("config/" + application + "/log.conf")
logger = LogHandler.getLogger("Runner_" + application)

# Print some info about the runner and the environment
logger.debug("PyRunner Location: " + str(sys.argv[0]))
logger.debug("Working Directory: " + str(os.getcwd()))
logger.debug("Library Module Path: " + str(sys.path))


if __name__ == '__main__':
    main()
