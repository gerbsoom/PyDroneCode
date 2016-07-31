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
# Communicates the generated controller commands to the controlled drone.

from LoggerFactory import LogHandler


class Transmitter(object):
    """ Establishes a TCP connection to the drone and populates commands. """

    def __init__(self):
        self.logger = LogHandler.getLogger(__name__)
        self.logger.debug("ged")
