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
# This implementation visualizes the orientation in 3D

from LoggerFactory import LogHandler
from math import *


class ViewPort(object):

    def getIdentifier(self):
        return self.identifier

    def __init__(self, _model, _pygameRef, _width=480, height=_320,
                 _id="#", _drawingMode="wire-frame"):

        self.logger = LogHandler.getLogger(__name__)
        self.pygame = _pygameRef
        if self.pygame:
            self.logger.debug("pyGame reference is valid")

        self.identifier = _id + " ViewPort: " + str(_width) + "x" + str(_height)
        self.screen = self.pygame.display.set_mode((_width, _height))
        self.pygame.display.set_caption(self.identifier)
        self.rotationAngles = [0.0, 0.0, 0.0]
        self.screen.fill((159, 182, 205))
        self.drawingMode = _drawingMode

        self.model = _model

        self.logger.debug("ViewPort initialized: " + self.identifier)

    def setDrawingMode(_drawingMode):
        self.drawingMode = _drawingMode

    def renderScene(self):
        """ Renders the complete scene using double-buffering by emptying the
            buffer image (filling everything with the background color) and
            then render all contained objects in the order from far to near. """

        self.screen.fill((159, 182, 205))
        for object in self.model.getSzeneGraph():
            object.draw(self.pygame, self.screen, self.drawingMode)

        self.pygame.display.flip()