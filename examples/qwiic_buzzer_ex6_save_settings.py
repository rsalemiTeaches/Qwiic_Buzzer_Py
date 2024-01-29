#!/usr/bin/env python
#-------------------------------------------------------------------------------
# qwiic_buzzer_ex6_save_settings.py
#
# This example shows how to save settings to the buzzer.
#
# It buzzes the buzzer once, and then commands it to save the settings.
#
# It then does nothing more in the main loop. It is up to you to trigger using
# the TRIGGER header pin.
#
# NOTE, TRIGGER PIN does utilize frequency, duration and volume. This means you can 
# set it up to be a "momentary" trigger button, or a "one-shot" button.
#
# When Duration=0, trigger is "momentary" trigger button.
#
# When Duration>0, trigger will fire a "one-shot" buzz of duration length.
#
# Note, this is most practically used when planning to trigger the buzzer using
# only the TRIGGER header pin.
#
# This is useful if you want to set the frequency, duration, volume to your 
# desired settings, and then have it remember them for next time you power your 
# Qwiic buzzer up. Then you can use the TRIGGER header to cause the buzzer to 
# buzz at your saved settings.
#
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

def runExample():
	print("\nQwiic Buzzer Example 6 - Save Settings\n")

	# Create instance of device
	my_buzzer = qwiic_buzzer.QwiicBuzzer()

	# Initialize the device
	if my_buzzer.begin() == False:
		print("The device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	print("\nQwiic Buzzer ready!")

	# Comment/Un-Comment the following "buzzer.configure()" example lines to try different settings:
  
	# "MOMENTARY" SETUP
	my_buzzer.configure(1000, 0, my_buzzer.VOLUME_MID); # frequency: 1KHz, duration: 0 (aka forever), volume: MID

	# "ONE-SHOT" Setup (aka adding in a duration amount).
	# buzzer.configure(1000, 100, SFE_QWIIC_BUZZER_VOLUME_MID); # frequency: 1KHz, duration: 100ms, volume: MID	
	
	# Beep once to show settings
	my_buzzer.on()
	time.sleep(1)
	my_buzzer.off()

	print("Saving settings now...")
	my_buzzer.save_settings()

	print("Goodbye.")

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example")
		sys.exit(0)