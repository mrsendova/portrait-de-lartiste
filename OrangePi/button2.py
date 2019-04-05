# coding: utf-8
#test

import orangepi.one
from OPi import GPIO

# Orange Pi One physical board pin to GPIO pin
GPIO.setmode(orangepi.one.BOARD)

GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while GPIO.input(40) == GPIO.LOW:
    time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things

print("Hourra")
