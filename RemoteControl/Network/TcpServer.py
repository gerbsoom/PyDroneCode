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


class TcpServer(object):
    """ Sets up TCP Transmitter and Listener to communicate with the drone. """

    def __init__(self, _networkConfig):
        self.logger = LogHandler.getLogger(__name__)
        self.logger.debug("ged")


def create(_networkConfig):
    tcpServer = TcpServer(_networkConfig)
    return tcpServer
