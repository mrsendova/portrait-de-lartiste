# coding: utf-8

# Code basé sur la source suivante:
# - https://stackoverflow.com/a/40531041

import serial
import serial.tools.list_ports


def getFirstDevice():
    ports = serial.tools.list_ports.comports(1)
    devices = []

    for p in ports:
        if ('Arduino' in p.manufacturer):
            devices.append(str(p.device))

    try:
        return devices[0]
        pass
    except Exception as e:
        raise
