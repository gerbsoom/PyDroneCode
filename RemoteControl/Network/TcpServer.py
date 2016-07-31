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
from Network import Transmitter
from Network import Listener


class TcpServer(object):
    """ Manages a bidirectional communication with the drone. """

    def __init__(self, _networkConfig):

        self.logger = LogHandler.getLogger(__name__)
        self.dataReceiver = []
        self.listerner = Listener.create(_networkConfig)
        self.listener.openSocket()

        self.transmitter = Transmitter.create(_networkConfig)
        self.transmitter.connect()

    def cycle(self):
        if not self.transmitter.connected():
            self.transmitter.connect()

    def getTransmitter(self):
        return self.transmitter

    def addDataReceiver(self, _dataReceiver):
        self.dataReceiver.append(_dataReceiver)


def create(_networkConfig):
    tcpServer = TcpServer(_networkConfig)
    return tcpServer
