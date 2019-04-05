# coding: utf-8

import time, os
from pyA20.gpio import gpio
from pyA20.gpio import port

def initiatePin(): #Enable a pin

	gpio.init()
	pin = port.PG7

	gpio.setcfg(pin, gpio.OUTPUT)
	gpio.input(pin)

	gpio.setcfg(pin, 0)
	gpio.pullup(pin, 0)
	gpio.pullup(pin, gpio.PULLDOWN)
	gpio.pullup(pin, gpio.PULLUP)

def buttonState(): #Get the state of the button. Is it high or low?
	buttonStateValue = gpio.input(port.PG7)
	if buttonStateValue == 0:
		buttonStateString = 'Low'
	elif buttonStateValue == 1:
		buttonStateString = "High"
	return buttonStateValue, buttonStateString

initiatePin() # beginning of script, enable the GPIO pin.


while True: # Constantly check for the state of the button
	print "Button Value: %s" % buttonState()[0]
	print "Button is: %s" % buttonState()[1] #debug

	if buttonState()[0] == 0:
		print "Do Nothing..."
		pass # if door closed, do nothing.
	elif buttonState()[0] == 1:
		print "Shut Down Computer!"
		#os.system('sudo shutdown')
	print "\n"
time.sleep(1)
