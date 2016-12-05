PyDroneCode
===========

The python-related part of a framework to (remote) control and visualize the flight of a physical drone device.
Parts of the (Py-)DroneCode also resists on the flying device and can be loaded by the drone once it is needed.
Initially the project was strictly split up into its both main parts: 'RemoteController' and 'DroneDevice'.

This separation resulted in a lot of duplicated functionality to see for example in the runner apps (V 0.3).
After the last re-factoring, there is only one configurable runner left which is able to run everything. 
Redundant parts in the code, commands, config and objects got abstracted and integrated in shared libs.

Python Remote Control:
======================

Python Flight System:
=====================
