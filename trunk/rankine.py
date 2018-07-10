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


class Rankine:

	def __init__(self):
		"""Constructor for this class"""
		self.unit = "Rankine"

	def toFahrenheit(self, _input):
		"""Converts Rankine to Fahrenheit"""
		return round(float(_input - 459.67))

	def toCelsius(self, _input):
		"""Converts Rankine to Celsius"""
		return round(float((_input - 491.67) * (5/9)))

	def toKelvin(self, _input):
		"""Converts Rankine to Kelvin"""
		return round(float(_input * (5/9)))

	def toRankine(self, _input):
		"""No converson necessary"""
		return round(_input)

