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

import select
import socket
import sys

from Com.Net import ClientTH


class Listener(object):

    def __init__(self, _netConf):

        self.size = 1024
        self.socket = None
        self.clientThreads = []
        self.netConf = _netConf
        self.listenAdress = self.netConf.listenAdress
        self.listenerPort = self.netConf.listenerPort
        self.logger = LogHandler.getLogger(__name__)

    def isSocketUp(self):
        if self.socket is None:
            return False
        else:
            return True

    def openSocket(self):
        try:
            self.socket = socket.socket()
            self.socket.bind((self.listenAdress, self.listenerPort))
            self.socket.listen(1)
            self.logger.debug("Successfully bound server socket")

        except:
            self.logger.warn("Could not open socket for listening!!!")
            self.socket = None

    def run(self):

        self.open_socket()
        pipes = [self.socket, sys.stdin]
        running = True
        while running:
            inputready, outputready, exceptready = select.select(pipes, [], [])
            for newSocket in inputready:
                if newSocket == self.server:
                    # the selected socket is the server socket and a client
                    # thread is started that accepts there new connections
                    clientThread = ClientTH(self.socket.accept())
                    clientThread.start()
                    self.clientThreads.append(clientThread)

                elif newSocket == sys.stdin:
                    inputLine = sys.stdin.readline()
                    self.logger.debug("READ from STD_IN: " + inputLine)
                    if inputLine == "quit":
                        running = False

        self.socket.close()
        for clientThread in self.clientThreads:
            clientThread.join()


def create(_netConf):
    listener = Listener(_netConf)
    return listener
