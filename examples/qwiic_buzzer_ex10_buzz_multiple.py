#!/usr/bin/env python
#-------------------------------------------------------------------------------
# qwiic_buzzer_ex10_buzz_multiple.py
#
# This example shows how to control multiple buzzers.
#
# Be warned, FULL VOLUME can cause your micro to reset.
#
# Note, you must use the "change_address"" example to change the address of your
# second (or third, etc.) buzzers. Here, we are using "0x5B" for the address
# of buzzer2.
#
# It turns each buzzer on and off with their own unique frequencies in a 
# unique pattern.
#-------------------------------------------------------------------------------
# Written by SparkFun Electronics, January 2024
#
# This python library supports the SparkFun Electroncis Qwiic ecosystem
#
# More information on Qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#
# https://www.sparkfun.com/products/24474
#
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

buzzer_1_address = 0x34
buzzer_2_address = 0x5B

def runExample():
	print("\nQwiic Buzzer Example 10 - Buzz Multiple\n")

	# Create instance of device
	my_buzzer1 = qwiic_buzzer.QwiicBuzzer(address = buzzer_1_address)
	my_buzzer2 = qwiic_buzzer.QwiicBuzzer(address = buzzer_2_address)

	# Initialize the device 1
	if my_buzzer1.begin() == False:
		print("The device 1 isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	print("\nQwiic Buzzer 1 ready!")

	# Initialize the device 2
	if my_buzzer2.begin() == False:
		print("The device 2 isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	print("\nQwiic Buzzer 2 ready!")	
	
	# Loop forever
	while True:
		my_buzzer1.configure(my_buzzer1.NOTE_C4, 0, my_buzzer1.VOLUME_MID)
		my_buzzer1.on()

		time.sleep(1)

		my_buzzer2.configure(my_buzzer2.NOTE_E6, 0, my_buzzer2.VOLUME_MID)
		my_buzzer2.on()

		time.sleep(1)		

		my_buzzer1.off()

		time.sleep(1)
		
		my_buzzer2.off()

		time.sleep(1)		

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example")
		sys.exit(0)