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


class Fahrenheit:
    
	def __init__(self):
		"""Constructor for this class"""
		self.unit = "Fahrenheit"

	def toFahrenheit(self, _input):
		"""No converson necessary"""
		return round(_input)

	def toCelsius(self, _input):
		"""Converts Fahrenheit to Celsius"""
		return round(float((_input - 32) * (5/9)))

	def toKelvin(self, _input):
		"""Converts Fahrenheit to Kelvin"""
		return round(float((_input + 459.67) * (5/9)))

	def toRankine(self, _input):
		"""Converts Fahrenheit to Rankine"""
		return round(float(_input + 459.67))

