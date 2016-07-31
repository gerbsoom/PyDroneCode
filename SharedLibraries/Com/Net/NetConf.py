# -*- coding: utf-8 -*-
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
# ______________________________________________________________________________
# Holds the current network configuration which is initially loaded from config.

from LoggerFactory import LogHandler


class NetConf(object):
    """ Holds the current network configuration. """

    def __init__(self):
        self.logger = LogHandler.getLogger(__name__)


def create():
    netConf = NetConf()
    return netConf
