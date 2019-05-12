#!/usr/bin/python
# coding: utf-8

import time, os
from pyA20.gpio import gpio
from pyA20.gpio import port
import smbus

r = 0
# Define some device parameters
I2C_ADDR  = 0x27 # I2C device address
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

#Open I2C interface
bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
#bus = smbus.SMBus(1) # Rev 2 Pi uses 1

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)


def initiatePin():
    gpio.init()
    pin = port.PG7
    pin2 = port.PG6

    gpio.setcfg(pin, gpio.OUTPUT)
    gpio.input(pin)

    gpio.setcfg(pin2, gpio.OUTPUT)
    gpio.input(pin2)

    gpio.setcfg(pin, 0)
    gpio.pullup(pin, 0)
    gpio.pullup(pin, gpio.PULLDOWN)
    gpio.pullup(pin, gpio.PULLUP)

    gpio.setcfg(pin2, 0)
    gpio.pullup(pin2, 0)
    gpio.pullup(pin2, gpio.PULLDOWN)
    gpio.pullup(pin2, gpio.PULLUP)

def buttonState(): #Retourne l'état de la pin
	return gpio.input(port.PG7)

def sState(): #Retourne l'état de la pin
	return gpio.input(port.PG6)

initiatePin() # beginning of script, enable the GPIO pin.


try:
    lcd_init()
    lcd_string("Portrait v0.2.5  ",LCD_LINE_1)
    lcd_string("0x0> Pret",LCD_LINE_2)

    while (r == 0):
        if buttonState() == 1:
            print "Bouton appuyé"
            lcd_string("0x1> Btn appuye",LCD_LINE_2)
            time.sleep(1)
            lcd_string("0x2>On calcule...",LCD_LINE_2)
            time.sleep(1)

            if sState() == 1:
                lcd_string("0x3> Cher.",LCD_LINE_2)
                time.sleep(2)
            else:
                lcd_string("0x3> Pas cher.",LCD_LINE_2)
                time.sleep(3)
        lcd_string("0x0> Pret",LCD_LINE_2)
        time.sleep(0.1)
except Exception as e:
    raise
