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
# Represents the szene graph containing all created geometrical 1/2/3D-Objects.

from LoggerFactory import LogHandler

from math import *

import Box as Box
import Point as Point
import Surface as Surface


class Model():
    """ Represents the complete szene graph containing all created geometrical
        1/2/3D-Objects and offers some basic object building methods. """

    def __init__(self, _drone=[], _objects=[]):

        self.logger = LogHandler.getLogger(__name__)
        self.logger.debug("Constructing model")
        self.drone = _drone
        self.objects_1D = []
        self.objects_2D = []
        self.objects_3D = []
        # define a preset of initial objects that get added to the scene
        for element in _objects:
            self.addObject(element)

    def setDrone(self, _objects=[]):
        self.drone = []
        for element in _objects:
            self.drone.append(element)
            if isinstance(element, Point.Point):
                self.logger.debug("Add Point to drone " + element.asString())
            elif isinstance(element, Surface.Surface):
                self.logger.debug("Add Surface to drone" + element.asString())
            elif isinstance(element, Box.Box):
                self.logger.debug("Add box to drone " + element.asString())
            else:
                self.logger.warn("No instanceOf-checks succeeded!!!")

    def debugSzeneGraph(self, _onlyDrone=True):
        self.logger.debug("Debugging drone-related model parts")
        for element in self.drone:
            element.asString()

        if not _onlyDrone:
            self.logger.debug("Debugging model parts not containig to drone")
            for element in self.objects_1D:
                self.logger.debug("1D objects:")
                element.asString()
            for element in self.objects_2D:
                self.logger.debug("2D objects:")
                element.asString()
            for element in self.objects_3D:
                self.logger.debug("3D objects:")
                element.asString()

    def getSzeneGraph(self):
        szeneGraph = []
        for element in self.drone:
            szeneGraph.append(element)
        for element in self.objects_1D:
            szeneGraph.append(element)
        for element in self.objects_2D:
            szeneGraph.append(element)
        for element in self.objects_3D:
            szeneGraph.append(element)

        return szeneGraph

    def addObject(self, _object):
        """ Adds the provided Objeckt into the szene """

        if isinstance(_object, Point.Point):
            self.objects_1D.append(_object)
            self.logger.debug("Adding Point " + _object.asString())
        elif isinstance(_object, Surface.Surface):
            self.objects_2D.append(_object)
            self.logger.debug("Adding Surface " + _object.asString())
        elif isinstance(_object, Box.Box):
            self.objects_3D.append(_object)
            self.logger.debug("Adding box " + _object.asString())
        else:
            self.logger.warn("No instanceOf-checks succeeded!!!")

    def rotateObject(self, _object, _rotX=False, _rotY=False, _rotZ=False):
        """ Applies a rotation defined by all provided axis angles.
            Orientational changes get stored in \c rotationAngles.  """

        if not isinstance(_object, Point.Point):
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

        if not isinstance(_object, Point.Point):
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

    def createCube(self, _scaleX=50, _scaleY=50, _scaleZ=50,
                   _basePosX=240, _basePosY=240, _basePosZ=240):
        """ Creates a scalable Cube which can be drawn at the ViewPort """

        Px = _basePosX
        Py = _basePosY
        Pz = _basePosZ
        # scale the base points in 3 dimensions
        # Px = _basePosX + 1.0 * _scaleX
        # Py = _basePosY + 1.0 * _scaleY
        # Pz = _basePosZ + 1.0 * _scaleZ
        # generate the vertex points to define the surfaces with
        # points = [Point.Point(-Px, Py, -Pz), Point.Point(Px, Py, -Pz),
        #          Point.Point(Px, Py, -Pz), Point.Point(-Px, -Py, -Pz),
        #          Point.Point(-Px, Py, Pz), Point.Point(Px, Py, Pz),
        #          Point.Point(Px, -Py, Pz), Point.Point(-Px, -Py, Pz)]
        points = [Point.Point(Px-_scaleX, Py+_scaleY, Pz-_scaleZ), Point.Point(Px+_scaleX, Py+_scaleY, Pz-_scaleZ),
                  Point.Point(Px+_scaleX, Py+_scaleY, Pz-_scaleZ), Point.Point(Px-_scaleX, Py-_scaleY, Pz-_scaleZ),
                  Point.Point(Px-_scaleX, Py+_scaleY, Pz+_scaleZ), Point.Point(Px+_scaleX, Py+_scaleY, Pz+_scaleZ),
                  Point.Point(Px+_scaleX, Py-_scaleY, Pz+_scaleZ), Point.Point(Px-_scaleX, Py-_scaleY, Pz+_scaleZ)]

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
            surfaces.append(Surface.Surface(area, color))

        # construct and return the constructed cube as Box object
        return Box.Box(surfaces)


def create(_drone=[], _objects=[]):
    model = Model(_drone, _objects)
    return model
