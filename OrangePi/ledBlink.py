#coding: utf-8

# Code trouvé à l'adresse suivante:
# https://diyprojects.io/orange-pi-onelite-tutorial-use-gpio-python-pinouts/


#import the library / Import des librairies
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep

delay = 0.2

#initialize the gpio module / initialise le GPIO
gpio.init()

#setup the port (same as raspberry pi's gpio.setup() function)
#Configure la broche PG7 (equivalent au GPIO21 du Raspberry) comme une sortie
gpio.setcfg(port.PG7, gpio.OUTPUT)

try:
    while True:
        gpio.output(port.PG7, gpio.HIGH)
        print("High")
        sleep(delay)
        gpio.output(port.PG7, gpio.LOW)
        print("Low")
        sleep(delay)
except KeyboardInterrupt:
    gpio.output(port.PG7, gpio.LOW)
    print("Low")
