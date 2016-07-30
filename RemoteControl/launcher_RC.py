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
sys.path.insert(0, '/home/pi/Desktop/DEV/gitdirs/PyDroneCode/SharedLibraries')
from LoggerFactory import LogHandler 
logger = LogHandler.getLogger("Launcher", "_log.conf")

import pygame
from pygame.locals import *
pygame.init()
gameClock = pygame.time.Clock()

# setup network server
# --> listen to port 21023 for remote control initialization
# --> query initial sensor state in a non-emergency scenario

#from GamepadController import GamepadController
#gamepadController = GamepadController(pygame)
# connect network/visualizer callbacks or use event emitting

# try/catch or check if X available
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
    #gamepadController.doCycle()

    # get the current orientation over network api and update view with it
    #gyro = sensorSenseHat.getOrientationDegrees()
    #simulator3D.rotateCubeToDegrees(360.0 - gyro["pitch"],
    #                                360.0 - gyro["yaw"],
    #                                360.0 - gyro["roll"])
    gameClock.tick(50)

if __name__ == '__main__':
    main()
