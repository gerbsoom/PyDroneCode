#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of PyDroneCode.
# Please check the file LICENSE.MD for information about the license.
#
# @file
# @version 0.3
# @copyright 2016 Desmodul
# @author Markus Riegert <desmodul@drow-land.de>
# ______________________________________________________________________________

import math


class Point:
    """ Represents a geometrical point in the space and the functionality
        to rotate it by axis and project it on a 2D surface for viewing.
        @toDo: Replace the sinus-calculations with matrix-rotations. """

    def __init__(self, _x=0.0, _y=0.0, _z=0.0):

        self.x = float(_x)
        self.y = float(_y)
        self.z = float(_z)

    def rotateX(self, _angle):
        """ Rotates the underlying 3-dimensional vector representing a point
            in the space around the X axis by the given angle in degrees.
            @toDo: Replace the sinus-calculations with matrix-rotations. """

        rad = _angle * math.pi / 180
        cosA = math.cos(rad)
        sinA = math.sin(rad)
        y = self.y * cosA - self.z * sinA
        z = self.y * sinA + self.z * cosA

        return Point(self.x, y, z)

    def rotateY(self, _angle):
        """ Rotates the underlying 3-dimensional vector representing a point
            in the space around the Y axis by the given angle in degrees.
            @toDo: Replace the sinus-calculations with matrix-rotations. """

        rad = _angle * math.pi / 180
        cosA = math.cos(rad)
        sinA = math.sin(rad)
        z = self.z * cosA - self.x * sinA
        x = self.z * sinA + self.x * cosA

        return Point(x, self.y, z)

    def rotateZ(self, _angle):
        """ Rotates the underlying 3-dimensional vector representing a point
            in the space around the Z axis by the given angle in degrees.
            @toDo: Replace the expensive sinus-calculations by a matrix-
                   rotation or a quaternion-rotatione """
        rad = _angle * math.pi / 180
        cosA = math.cos(rad)
        sinA = math.sin(rad)
        x = self.x * cosA - self.y * sinA
        y = self.x * sinA + self.y * cosA

        return Point(x, y, self.z)

    def project(self, _width, _height, _fov=192, _dist=8):
        """ Transforms the underlying 3-dimensional vector representing a point
            in the space by the shortly explained perspective projection:
            fov (field of vision): works good in the range (128, 256)
            Good mapping if the object is in front of the viewer,
            not too near and big enough """

        factor = _fov / (_dist + self.z)
        x = self.x * factor + _width / 2
        y = -self.y * factor + _height / 2

        return Point(x, y, self.z)

    def asVector(self):
        """ Returns the 3D point in a vector representation """

        return (self.x, self.y, self.z)

    def asString(self):
        """ Returns a short string representation for debuggin purposes. """
        point = str(self.x) + "," + str(self.Y) + "," + str(self.z)

        return str("Pxyz=(" + point + ")")
