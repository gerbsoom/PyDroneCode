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


class ComListenerBase(object):
    """ Listener base class forces the existence of specific methods"""

    def __init__(self, _controller, _listenerConf):
        """ Constructs the Event Listener from the provided config"""
        self.logger = LogHandler.getLogger(__name__)
        self.listenerConf = _listenerConf
        self.controller = _controller
        self.isListening = False

    def cycle(self):
        """ Cyclically check for available Events on non-blocking sources """
        #if self.isListening :
            # check all configured sources for new Events

    def listen(self):
        """ Activates the Listener to retrieve and process Events """
        self.isListening = True

    def stopListening(self):
        """ Stops the Listener from recieving Events """
        self.isListening = False
        return self.isListening()

    def isListening(self):
        """ Returns if the Listener is activated """
        return self.isListening

    def onCommandReceived(self, _recievedCommand):
        """ Triggered on Events from a blocking source """
        self.controller.processCommand(_recievedCommand)


def create(_listenerConf):
    """ Creation helper """
    return ComListenerBase(_listenerConf)
