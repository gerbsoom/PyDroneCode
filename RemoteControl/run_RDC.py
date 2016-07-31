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

# ________________________________________________________________
# Launches an interface to remote control a drone over the network

import sys
baseDir = "/home/pi/Desktop/DEV/gitdirs/PyDroneCode/"
# add SharedLibraries as additional module loading path (simplify installation)
sys.path.insert(0, baseDir + "SharedLibraries")
# add Simulator directory to simplify installation
sys.path.insert(1, baseDir + "RemoteControl/Visualizer/View3D")

# setup logging
from LoggerFactory import LogHandler
LogHandler.initialize("_log.conf")
logger = LogHandler.getLogger("Launcher")
logger.debug("Created a global LogHandler to retrieve configured logger from.")

# setup pygame
import pygame
from pygame.locals import *
pygame.init()
gameClock = pygame.time.Clock()
logger.debug("Initialized the pygame engine.")

# setup the network server
import Com.Net.NetConf as NetConf
netConf = NetConf.create("_netConf")

import Com.Net.Server as Server
server = Server.create(netConf)
transmitter = server.getTransmitter()
transmitter.sendData("#CMD#GET sensor_state")
logger.info("Network Server is up and running.")

# setup a gamepad controller
from Controller import Gamepad
# and set the Network CMD/DATA-Transmitter
gamepad = Gamepad.create(pygame, transmitter)

# setup the 3D Simulator
import Visualizer.View3D.Simulator as Simulator
simulator = Simulator.create(pygame)
simulator.start()

running = True
while running:

    pygame.event.pump()
    # check for keyboard events, maybe allow setting commands from STD_IN
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        running = False

    # cycle gamepad for button events or relevant throttle value changes
    gamepad.cycle()

    # cycle the TcpServer for new Events or messages
    tcpServer.cycle()

    # get the current orientation over network api and update view with it
    #gyro = sensorSenseHat.getOrientationDegrees()
    #simulator3D.rotateCubeToDegrees(360.0 - gyro["pitch"],
    #                                360.0 - gyro["yaw"],
    #                                360.0 - gyro["roll"])
    gameClock.tick(50)

    simulator.cycle()

if __name__ == '__main__':
    main()
