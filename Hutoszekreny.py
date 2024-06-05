#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.nxtdevices import TemperatureSensor                                
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Huto:
    def __init__(self):
        self.ev3 = EV3Brick()
        self.ts = TemperatureSensor(Port.S2)
        self.elemek = {
            'tej': 3,
            'tojas': 3,
            'vaj': 3
        }
        self.elemek_lista = list(self.elemek.keys())
        self.kivalasztott_index = 0

    def hozza_ad(self, elem):
        self.elemek[elem] += 1
        self.frissit_kijelzo()

    def elvesz(self, elem):
        if self.elemek[elem] > 0:
            self.elemek[elem] -= 1
        self.frissit_kijelzo()

    def keszlet_ellenorzes(self):
        hianyzo_elemek = []
        for elem, mennyiseg in self.elemek.items():
            if mennyiseg == 0:
                hianyzo_elemek.append(elem)
        return hianyzo_elemek

    def frissit_kijelzo(self):
        self.ev3.screen.clear()
        homerseklet = self.ts.temperature()
        self.ev3.screen.print("Hö+: {:.1f}C".format(homerseklet))
        self.ev3.screen.print("Elem: {}".format(self.elemek_lista[self.kivalasztott_index]))
        self.ev3.screen.print("Készlet: {}".format(self.elemek[self.elemek_lista[self.kivalasztott_index]]))

        hianyzo_elemek = self.keszlet_ellenorzes()
        if hianyzo_elemek:
            self.ev3.screen.print("Hiány: {}".format(", ".join(hianyzo_elemek)))

    def main(self):
        self.ev3.speaker.beep()
        self.frissit_kijelzo()

        while True:
            if Button.LEFT in self.ev3.buttons.pressed():
                self.kivalasztott_index = (self.kivalasztott_index - 1) % len(self.elemek_lista)
                self.frissit_kijelzo()
                wait(300)

            if Button.RIGHT in self.ev3.buttons.pressed():
                self.kivalasztott_index = (self.kivalasztott_index + 1) % len(self.elemek_lista)
                self.frissit_kijelzo()
                wait(300)

            if Button.UP in self.ev3.buttons.pressed():
                self.hozza_ad(self.elemek_lista[self.kivalasztott_index])
                wait(300)

            if Button.DOWN in self.ev3.buttons.pressed():
                self.elvesz(self.elemek_lista[self.kivalasztott_index])
                wait(300)

            if Button.CENTER in self.ev3.buttons.pressed():
                break

            wait(100)