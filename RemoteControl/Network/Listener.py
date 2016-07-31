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
# _________________________________________________________________________
# Listens to specific requests from the controlled drone and receives data.

from LoggerFactory import LogHandler

import socketserver


class Listener(socketserver.StreamRequestHandler):
    """ Creates a listener socket and waits for TCP connection of the drone. """

    def __init__(self, _networkConfig):

        self.logger = LogHandler.getLogger(__name__)
        self.logger.debug("Awaiting drone request to change network config")

    def handle(self):
        # self.data = self.rfile.readline().strip()
        self.data = self.rfile.read(100).strip()
        self.logger.debug(self.data)
        self.logger.debug("{} wrote:".format(self.client_address[0]))
        # maybe anser something directly
        # self.wfile.write(self.data.upper())


def create(_networkConfig):
    listener = Listener(_networkConfig)
    return listener
