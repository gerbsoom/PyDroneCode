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
# _______________________________________________________________________
# A pygame-based EventHandler which is able to handle gamepad controller.

from LoggerFactory import LogHandler


class Gamepad(object):

    def __init__(self, _pygameRef, _transmitter, _gamepadConfig=False):
        self.hysteresis = 0.1
        self.logger = LogHandler.getLogger(__name__)
        self.lastThrottleValues = [0.0, 0.0, 0.0, 0.0]
        self.lastPressedButtons = [0, 0, 0, 0, 0, 0, 0, 0,
                                   0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.gamepadConfig = _gamepadConfig
        self.transmitter = _transmitter
        self.pygame = _pygameRef
        if self.pygame:
            self.logger.debug("PyGame reference is valid")
            self.gamepad = 0

    def deviceInitialized(self):
        if self.gamepad:
            return True
        else:
            return False

    def initDevice(self):
        if not self.gamepad:

            numDev = self.pygame.joystick.get_count()
            self.logger.debug(str(numDev) + " control devices available.")
            for i in range(numDev):
                device = self.pygame.joystick.Joystick(i)
                name = device.get_name()
                self.logger.debug("Current device: " + name)
                self.debugDevice(device)
                try:
                    device.init()
                    self.gamepad = device
                    self.logger.info("Device successfully initialized.")
                except:
                    self.logger.info("Error initializing control device!!!")

    def cycle(self):
        if self.deviceInitialized():
            self.processPressedButtons()
            self.processThrottleValues()
        else:
            self.initDevice()

    def processPressedButtons(self):

        for i in range(0, self.gamepad.get_numbuttons()):
            if self.gamepad.get_button(i):
                if self.lastPressedButtons[i] == 0:
                    self.lastPressedButtons[i] = 1
                    self.logger.debug("Button [" + str(i) + "] pressed")
            else:
                if self.lastPressedButtons[i]:
                    self.lastPressedButtons[i] = 0
                    self.logger.debug("Button [" + str(i) + "] released")

    def processThrottleValues(self):
        throttles = [self.gamepad.get_axis(0),
                     self.gamepad.get_axis(1),
                     self.gamepad.get_axis(2),
                     self.gamepad.get_axis(3)]

        for i in range(0, 4):
            if abs(self.lastThrottleValues[i] - throttles[i]) > self.hysteresis:
                self.lastThrottleValues[i] = throttles[i]
                if i == 0 or i == 1:
                    self.transmitter.sendData("#CMD#LT=" +
                                              str(throttles[i] * 128 + 128) +
                                              "#")
                elif i == 2 or i == 3:
                    self.transmitter.sendData("#CMD#RT=" +
                                              str(throttles[i] * 128 + 128) +
                                               "#")

                self.logger.debug("Axis [" + str(i) + "]->" + str(throttles[i]))

    def debugDevice(self, _gamepad):
        self.logger.debug("Buttons: " + str(_gamepad.get_numbuttons()))
        self.logger.debug("Axis: " + str(_gamepad.get_numaxes()))


def create(_pygameRef, _transmitter, _gamepadConfig=False):
    gamepad = Gamepad(_pygameRef, _transmitter, _gamepadConfig)
    return gamepad
