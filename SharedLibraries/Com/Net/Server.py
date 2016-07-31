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


class Server(object):
    """ Manages a bidirectional communication with the drone. """

    def __init__(self, _netConf):

        self.logger = LogHandler.getLogger(__name__)
        self.listener = Listener.create(_netConf)
        self.listener.openSocket()
        self.dataReceiver = []

        self.transmitter = Transmitter.create(_netConf)
        self.transmitter.connect()

    def cycle(self):
        if not self.transmitter.connected():
            self.transmitter.connect()

    def getTransmitter(self):
        return self.transmitter

    def addDataReceiver(self, _dataReceiver):
        self.dataReceiver.append(_dataReceiver)


def create(_netConf):
    server = Server(_netConf)
    return server
