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

from LoggerFactory import LogHandler

import threading


class ClientTH(threading.Thread):

    def __init__(self, _client, _address):

        self.logger = LogHandler.getLogger(__name__)
        threading.Thread.__init__(self)
        self.address = _address
        self.client = _client
        self.size = 1024
        self.logger.debug("ClientThread up, waiting for data")

    def run(self):

        running = True
        while running:
            data = self.client.recv(self.size)
            if data:
                self.logger.debug("ClientThread received: " + data)
            else:
                self.client.close()
                running = False
