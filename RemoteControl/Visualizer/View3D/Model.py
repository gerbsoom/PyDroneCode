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
# Represents the szene graph containing all created geometrical 1/2/3D-Objects.

from LoggerFactory import LogHandler

from math import *

import Box
import Point
import Surface


class Model():
    """ Represents the complete szene graph containing all created geometrical
        1/2/3D-Objects and offers some basic object building methods. """

    def __init__(self, _drone=[], _objects=[]):
        super(Box, self).__init__(_objects)

        self.logger = LogHandler.getLogger(__name__)
        self.drone = _drone
        self.objects_1D = []
        self.objects_2D = []
        self.objects_3D = []
        # define a preset of initial objects that get added to the scene
        for object in _objects:
            self.addObject(object)

    def setDrone(_objects=[]):
        self.drone = _objects

    def getSzeneGraph():
        objects = []
        objects.append(self.drone)
        objects.append(self.objects_1D)
        objects.append(self.objects_2D)
        objects.append(self.objects_3D)

        return objects

    def addObject(self, _object):
        """ Adds the provided Objeckt into the szene """

        if isinstance(_object, Point):
            self.objects_1D.append(_object)
            self.logger.debug("Adding Point " + _object.asString())
        elif isinstance(_object, Surface):
            self.objects_2D.append(_object)
            self.logger.debug("Adding Surface " + _object.asString())
        elif isinstance(_object, Box):
            self.objects_3D.append(_object)

    def rotateObject(self, _object, _rotX=False, _rotY=False, _rotZ=False):
        """ Applies a rotation defined by all provided axis angles.
            Orientational changes get stored in \c rotationAngles.  """

        if not isinstance(_object, Point):
            if _rotX:
                _object = _object.rotateX(_rotX)
                _object.rotationAngles[0] += _rotX
            if _rotY:
                _object = _object.rotateY(_rotY)
                _object.rotationAngles[1] += _rotY
            if _rotZ:
                _object = _object.rotateZ(_rotZ)
                _object.rotationAngles[2] += _rotZ

    def rotateObjectToDegrees(self, _object, _angleX, _angleY, _angleZ):
        """ Calculates a rotation which sets all requested axis angles.
            Current orientation angles are stored in rotationAngles.  """

        if not isinstance(_object, Point):
            if _angleX > _object.rotationAngles[0]:
                needRotationX = _angleX - _object.rotationAngles[0]
            else:
                needRotationX = _object.rotationAngles[0] - _angleX

            if _angleY > _object.rotationAngles[1]:
                needRotationY = _angleY - _object.rotationAngles[1]
            else:
                needRotationY = _object.rotationAngles[1] - _angleY

            if _angleZ > _object.rotationAngles[2]:
                needRotationZ = _angleZ - _object.rotationAngles[2]
            else:
                needRotationZ = _object.rotationAngles[2] - _angleZ

            _object.rotateObject(needRotationX, needRotationY, needRotationZ)

    def createCube(self, _scaleX=25, _scaleY=25, _scaleZ=25,
                   _basePosX=240, _basePosY=160, _basePosZ=50):
        """ Creates a scalable Cube which can be drawn at the ViewPort """

        # scale the base points in 3 dimensions
        Px = _basePosX + 1.0 * _scaleX
        Py = _basePosY + 1.0 * _scaleY
        Pz = _basePosZ + 1.0 * _scaleZ

        # generate the vertex points to define the surfaces with
        points = [Point(-Px, Py, -Pz), Point(Px, Py, -Pz),
                  Point(Px, Py, -Pz), Point(-Px, -Py, -Pz),
                  Point(-Px, Py, Pz), Point(Px, Py, Pz),
                  Point(Px, -Py, Pz), Point(-Px, -Py, Pz)]

        # construct all cube surfaces from these areas raw data
        areaData = [(points[0], points[1], points[2], points[3]),
                    (points[1], points[5], points[6], points[2]),
                    (points[5], points[4], points[0], points[3]),
                    (points[4], points[0], points[3], points[7]),
                    (points[0], points[4], points[5], points[1]),
                    (points[3], points[2], points[6], points[7])]

        # give all surfaces a slightly different color
        baseValue = 42
        multiplicator = 0
        surfaces = []
        for area in areaData:
            multiplicator += 1
            colorValue = multiplicator * baseValue
            color = (colorValue, colorValue, colorValue)
            surfaces.append(Surface(area, color))

        # construct and return the constructed cube as Box object
        return Box(surfaces)
