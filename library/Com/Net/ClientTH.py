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

    def __init__(self, _client, _address, _receivers=[]):

        self.logger = LogHandler.getLogger(__name__)
        threading.Thread.__init__(self)
        self.receivers = _receivers
        self.address = _address
        self.receiveSize = 1024
        self.client = _client
        self.receivedData = 0
        self.logger.debug("ClientThread up: Waiting for data...")

    def run(self):

        running = True
        while running:
            data = self.client.recv(self.receiveSize)
            if data:
                dataLen = len(data)
                self.logger.debug("[" + dataLen + "] received: " + str(data))

                self.receivedData += dataLen
                for receiver in self.receivers:
                    receiver.notify("##DATA#" + dataLen + "#" + str(data) +
                                    "##CHECK#" + str(data[7:12]) + "##\n")

            else:
                self.logger.debug("Socket Error: ClientThread closing...")
                self.client.close()
                running = False

    def debugConnection(self):
        res = "Address: " + self.address + " - " + str(self.receivedData + "\n")
        for receiver in self.receivers:
            res += "#RECEIVER#"
        res += "\n"
        self.logger.debug(res)

        return res


def create(_netConf):
    clientTH = ClientTH(_netConf)
    return clientTH
