# coding: utf-8

# Code basé sur les sources suivantes:
# - https://engineersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
# - https://www.instructables.com/id/Interface-Python-and-Arduino-with-pySerial/


from time import sleep
import serial
import regex

ser = serial.Serial('/dev/ttyACM1') #Établir la connection
ser.flushInput()

while True:
    try:
        rawdata = ser.readline().strip('\n').strip('\r')
        data = regex.split(";", rawdata)
        print(data)

    except:
        print("Keyboard Interrupt")
        break
