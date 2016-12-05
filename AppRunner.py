#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of PyDroneCode.
# Please check the file LICENSE.MD for information about the license.
#
# @file
# @version 0.5
# @copyright 2016 Desmodul
# @author Markus Riegert <desmodul@drow-land.de>
#
# _____________________________________________________________________________
# Starts the Drone Application configured in 'baseDir/config/<app>/<app>.conf'


def runnerVersion():
    return "0.5"


def defaultApp():
    return "DroneDevice"


import sys
import os


def main():
    # relative pathes work as well
    baseDir = os.path.dirname(os.path.realpath(__file__)) + "/"

    # overwrite start app
    if len(sys.argv) > 1:
        app = str(sys.argv[1])
    else:
        app = defaultApp()

    version = runnerVersion()
    confDir = baseDir + "config/" + app + "/"

    # overwrite the config folder location
    if len(sys.argv) > 2:
        confDir = str(sys.argv[2])
        if confDir == ".":
            confDir = baseDir

    try:
        # append module include pathes to python's library loading path
        sys.path.insert(0, baseDir + "library/")
        sys.path.insert(0, baseDir + "launcher/")
        print(("Fully imported Library Module Path: " + str(sys.path)))
        try:
            # setup the logging from a config
            from LoggerFactory import LogHandler
            logConfig = confDir + "log.conf"
            print(("Assuming log config at " + logConfig))
            LogHandler.initialize(logConfig)
            logger = LogHandler.getLogger("Runner__" + app)
            logger.debug("Successfully loaded logging environment")

            # Print some info about the runner and the environment
            logger.debug("Runner" + "_V_" + version + "_: " + app)
            logger.debug("PyRunner Location: " + str(sys.argv[0]))
            logger.debug("Working Directory: " + str(os.getcwd()))
            logger.debug("Library Loading Path: " + str(sys.path))
            logger.debug("Config Directory Path: " + str(confDir))
            try:
                from ConfigFactory import ConfigUtility
                confUtil = ConfigUtility.create(app, confDir)
                droneConf = confUtil.loadConfig(confDir + "app.conf")
                logger.debug("Config successfully loaded")

                from Application import DroneDevice
                app = DroneDevice.create(droneConf)
                #logger.debug("Initialization: OK")
                # app.setup()
                #logger.debug("Setup: OK")
                app.run()

            except:
                print(("ERR: Initializing Application! E=", sys.exc_info()[0]))
        except:
            print(("ERR: Loading Logging Environment! E=", sys.exc_info()[0]))
    except:
        print(("ERR: Accessing Library Loading Path! E=", sys.exc_info()[0]))

    print(("______________________________________"))
    print(("Runner" + "_V_" + version + "_: " + app))
    print(("PyRunner Location: " + str(sys.argv[0])))
    print(("Working Directory: " + str(os.getcwd())))
    print(("Library Loading Path: " + str(sys.path)))
    print(("Config Directory Path: " + str(confDir)))


if __name__ == '__main__':
    main()
