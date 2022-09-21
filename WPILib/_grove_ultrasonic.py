#!/usr/bin/env python3

# The MIT License (MIT)
#
# Copyright (c) 2017 Mike Mabey
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`grove_ultrasonic`
====================================================

A CircuitPython library for the Grove ultrasonic range sensor.
Based on the CircuitPython library for the HC-SR04 ultrasonic range sensor.

The HC-SR04 functions by sending an ultrasonic signal, which is reflected by
many materials, and then sensing when the signal returns to the sensor. Knowing
that sound travels through dry air at `343.2 meters per second (at 20 °C)
<https://en.wikipedia.org/wiki/Speed_of_sound>`_, it's pretty straightforward
to calculate how far away the object is by timing how long the signal took to
go round-trip and do some simple arithmetic, which is handled for you by this
library.

* Original authors:

  - Mike Mabey
  - Jerry Needell - modified to add timeout while waiting for echo (2/26/2018)
  - ladyada - compatible with `distance` property standard, renaming, Pi compat
"""

import time
from digitalio import DigitalInOut, Direction

# Took this idea from adafruit_debouncer.py
# Find out whether the current CircuitPython supports time.monotonic_ns(),
# which doesn't have the accuracy limitation.
if hasattr(time, "monotonic_ns"):
    TICKS_PER_SEC = 1_000_000_000
    MONOTONIC_TICKS = time.monotonic_ns
else:
    TICKS_PER_SEC = 1
    MONOTONIC_TICKS = time.monotonic
	
_USE_PULSEIO = False
try:
	from pulseio import PulseIn
	
	_USE_PULSEIO = True
except ImportError:
	pass  # This is OK, we'll try to bitbang it!
	
__version__ = "1.0.0"
__repo__ = "https://github.com/derhexenmeister/GroveUltrasonicRanger.git"


class GroveUltrasonic:
	"""Control a Grove ultrasonic range sensor.

	Example use:

	::

		import time
		import board

		import grove_ultrasonic_ranger

		sonar = grove_ultrasonic_ranger.GroveUltrasonicRanger(sig_pin=board.D2)


		while True:
			try:
				print((sonar.distance,))
			except RuntimeError as e:
				print("Retrying due to exception =", e)
				pass
			time.sleep(0.1)
	"""
	
	def __init__(self, sig_pin, unit=1.0, timeout=1.0):
		"""
		:param sig_pin: The pin on the microcontroller that's connected to the
			``Sig`` pin on the GroveUltrasonicRanger.
		:type sig_pin: microcontroller.Pin
		:param float unit: pass in conversion factor for unit conversions from cm
			for example 2.54 would convert to inches.
		:param float timeout: Max seconds to wait for a response from the
			sensor before assuming it isn't going to answer. Should *not* be
			set to less than 0.05 seconds!
		"""
		print("init grove with ", sig_pin)
		self._unit = unit
		self._timeout = timeout*TICKS_PER_SEC
		print("Using pulseio: ", _USE_PULSEIO)
		if _USE_PULSEIO:
			self._sig = PulseIn(sig_pin)
			self._sig.pause()
			self._sig.clear()
		else:
			self._sig = DigitalInOut(sig_pin)
			self._sig.direction = Direction.OUTPUT
			self._sig.value = False	 # Set trig low
			
	def __enter__(self):
		#Allows for use in context managers.
		return self
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		#Automatically de-initialize after a context manager.
		self._deinit()
		
	def _deinit(self):
		#De-initialize the sig pin.
		self._sig.deinit()
		
	def get_distance(self) -> float:
		"""
		Return the distance measured by the sensor in cm.

		:return: Distance in centimeters
		:rtype: float
		"""
		return self._dist_one_wire()
	
	def _dist_one_wire(self):
		if _USE_PULSEIO:
			self._sig.pause()
			self._sig.clear()  # Discard any previous pulse values
		else:
			#self._sig.direction = Direction.OUTPUT
			self._sig.value = True	# Set trig high
			time.sleep(0.00001)	 # 10 micro seconds 10/1000/1000
			self._sig.value = False	 # Set trig low
			self._sig.direction = Direction.INPUT
			
		pulselen = None
		timestamp = MONOTONIC_TICKS()
		if _USE_PULSEIO:
			self._sig.resume(10)
			while not self._sig:
				# Wait for a pulse
				if (MONOTONIC_TICKS() - timestamp) > self._timeout:
					self._sig.pause()
					raise RuntimeError("Timed out (pulseio waiting for a pulse)")
			self._sig.pause()
			pulselen = self._sig[0]
		else:
			# OK no hardware pulse support, we'll just do it by hand!
			# hang out while the pin is low
			while not self._sig.value:
				if MONOTONIC_TICKS() - timestamp > self._timeout:
					self._sig.direction = Direction.OUTPUT
					raise RuntimeError("Timed out (gpio, waiting for pulse leading edge)")
			timestamp = MONOTONIC_TICKS()
			# track how long pin is high
			while self._sig.value:
				if MONOTONIC_TICKS() - timestamp > self._timeout:
					self._sig.direction = Direction.OUTPUT
					raise RuntimeError("Timed out (gpio, waiting for pulse trailing edge)")
			pulselen = MONOTONIC_TICKS() - timestamp
			self._sig.direction = Direction.OUTPUT
			pulselen *= (1000000/TICKS_PER_SEC) # convert to us to match pulseio
		if pulselen >= 65535:
			raise RuntimeError("Timed out (unreasonable pulse length)")
			
		# positive pulse time, in seconds, times 340 meters/sec, then
		# divided by 2 gives meters. Multiply by 100 for cm
		# 1/1000000 s/us * 340 m/s * 100 cm/m * 2 = 0.017
		# Divide by the supplied unit conversion factor
		return (pulselen * 0.017)/self._unit
