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

# __________________________________________________________________________
# Interfaces and Librarary to communicate and visialize on the drone device.

import sys
baseDir = "/home/pi/Desktop/DEV/gitdirs/PyDroneCode/"
# add SharedLibraries as additional module loading path (simplify installation)
sys.path.insert(0, baseDir + "SharedLibraries")

# setup logging
from LoggerFactory import LogHandler
LogHandler.initialize("_log.conf")
logger = LogHandler.getLogger("Launcher")
logger.debug("Created a global LogHandler to retrieve configured logger from.")

# setup the network server
import Com.Net.NetConf as NetConf
netConf = NetConf.create("_netConf")

import Com.Net.Server as Server
server = Server.create(netConf)
transmitter = server.getTransmitter()
transmitter.sendData("#DATA#" + "GET sensor_state")
logger.info("Network Server is up and running.")
