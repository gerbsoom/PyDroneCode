#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of PyDroneCode.
# Please check the file LICENSE.MD for information about the license.
#
# @file
# @version 0.4
# @copyright 2016 Desmodul
# @author Markus Riegert <desmodul@drow-land.de>
# _____________________________________________________________________
# Manages a listening socket and one to transmit commands to the drone.


from LoggerFactory import LogHandler
from math import *

import ViewPort as ViewPort


class Simulator(object):

    def __init__(self, _pygameRef, _model):

        self.logger = LogHandler.getLogger(__name__)
        self.model = _model
        self.pygame = _pygameRef
        if self.pygame:
            self.logger.debug("pyGame reference is valid")
            self.viewPort = ViewPort.create(self.model, _pygameRef, 480, 320)
            self.logger.debug("Simulator is up and running...")

        self.started = False

    def start(self):
        self.viewPort.renderScene()
        drone = []
        drone.append(self.model.createCube(20, 20, 20, 10, 10, 150))
        self.model.setDrone(drone)
        self.model.addObject(self.model.createCube(50, 50, 50, 250, 250, 250))
        self.started = True
        self.viewPort.renderScene()
        self.model.debugSzeneGraph(False)

    def cycle(self):
        if self.started:
            self.logger.debug("cycling...")
            self.rotateDrone(10, 0.1, 0.01)
            self.viewPort.renderScene()
            self.model.debugSzeneGraph(False)

    def rotateDrone(self, _angleX, _angleY, _angleZ):
        for element in self.model.drone:
            self.model.rotateObject(element, _angleX, _angleY, _angleZ)

    def rotateDroneToDegrees(self, _rotX, _rotY, _rotZ):
        for element in self.model.drone:
            self.model.rotateObjectToDegrees(element, _rotX, _rotY, _rotZ)


def create(_pygameRef, _modelRef):
    simulator = Simulator(_pygameRef, _modelRef)
    return simulator
