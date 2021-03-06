#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of PyDroneCode.
# Please check the file LICENSE.MD for information about the license.
#
# @file
# @version 0.4
# @copyright 2016 Desmodul
# @author Markus Riegert <desmodul@drow-land.de>
# ______________________________________________________________________________
# This implementation visualizes the orientation in 3D

from LoggerFactory import LogHandler
from math import *


class ViewPort(object):

    def getIdentifier(self):
        return self.identifier

    def __init__(self, _model, _pygameRef, _width=480, _height=320,
                 _drawingMode="color-surface"):

        self.logger = LogHandler.getLogger(__name__)
        self.pygame = _pygameRef
        if self.pygame:
            self.logger.debug("pyGame reference is valid")

        self.identifier = "screen:[" + str(_width) + "x" + str(_height) + "]"
        self.screen = self.pygame.display.set_mode((_width, _height),
                                                   self.pygame.DOUBLEBUF|self.pygame.HWSURFACE)
        self.pygame.display.set_caption(self.identifier)
        self.gameClock = self.pygame.time.Clock()
        self.rotationAngles = [0.0, 0.0, 0.0]
        self.screen.fill((159, 182, 205))
        self.drawingMode = _drawingMode
        self.model = _model

        self.logger.debug("ViewPort initialized: " + self.identifier)

    def setDrawingMode(self, _drawingMode):
        self.drawingMode = _drawingMode

    def renderScene(self):
        """ Renders the complete scene using double-buffering by emptying the
            buffer image (filling everything with the background color) and
            then render all contained objects in the order from far to near. """

        self.screen.fill((159, 182, 205))
        self.logger.debug("Drawing scene")
        # self.screen.render(str(self.gameClock.get_fps() + " fps")
        self.pygame.display.set_caption(self.identifier + " (" + str(self.gameClock.get_fps()) + " fps)")
        for element in self.model.getSzeneGraph():
            self.logger.debug("Drawing element" + element.asString())
            element.draw(self.pygame, self.screen, self.drawingMode)

        self.pygame.display.flip()


def create(_model, _pygameRef, _width=480, _height=320, _drawMode="color-surface"):
    viewPort = ViewPort(_model, _pygameRef, _width, _height, _drawMode)

    return viewPort
