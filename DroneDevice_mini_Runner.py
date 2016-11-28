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
# _____________________________________________________________________________
# Starter for the DroneDevice App configured in: config/<application>.conf

# Runner ID
app = "drone-device_mini"
version = 0.3

import os
import sys

print(("RunnerID: " + app + "_V_" + str(version)))
print(("PyRunner Location: " + str(sys.argv[0])))
print(("Working Directory: " + str(os.getcwd())))

try:
    # append the needed includes to the python module loading path
    sys.path.insert(0, "lib/")
    sys.path.insert(0, "launcher/")
    print(("Fully imported Library Module Path: " + str(sys.path)))
    try:
        # setup the logging from a config
        from LoggerFactory import LogHandler
        logConfig = "config/" + app + "/log.conf"

        print(("Assuming log config at " + logConfig))
        LogHandler.initialize(logConfig)
        logger = LogHandler.getLogger("Runner__" + app)
        logger.debug("Successfully loaded logging environment")

        # Print some info about the runner and the environment
        logger.debug("PyRunner Location: " + str(sys.argv[0]))
        logger.debug("Working Directory: " + str(os.getcwd()))
        logger.debug("Library Module Path: " + str(sys.path))

        try:

        except:
            print(("ERROR: Initializing DroneDevice!!! E=", sys.exc_info()[0]))
    except:
        print(("ERROR: Loading logging environment!!! E=", sys.exc_info()[0]))
except:
    print(("ERROR: Accessing the libpath!!! E=", sys.exc_info()[0]))
