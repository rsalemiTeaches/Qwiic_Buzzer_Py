#!/usr/bin/env python
#-------------------------------------------------------------------------------
# qwiic_buzzer_ex8_sound_effects.py
# 
# This example demos the sound effects included in this library.

# This includes the following sound effects:
#   0 (aka "Siren")
#     Intended to sound like a siren, starting at a low frequency, and then
#     increasing rapidly up and then back down. This sound effect does a
#     single "up and down" cycle.
#
#   1 (aka "3 Fast Sirens")
#     Similar to the "Siren" sound effect, only faster and goes three times.
#
#   2 (aka "robot saying 'Yes'")
#     Intended to sound like a robot saying the word "yes".
#     It starts at a low frequency and quickly ramps up to a high frequency, 
#     then stops. This can be interpreted by most to be an affirmative
#     sound to any question you may ask your buzzing robot.      
#
#   3 (aka "robot yelling 'YES!'" - faster)
#     Same as the "Yes" sound effect, only faster.
#     When done more quickly, it can add enthusiasm to the buzzing sound.
#
#   4 (aka "robot saying 'No'")
#     Intended to sound like a robot saying the word "no".
#     It starts at a high frequency and quickly ramps down to a low frequency, 
#     then stops. This can be interpreted by most to be an negative
#     sound to any question you may ask your buzzing robot. 
#
#   5 (aka "robot yelling 'NO!'" - faster)
#     Same as the "No" sound effect, only faster.
#     When done more quickly, it can add enthusiasm to the buzzing sound.
#
#   6 (aka "Laughing Robot")
#     Intended to sound like your robot is laughing at you.
#
#   7 (aka "Laughing Robot Faster")
#     Same as the "Laugh" sound effect, only faster.
#     When done more quickly, it can add enthusiasm to the buzzing sound.
#
#   8 (aka "Crying Robot")
#     Intended to sound like a robot is crying and sad.
#
#   9 (aka "Crying Robot Faster")
#     Same as the "Cry" sound effect, only faster.
#     When done more quickly, it can add enthusiasm to the buzzing sound.
#
#   Sound effects based on the following work:
#     Jan 21st, 2020
#     Snake In A Can Controller
#     Written by: Pete Lewis, with contributions from Jeff Haas
#     A collaboration with Mario the Maker Magician
#     https://www.mariothemagician.com/
#
#     January, 2021
#     Cry, Laugh Functions were adapted from Adafruit animal sounds
#     by Magician/hacker Jeff Haas. Thanks Jeff!!
#     https://learn.adafruit.com/adafruit-trinket-modded-stuffed-animal/animal-sounds
#
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
	print("\nQwiic Buzzer Example 8 - Sound Effects\n")

	# Create instance of device
	my_buzzer = qwiic_buzzer.QwiicBuzzer()

	# Initialize the device
	if my_buzzer.begin() == False:
		print("The device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	print("\nQwiic Buzzer ready!\n")
	
	for i in range(0,10):
		print("\nSound Effect: ")
		print(i)
		my_buzzer.play_sound_effect(i, my_buzzer.VOLUME_MAX)
		time.sleep(2)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example")
		sys.exit(0)