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
# Visualizes sensor data on the LED-MAtrix of a SenseHat
# @todo: Assert that all used IO-Operations do not block

#for i in (0, 32, 64, 96, 128, 160, 192, 224, 255):
#    visualizerSensorHat.showLeftThrottleAt(i);
#    visualizerSensorHat.showRightThrottleAt(255-i);

from LoggerFactory import LogHandler
from sense_hat import SenseHat
from math import *


class LedMatrix(object):

    def __init__(self, _senseHat):

        self.logger = LogHandler.getLogger(__name__)
        self.O = (0, 0, 255)
        self.X = (255, 255, 255)
        self.ledMatrix = self.createEmptyMatrix()

        self.senseHat = _senseHat
        self.senseHat.set_rotation(90)
        self.senseHat.clear()

        self.lastLeftThrottle = 0
        self.lastRightThrottle = 0
        self.senseHat.set_pixels(self.ledMatrix)

    def showChar(self, _char='?'):
        self.senseHat.show_letter(_char, [255, 255, 255], [0, 0, 255])

    # Set the pixels on the left side of the LED-Matrix to the given value
    #
    def showLeftThrottleAt(self, _value=0):
        rows = (8 - int(_value / 32))

        #if rows <> self.lastLeftThrottle:
        for i in range(len(self.ledMatrix)):
            if i % 8 < 4:
                if rows <= int(i / 8):
                    self.ledMatrix[i] = self.X
                else:

                    # skip if oldRows <= rows because nothing to clean up
                    self.ledMatrix[i] = self.O

        self.lastLeftThrottle = rows
        self.senseHat.set_pixels(self.ledMatrix)

    # Set the pixels on the right side of the LED-Matrix to the given value
    #
    def showRightThrottleAt(self, _value=0):
        rows = (8 - int(_value / 32))
        for i in range(len(self.ledMatrix)):
            if i % 8 >= 4:
                if rows <= int(i / 8):
                    self.ledMatrix[i] = self.X
                else:
                    self.ledMatrix[i] = self.O

        self.lastRightThrottle = rows
        self.senseHat.set_pixels(self.ledMatrix)

    def createEmptyMatrix(self):
        O = (0, 0, 255)
        emptyMatrix = [O, O, O, O, O, O, O, O,
                       O, O, O, O, O, O, O, O,
                       O, O, O, O, O, O, O, O,
                       O, O, O, O, O, O, O, O,
                       O, O, O, O, O, O, O, O,
                       O, O, O, O, O, O, O, O,
                       O, O, O, O, O, O, O, O,
                       O, O, O, O, O, O, O, O]

        return emptyMatrix

    def hideDisplay(self):
        self.senseHat.ledMatrix = self.createEmptyMatrix()
        self.senseHat.set_pixels(self.senseHat.ledMatrix)
