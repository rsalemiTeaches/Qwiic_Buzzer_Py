#-------------------------------------------------------------------------------
# qwiic_buzzer.py
#
# Python library for the SparkFun Qwiic Buzzer, available here:
# https://www.sparkfun.com/products/24474
#-------------------------------------------------------------------------------
# Written by SparkFun Electronics, January 2024
#
# This python library supports the SparkFun Electroncis Qwiic ecosystem
#
# More information on Qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#===============================================================================
# Copyright (c) 2024 SparkFun Electronics
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

"""
qwiic_buzzer
============
Python module for the [SparkFun Qwiic Buzzer](https://www.sparkfun.com/products/24474)
This is a port of the existing [Arduino Library](https://github.com/sparkfun/SparkFun_Qwiic_Buzzer_Arduino_Library)
This package can be used with the overall [SparkFun Qwiic Python Package](https://github.com/sparkfun/Qwiic_Py)
New to Qwiic? Take a look at the entire [SparkFun Qwiic ecosystem](https://www.sparkfun.com/qwiic).
"""

# The Qwiic_I2C_Py platform driver is designed to work on almost any Python
# platform, check it out here: https://github.com/sparkfun/Qwiic_I2C_Py
import qwiic_i2c

# Define the device name and I2C addresses. These are set in the class defintion
# as class variables, making them avilable without having to create a class
# instance. This allows higher level logic to rapidly create a index of Qwiic
# devices at runtine
_DEFAULT_NAME = "Qwiic Buzzer"

# Some devices have multiple available addresses - this is a list of these
# addresses. NOTE: The first address in this list is considered the default I2C
# address for the device.
_QWIIC_BUZZER_DEFAULT_ADDRESS = 0x34
_FULL_ADDRESS_LIST = list(range(0x08, 0x77+1))  # Full address list (excluding reserved addresses)
_FULL_ADDRESS_LIST.remove(_QWIIC_BUZZER_DEFAULT_ADDRESS >> 1)   # Remove default address from list
_AVAILABLE_I2C_ADDRESS = [_QWIIC_BUZZER_DEFAULT_ADDRESS]    # Initialize with default address
_AVAILABLE_I2C_ADDRESS.extend(_FULL_ADDRESS_LIST) # Add full range of I2C addresses

# Define the class that encapsulates the device being created. All information
# associated with this device is encapsulated by this class. The device class
# should be the only value exported from this module.
class QwiicBuzzer(object):
    # Set default name and I2C address(es)
    device_name         = _DEFAULT_NAME
    available_addresses = _AVAILABLE_I2C_ADDRESS

    # TODO: Define constants here
    _ID = 0x5E

    # Register addresses for the Qwiic Buzzer
    _REG_ADR_ID = 0x00
    _REG_ADR_FW_MIN = 0x01
    _REG_ADR_FW_MAJ = 0x02
    _REG_ADR_FREQ_MSB = 0x03
    _REG_ADR_FREQ_LSB = 0x04
    _REG_ADR_VOL = 0x05
    _REG_ADR_DUR_MSB = 0x06
    _REG_ADR_DUR_LSB = 0x07
    _REG_ADR_ACTIVE = 0x08
    _REG_ADR_SAVE = 0x09
    _REG_ADR_I2C_ADD = 0x0A

    VOLUME_MIN = 1
    VOLUME_LOW = 2
    VOLUME_MID = 3
    VOLUME_MAX = 4

    def __init__(self, address=None, i2c_driver=None):
        """
        Constructor

        :param address: The I2C address to use for the device
            If not provided, the default address is used
        :type address: int, optional
        :param i2c_driver: An existing i2c driver object
            If not provided, a driver object is created
        :type i2c_driver: I2CDriver, optional
        """

        # Use address if provided, otherwise pick the default
        if address in self.available_addresses:
            self.address = address
        else:
            self.address = self.available_addresses[0]

        # Load the I2C driver if one isn't provided
        if i2c_driver is None:
            self._i2c = qwiic_i2c.getI2CDriver()
            if self._i2c is None:
                print("Unable to load I2C driver for this platform.")
                return
        else:
            self._i2c = i2c_driver

        # TODO: Initialize any variables used by this driver

    def is_connected(self):
        """
        Determines if this device is connected

        :return: `True` if connected, otherwise `False`
        :rtype: bool
        """
        # Check if connected by seeing if an ACK is received
        # TODO: If the device has a product ID register, that should be
        # checked in addition to the ACK
        return self._i2c.isDeviceConnected(self.address)

    connected = property(is_connected)

    def begin(self):
        """
        Initializes this device with default parameters
        Run is_connected() and check the ID in the ID register

        :return: Returns `True` if successful, otherwise `False`
        :rtype: bool
        """
        # Confirm device is connected before doing anything
        if self.is_connected():
            id = self._i2c.readByte(self.address, self._REG_ADR_ID)
            
            if id == self._ID:
                return True

        # TODO Perform a reset of the device if possible. This reverts all
        # registers to a known state in case the device was reconfigured before

        # TODO: Configure device as needed. Once complete, the device should be
        # fully ready to use to make it very simple for the user

        # TODO: Return True once successful. Template defaults to False!
        return False

    # TODO: Add features for this device

    def on(self):
        """
        Turns on the buzzer

        :return: Returns true if the register write has completed
        :rtype: bool
        """

        self._i2c.writeByte(self.address, self._REG_ADR_ACTIVE, 1)

        return True
    
    def off(self):
        """
        Turns off the buzzer

        :return: Returns true if the register write has completed
        :rtype: bool
        """
        
        self._i2c.writeByte(self.address, self._REG_ADR_ACTIVE, 0)

        return True

    def configure(self, frequency = 2730, duration = 0, volume = 3):
        """
        Configures the Qwiic Buzzer without causing the buzzer to buzz.
        This allows configuration in silence (before you may want to buzz).
        It is also useful in combination with saveSettings(), and then later
        causing buzzing by using the physical TRIGGER pin.
        To start buzzing (via Qwiic) with your desired configuration, use this
        function, then call on().

        :param frequency: Frequency in Hz of buzzer tone
        :type frequency: int
        :param duration: Duration in milliseconds (0 = forever)
        :type duration: int        
        :param volume: Volume (4 settings; 0=off, 1=quiet... 4=loudest) 
        :type volume: int                   
        :return: Returns true if the register write has completed
        :rtype: bool
        """
        
        # All of the necessary configuration register addresses are in sequential order,
        # starting at "_REG_ADR_FREQ_MSB".
        # We can write all of them in a single use of "writeBlock()".

        # _REG_ADR_FREQ_MSB = 0x03,
        # _REG_ADR_FREQ_LSB = 0x04,
        # _REG_ADR_VOL = 0x05,
        # _REG_ADR_DUR_MSB = 0x06,
        # _REG_ADR_DUR_LSB = 0x07,

        # extract MSBs and LSBs from user passed in arguments
        frequencyMSB = ((frequency & 0xFF00) >> 8)
        frequencyLSB = (frequency & 0x00FF)
        durationMSB = ((duration & 0xFF00) >> 8)
        durationLSB = (duration & 0x00FF)

        data = [0,0,0,0,0]

        data[0] = frequencyMSB; # _REG_ADR_FREQ_MSB
        data[1] = frequencyLSB; # _REG_ADR_FREQ_LSB
        data[2] = volume;           # _REG_ADR_VOL
        data[3] = durationMSB;      # _REG_ADR_DUR_MSB
        data[4] = durationLSB;      # _REG_ADR_DUR_LSB

        self._i2c.writeBlock(self.address, self._REG_ADR_FREQ_MSB, data)

        return True    
