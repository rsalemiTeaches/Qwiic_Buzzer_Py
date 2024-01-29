#!/usr/bin/env python
#-------------------------------------------------------------------------------
# qwiic_buzzer_ex5_change_address.py
#
# Demonstrates how to change the address of the Qwiic Buzzer
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

# The default address is 0x34, change this if your buzzer currently has a different address!
initial_address = qwiic_buzzer.QwiicBuzzer.DEFAULT_ADDRESS

def runExample():
	print("\nQwiic Buzzer Example 5 - Change Address\n")

	# Create instance of device
	my_buzzer = qwiic_buzzer.QwiicBuzzer(address=initial_address)

	# Initialize the device
	if my_buzzer.begin() == False:
		print("The device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	print("\nQwiic Buzzer ready!")

	# Repeat until the address has been successfully changed
	addressChanged = False
	while not addressChanged:
		# Print instructions
		print()
		print("Please enter a new address for the sensor.")
		print("Any value between 0x08 and 0x77 is valid.")
		print("Enter the address in hexadecimal without the `0x`.")
		print()

		# Read input from user
		newAddress = input("New address: ")

		try:
			# Parse input using int() function
			newAddress = int(newAddress, 16)

			print("Parsed address:", hex(newAddress))

			# Check if the address is valid
			if newAddress < 0x08 or newAddress > 0x77:
				print("Invalid address!")
				continue

			# Address is valid, attempt to change it on the device
			result = my_buzzer.change_address(newAddress)

			# Check whether the address was changed successfully
			if result == False:
				print("Failed to change address!")
				continue
			
			# Success, we're done here!
			addressChanged = True

		except ValueError:
			print("Invalid address format!")

	print("Address changed successfully! Continuing...")

	# Wait a moment so user can read the messages
	time.sleep(1)

	# Loop forever
	while True:
		my_buzzer.on()
		time.sleep(1)
		my_buzzer.off()
		time.sleep(1)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example")
		sys.exit(0)