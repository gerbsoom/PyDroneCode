# setup pygame
import pygame
from pygame.locals import *
pyGameInit = pygame.init()
logger.info("PyGame version: " + pygame.ver)
logger.debug("-> load " + str(pyGameInit[0]) + " failed " + str(pyGameInit[1]))
# if sys.platform in ('win32', 'cygwin'):
#     time_source = None
# else:
#     time_source = lambda:pygame.time.get_ticks()/1000.

gameClock = pygame.time.Clock()
logger.debug("Initialized the pygame engine.")

# check for keyboard events, maybe allow setting commands from STD_IN
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                running = False

                # get the current orientation over network api and update view with it
            gyro = sensorHat.getOrientationDegrees()
            #simulator3D.rotateCubeToDegrees(360.0 - gyro["pitch"],
            #                                360.0 - gyro["yaw"],
            #                                360.0 - gyro["roll"])
            transmitter.sendData("#DATA#Orientation#" + "%d" % (gyro["pitch"]) + "#" +
                                                        "%d" % (gyro["yaw"]) + "#" +
                                                        "%d" % (gyro["roll"]) + "#")