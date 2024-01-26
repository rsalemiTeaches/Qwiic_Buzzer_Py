#!/usr/bin/env python
#-------------------------------------------------------------------------------
# qwiic_buzzer_ex3_buzz_duration.py
#
# This example shows how to control the buzzer using frequency and duration.
#
# This example shows how to turn the buzzer on and off.
# Much like the classic "blink LED sketch" this will buzz
# the buzzer once every second.
#-------------------------------------------------------------------------------
# Written by SparkFun Electronics, January 2024
#
# This python library supports the SparkFun Electroncis Qwiic ecosystem
#
# More information on Qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#===============================================================================
# Copyright (c) 2023 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#===============================================================================

import qwiic_buzzer
import sys
import time

def runExample():
	print("\nQwiic Buzzer Example 3 - Buzz Duration\n")

	# Create instance of device
	my_buzzer = qwiic_buzzer.QwiicBuzzer()

	# Initialize the device
	if my_buzzer.begin() == False:
		print("The device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	print("\nQwiic Buzzer ready!")
	
	# Loop forever
	while True:
		my_buzzer.configure(2730, 100) # frequency: 2.73KHz, duration: 100ms
		my_buzzer.on()
		time.sleep(1)     

		my_buzzer.configure(1000, 500) # frequency: 1K, duration: 500ms
		my_buzzer.on()
		time.sleep(1)  

		# Note, we dont' have to call buzzer.off(), because it will automatically turn
		# off after the duration of each tone is completed.

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example")
		sys.exit(0)