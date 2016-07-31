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

import Surface


class Box(object):
    """ Represents a geometrical box in the space and the functionality
        to rotate it by axis and project it on a 2D surface for viewing. """
    def __init__(self, _surfaces):

        self.surfaces = []
        for surface in _surfaces:
            if isinstance(surface, Surface):
                self.surfaces.append(surface)
            else:
                self.surfaces.append(Surface(surface))

        self.rotationAngles = [0.0, 0.0, 0.0]
        self.zIndexAverage = 0
        self.zDirty = True

    def asString(self):

        result = "Box (" + str(len(self.surfaces)) + ")\n -->  "
        for surface in self.surfaces:
            result += surface.asString() + "\n"

        return result + "]"

    def rotateX(self, _angle):
        """ Rotates the underlying surface group representing a cube in
            the space around the X axis by the given angle in degrees. """

        self.zDirty = True
        rotatedSurfaces = []
        for surface in self.surfaces:
            rotatedSurfaces.append(surface.rotateX(_angle))

        self.rotationAngles[0] += _angle

        return Box(rotatedSurfaces)

    def rotateY(self, _angle):
        """ Rotates the underlying surface group representing a cube in
            the space around the Y axis by the given angle in degrees. """

        self.zDirty = True
        rotatedSurfaces = []
        for surface in self.surfaces:
            rotatedSurfaces.append(surface.rotateY(_angle))

        self.rotationAngles[1] += _angle

        return Box(rotatedSurfaces)

    def rotateZ(self, _angle):
        """ Rotates the underlying surface group representing a cube in
            the space around the Z axis by the given angle in degrees. """

        self.zDirty = True
        rotatedSurfaces = []
        for surface in self.surfaces:
            rotatedSurfaces.append(surface.rotateZ(_angle))

        self.rotationAngles[2] += _angle

        return Box(rotatedSurfaces)

    def getAverageZ(self):
        """ Calculates the average depth index Z of all contained surfaces. """

        if self.zDirty:
            dividor = 0
            self.zIndexAverage = 0
            for surface in self.surfaces:
                dividor += 1
                self.zIndexAverage += surface.getAverageZ
            if dividor > 0:
                self.zIndexAverage /= dividor
            self.zDirty = False

        return self.zIndexAverage

    def draw(self, _pyGameRef, _screen, _drawMode="wire-frame"):
        """ Draws the contained surfaces of the underlying cube on the
            provided screen which is assumed to be blanked before.
            The calling code is responsible for updating the screen after
            the scene is rendered completely. The algorithm firstly draws
            the surfaces with the heighest depth. """

        for surface in self.surfaces:
            surface.project().draw(_pyGameRef, _screen, _drawMode)
