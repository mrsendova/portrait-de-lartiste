# coding: utf-8

# Code basé sur les sources suivantes:
# - https://engineersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
# - https://www.instructables.com/id/Interface-Python-and-Arduino-with-pySerial/


from time import sleep
import serial

ser = serial.Serial('/dev/ttyACM0') #Établir la connection
ser.flushInput()

while True:
    try:
        ligne = unicode(ser.readline().strip('\n').strip('\r'))
    except:
        print("Keyboard Interrupt")

    if (len(ligne.split(";")) == 13):
        print(ligne.split(";"))
        break
