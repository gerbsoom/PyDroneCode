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
logger.debug("Created a global LogHandler.")

# setup pygame
import pygame
from pygame.locals import *
pygame.init()
gameClock = pygame.time.Clock()
logger.debug("Initialized the pygame engine.")

# setup the network server
import Com.Net.NetConf as NetConf
netConf = NetConf.create("_net.conf")

import Com.Net.Server as Server
server = Server.create(netConf)
transmitter = server.getTransmitter()
transmitter.sendData("#DATA#" + "GET sensor_state")
logger.info("Network Server is up and running.")

from sense_hat import SenseHat
senseHat = SenseHat()
import Visualizer.LedMatrix as LedMatrix
ledMatrix = LedMatrix.create(senseHat)
import Sensoric.SensorHat as SensorHat
sensorHat = SensorHat.create(senseHat)

running = True
while running:

    # check for keyboard events, maybe allow setting commands from STD_IN
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        running = False

    # cycle the TcpServer for new Events or messages
    server.cycle()

    # get the current orientation over network api and update view with it
    gyro = sensorHat.getOrientationDegrees()
    #simulator3D.rotateCubeToDegrees(360.0 - gyro["pitch"],
    #                                360.0 - gyro["yaw"],
    #                                360.0 - gyro["roll"])
    transmitter.sendData("#DATA#Orientation#" + str(gyro["pitch"]) + "#" +
                         str(gyro["yaw"]) + "#" + str(gyro["roll"]) + "#")

    gameClock.tick(50)


if __name__ == '__main__':
    main()
