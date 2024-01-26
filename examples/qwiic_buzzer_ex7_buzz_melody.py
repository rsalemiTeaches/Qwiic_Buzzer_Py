#!/usr/bin/env python
#-------------------------------------------------------------------------------
# qwiic_buzzer_ex7_buzz_melody.py
#
# This example shows how to buzz a melody on the Qwiic Buzzer
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
	print("\nQwiic Buzzer Example 7 - Buzz Melody\n")

	# Create instance of device
	my_buzzer = qwiic_buzzer.QwiicBuzzer()

	# Initialize the device
	if my_buzzer.begin() == False:
		print("The device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	print("\nQwiic Buzzer ready!")
	
	# notes in the melody
	melody = [my_buzzer.NOTE_C4, my_buzzer.NOTE_G3, my_buzzer.NOTE_G3, my_buzzer.NOTE_A3, my_buzzer.NOTE_G3, my_buzzer.NOTE_REST, my_buzzer.NOTE_B3, my_buzzer.NOTE_C4]

	# note durations: 4 = quarter note, 8 = eighth note, etc.:
	noteDurations = [4, 8, 8, 4, 4, 4, 4, 4]

	# iterate over the notes of the melody:
	for thisNote in range(8):
		# to calculate the note duration, take one second divided by the note type.
		#e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
		noteDuration = round(1000 / noteDurations[thisNote])
		my_buzzer.configure(melody[thisNote], noteDuration, my_buzzer.VOLUME_MAX)
		my_buzzer.on()

		# to distinguish the notes, set a minimum time between them.
		# the note's duration + 30% seems to work well:
		pauseBetweenNotes = noteDuration * 1.30
		time.sleep(pauseBetweenNotes * 0.001)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example")
		sys.exit(0)