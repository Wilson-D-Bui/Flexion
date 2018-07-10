#!/usr/bin/env python3.6

__author__ = 'Wilson Bui'
__copyright__ = 'Copyright 2018, Bui Technologies'
__license__ = 'N/A'
__version__ = '1.0.0'
__maintainer__ = 'Wilson Bui'
__email__ = 'wilson.d.bui@hotmail.com'
__status__ = 'Development'


import os
import sys


class Celsius:

	def __init__(self):
		"""Constructor for this class"""
		self.unit = "Celsius"

	def toFahrenheit(self, _input):
		"""Converts Celsius to Fahrenheit"""
		return round(float(_input * (5/9) + 32))

	def toCelsius(self, _input):
		"""Converts Celsius to Fahrenheit"""
		return round(_input)

	def toKelvin(self, _input):
		"""Converts Celsius to Kelvin"""
		return round(float(_input + 273.15))

	def toRankine(self, _input):
		"""Converts Celsius to Rankine"""
		return round(float((_input + 273.15) * (9/5)))

