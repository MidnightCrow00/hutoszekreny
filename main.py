#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.nxtdevices import TemperatureSensor                                
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from Hutoszekreny import Huto
# Létrehozzuk az EV3 Brick objektumot
ev3 = EV3Brick()

# Hőmérséklet szenzor inicializálása
ts = TemperatureSensor(Port.S2)

# Initialize the Huto class
oHuto = Huto()

# Run the main function
oHuto.main()

