# coding: utf-8


import getArduinoPort

try:
    print(getArduinoPort.getFirstDevice())
    pass
except Exception as e:
    print("No device found")
