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

import Point as Point


class Surface(object):
    """ Represents a geometrical surface in the space and the functionality
        to rotate it by axis and project it on a 2D surface for viewing. """

    def __init__(self, _vertices, _color=(88, 88, 88)):

        self.zDirty = True
        self.color = _color
        self.zIndexAverage = 0
        self.rotationAngles = [0.0, 0.0, 0.0]

        self.points = []
        for vertice in _vertices:
            if isinstance(vertice, Point):
                self.points.append(vertice)
            elif isinstance(vertice, Point.Point):
                self.points.append(vertice)
            else:
                self.points.append(Point.Point(vertice.x, vertice.y, vertice.z))

    def asString(self):
        result = "Surface (" + str(len(self.points)) + ") -->  "
        for point in self.points:
            result += point.asString()
        return result + "]"

    def rotateX(self, _angle):
        """ Rotates the underlying 3D vector group representing a surface in
            the space around the X axis by the given angle in degrees. """

        self.zDirty = True
        rotatedPoints = []
        for point in self.points:
            rotatedPoints.append(point.rotateX(_angle))

        self.rotationAngles[0] += _angle

        return Surface(rotatedPoints, self.color)

    def rotateY(self, _angle):
        """ Rotates the underlying 3D vector group representing a surface in
            the space around the Y axis by the given angle in degrees. """

        self.zDirty = True
        rotatedPoints = []
        for point in self.points:
            rotatedPoints.append(point.rotateY(_angle))

        self.rotationAngles[1] += _angle

        return Surface(rotatedPoints, self.color)

    def rotateZ(self, _angle):
        """ Rotates the underlying 3D vector group representing a surface in
            the space around the Z axis by the given angle in degrees. """

        self.zDirty = True
        rotatedPoints = []
        for point in self.points:
            rotatedPoints.append(point.rotateZ(_angle))

        self.rotationAngles[2] += _angle

        return Surface(rotatedPoints, self.color)

    def project(self, _width=480, height=320, _fov=192, _dist=8):
        """ Transforms the 3D surface to 2D using a perspective projection. """

        self.zDirty = True
        projectedPoints = []
        for point in self.points:
            projectedPoints.append(point.project(_width, height, _fov, _dist))

        return Surface(projectedPoints, self.color)

    def getAverageZ(self):
        """ Calculates the average depth index Z of all contained vertices. """

        if self.zDirty:
            dividor = 0
            self.zIndexAverage = 0
            for point in self.points:
                dividor += 1
                self.zIndexAverage += point.z
            if dividor > 0:
                self.zIndexAverage /= dividor
            self.zDirty = False

        return self.zIndexAverage

    def asPolygon(self):

        polygon = []
        for point in self.points:
            polygon.append((point.x, point.y))

        return polygon

    def draw(self, _gameRef, _screen, _drawMode, _color=(-1, -1, -1)):
        """ Draws the contained surface on the provided references which are
            assumed to be blanked before to not mess up the render logic.
            The calling code is responsible for applying all transformations
            completely over the 3D scene and to flip in the rendered scene. """

        if _color == (-1, -1, -1):
            color = self.color
        else:
            color = _color

        if _drawMode == "wire-frame":
            color = (255, 255, 255)

            iterator = 0
            first = 0
            for point in self.points:
                # skip first round with only one point
                if not iterator:
                    iterator = point
                    first = point
                else:
                    _gameRef.draw.line(_screen, color, (iterator.x, iterator.y),
                                                       (point.x, point.y))
                    iterator = point

            if iterator and first:
                _gameRef.draw.line(_screen, color, (iterator.x, iterator.y),
                                                   (first.x, first.y))

        elif _drawMode == "color-surface":
            _gameRef.draw.polygon(_screen, color, self.asPolygon())
