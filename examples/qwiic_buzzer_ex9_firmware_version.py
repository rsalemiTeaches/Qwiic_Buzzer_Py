#!/usr/bin/env python
#-------------------------------------------------------------------------------
# qwiic_buzzer_ex9_firmware_version.py
# 
# This example shows how to read the firmware version from the Qwiic Buzzer
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
  print("\nQwiic Buzzer Example 9 - Firmware Version\n")

  # Create instance of device
  if (sys.platform == "esp32"):
      alvik_i2c_driver = MicroPythonI2C(scl=12, sda=11)
      my_buzzer = qwiic_buzzer.QwiicBuzzer(i2c_driver=alvik_i2c_driver)
  else:
      my_buzzer = qwiic_buzzer.QwiicBuzzer()

  # Initialize the device
  if my_buzzer.begin() == False:
      print("The device isn't connected to the system. Please check your connection", \
          file=sys.stderr)
      return

  print("\nQwiic Buzzer ready!\n")
  
  print("Firmware Version Major: ")
  print(my_buzzer.firware_version_major())
  print("\nFirmware Version Minor: ")
  print(my_buzzer.firware_version_minor())

if __name__ == '__main__':
  try:
      runExample()
  except (KeyboardInterrupt, SystemExit) as exErr:
      print("\nEnding Example")
      sys.exit(0)