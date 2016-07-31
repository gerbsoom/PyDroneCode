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
# add SharedLibraries as additional module loading path (simplify installation)
sys.path.insert(0, '/home/pi/Desktop/DEV/gitdirs/PyDroneCode/SharedLibraries')

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

# setup network server
from Network import NetworkConfig
from Network import TcpServer
networkConfig = NetworkConfig.create()
tcpServer = TcpServer.create(networkConfig)
logger.info("Network Server is up and running.")
transmitter = tcpServer.getTransmitter()
transmitter.sendData("#CMD#GET sensor_state")

# setup gamepad controller
from Controller import Gamepad
gamepad = Gamepad.create(pygame, transmitter)

# setup 3D View and further visualizers
#from Visualizer import View3D
#view3d = View3D(pygame)

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

if __name__ == '__main__':
    main()
