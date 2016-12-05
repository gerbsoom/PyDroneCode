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

# ____________________________________________________________________________
# Starts the Application DroneDevice (IFS) which takes control over the drone.

from LoggerFactory import LogHandler
from Com.Net import Server
# from Com.Output.Display import LedMatrix
# from Com.Input.Sensor import SensorHat

import time


class DroneDevice(object):

    def __init__(self, _droneConfig):
        self.logger = LogHandler.getLogger(__name__)
        self.config = _droneConfig
        self.loop = 0
        self.server = 0
        self.emitter = 0
        self.ledMatrix = 0
        self.sensorHat = 0
        self.transmitter = 0
        #for section in self.config.sections(_droneConfig):
        #    for (key, value) in self.config.items(_droneConfig):
         #       self.logger.debug("EventLoop: [" + key + "] => " + str(value))

    def run(self):
        running = True
        while running:
            # cycle the TcpServer for new Events or messages
            # self.server.cycle()
            time.sleep(1)

    def setupNetwork(self, _networkSection):
        self.logger.debug("Setting up Network...")
        # self.server = Server.create(_networkSection)
        # self.transmitter = self.server.getTransmitter()
        self.logger.info("Network Server is up and running")
        # transmitter.sendData("#CMD#" + "GET sensor_state")

    def setupEventLoop(self, _eventLoopSection):
        self.logger.debug("Setting up EventLoop...")
        for (key, value) in self.config.items(_eventLoopSection):
            self.logger.debug("EventLoop: [" + key + "] => " + str(value))

    def setupEmitter(self, _emitterSection):
        self.logger.debug("Setting up EventEmitter...")
        for (key, value) in self.config.items(_emitterSection):
            self.logger.debug("EventEmitter: [" + key + "] => " + str(value))

    def setupSensorHat(self, _sensorHatSection):
        self.logger.debug("Setting up SensorHat...")
        for (key, value) in self.config.items(_sensorHatSection):
            self.logger.debug("SensorHat: [" + key + "] => " + str(value))

    def setupLedMatrix(self, _ledMatrixtSection):
        self.logger.debug("Setting up LedMatrix...")
        for (key, value) in self.config.items(_ledMatrixtSection):
            self.logger.debug("LedMatrix: [" + key + "] => " + str(value))

    def setup(self):
        for section in self.config.sections():
            if section.name == "network":
                self.setupNetwork(section)
            elif section.name == "sensorhat":
                self.setupSensorHat(section)
            elif section.name == "ledmatrix":
                self.setupLedMatrix(section)
            elif section.name == "EventLoop":
                self.setupEventLoop(section)
            elif section.name == "Emitter":
                self.setupEmitter(section)

        return True


def create(_droneConfig):
    return DroneDevice(_droneConfig)
