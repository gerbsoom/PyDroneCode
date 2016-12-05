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
# __________________________________________________________________________
# Retrieves sensor data from a connected SenseHat device

from LoggerFactory import LogHandler
from sense_hat import SenseHat
from math import *


class SensorHat():

    def __init__(self, _sensorHatConfig):
        self.logger = LogHandler.getLogger(__name__)
        self.config = _sensorHatConfig
        self.sensorHat = SenseHat()

#    def setup(self, _sensorHatConfig):

    def getOrientationDegrees(self):
        orientation = self.sensorHat.get_orientation_degrees()
        self.logger.debug("Orientation_YAW: " + orientation["yaw"])
        self.logger.debug("Orientation_PITCH: " + orientation["pitch"])
        self.logger.debug("Orientation_ROLL: " + orientation["roll"])

        return orientation

    def getYawDegree(self):
        orientation = self.sensorHat.get_orientation_degrees()
        self.logger.debug("Orientation_YAW: " + orientation["yaw"])

        return orientation["yaw"]

    def getPitchDegree(self):
        orientation = self.sensorHat.get_orientation_degrees()
        self.logger.debug("Orientation_PITCH: " + orientation["pitch"])

        return orientation["pitch"]

    def getRollDegree(self):
        orientation = self.sensorHat.get_orientation_degrees()
        self.logger.debug("Orientation_ROLL: " + orientation["roll"])

        return orientation["roll"]

    #def getCompass(self):
        #
    #def getGyroscope(self):
        #
    #def getAcceleration(self):
        #
    #def getOtherSensorData(self):
        #
    #def debugOtherSensorData(self):
        #self.logger.debug("____________________________________")
        #self.logger.debug("||||||||||||||||||||||||||||||||||||")
        #self.logger.debug("|||||| S E N S O R - D A T A |||||||")
        #self.logger.debug("||||||||||||||||||||||||||||||||||||")
        #self.logger.debug("____________________________________")
        #self.logger.debug("////////////////////////////////////")

    def showDebugFrameFor(self, _title, _isHeader=False, _onlyFooter=False):

        if _onlyFooter:
            self.logger.debug("____________________________________")
            self.logger.debug("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        else:
            if _isHeader:
                self.logger.debug("____________________________________")
                self.logger.debug("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
            self.logger.debug("____________________________________")
            self.logger.debug("||||||||||||||||||||||||||||||||||||")
            self.logger.debug(_title)
            self.logger.debug("||||||||||||||||||||||||||||||||||||")
            self.logger.debug("____________________________________")
            self.logger.debug("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

    def debugOrientationSensors(self):

        self.showDebugFrameFor("|||| A C C E L E R O M E T E R |||||", True)
        self.logger.debug(self.senseHat.accelerometer)
        self.logger.debug(self.senseHat.accelerometer_raw)
        self.showDebugFrameFor("|||||| O R I E N T A T I O N |||||||")
        self.logger.debug(self.senseHat.orientation)
        self.logger.debug(self.senseHat.orientation_radians)
        self.showDebugFrameFor("|||||||| G Y R O S C O P E |||||||||")
        self.logger.debug(self.senseHat.gyroscope)
        self.logger.debug(self.senseHat.gyroscope_raw)
        self.showDebugFrameFor("|||||||||| C O M P A S S |||||||||||")
        self.logger.debug(self.senseHat.compass)
        self.logger.debug(self.senseHat.compass_raw)
        self.showDebugFrameFor("||||||||||| ___________", False, True)


def create(_sensorHatConfig):
    return SensorHat(_sensorHatConfig)

