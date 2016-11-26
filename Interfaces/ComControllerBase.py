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
from Com.Net import Transmitter
from Com.Net import Listener


class ComControllerBase(object):
    """ Manages a bidirectional communication with the drone. """

    def __init__(self, _controllerConf):

        self.logger = LogHandler.getLogger(__name__)
        # foreach listeners, create with listernConfig from config list
        self.listener = Listener.create(_controllerConf)
        self.listener.openSocket()
        self.dataReceiver = []
        # foreach transmitters, create with transmitterConfig from config list
        self.transmitter = Transmitter.create(_controllerConf)
        self.transmitter.connect()

    def cycle(self):
        if not self.transmitter.connected():
            self.transmitter.connect()

    def getTransmitter(self):
        return self.transmitter

    def addDataReceiver(self, _dataReceiver):
        self.dataReceiver.append(_dataReceiver)

    def processReceivedCommand(self, _command):
        return _command.execute()


def create(_controllerConf):
    return ComControllerBase(_controllerConf)
