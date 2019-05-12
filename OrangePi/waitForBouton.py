# coding: utf-8

import time, os
from pyA20.gpio import gpio
from pyA20.gpio import port

r = 0


def initiatePin(): #Initialiser les GPIO
	gpio.init()
	pin = port.PG6

	gpio.setcfg(pin, gpio.OUTPUT)
	gpio.input(pin)

	gpio.setcfg(pin, 0)
	gpio.pullup(pin, 0)
	gpio.pullup(pin, gpio.PULLDOWN)
	gpio.pullup(pin, gpio.PULLUP)

def buttonState(): #Retourne l'état de la pin
	return gpio.input(port.PG6)

initiatePin() # beginning of script, enable the GPIO pin.


try:
    while (r == 0):
        if buttonState() == 1:
            print "Bouton appuyé"
            r = 1

        time.sleep(0.1)
except Exception as e:
    raise
