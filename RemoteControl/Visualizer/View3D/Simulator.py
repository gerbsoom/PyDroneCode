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
# _____________________________________________________________________
# Manages a listening socket and one to transmit commands to the drone.


from LoggerFactory import LogHandler
from math import *

import Model
import ViewPort

class Simulator(object):

    def __init__(self, _pygameRef):

        self.logger = LogHandler.getLogger(__name__)
        self.pygame = _pygameRef
        if self.pygame:
            self.logger.debug("pyGame reference is valid")

        self.model = Model.Model()
        self.viewPort = ViewPort.ViewPort(self.model, _pygameRef,
                                          480, 320, "Simulator")

        self.logger.debug("Simulator is up and running...")
        self.started = False

    def start(self):
        self.started = True
        drone = []
        drone.append(self.model.createCube())
        self.model.setDrone(drone)

    def cycle(self):
        if self.started:
            self.rotateDrone(self, _angleX=0.0001)
            self.viewPort.renderScene()

    def rotateDrone(self, _angleX, _angleY, _angleZ):
        for object in self.model.drone:
            self.model.rotateObject(object, _angleX, _angleY, _angleZ)

    def rotateDroneToDegrees(self, _rotX, _rotY, _rotZ):
        for object in self.model.drone:
            self.model.rotateObjectToDegrees(object, _rotX, _rotY, _rotZ)


def create(_pygameRef):
    simulator = Simulator(_pygameRef)
    return simulator
