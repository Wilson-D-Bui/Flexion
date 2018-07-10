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


class Kelvin:

	def __init__(self):
		"""Constructor for this class"""
		self.unit = "Kelvin"

	def toFahrenheit(self, _input):
		"""Converts Kelvin to Fahrenheit"""
		return round(float(_input * (9/5) - 459.67))

	def toCelsius(self, _input):
		"""Converts Kelvin to Celsius"""
		return round(float(_input - 273.15))

	def toKelvin(self, _input):
		"""No converson necessary"""
		return round(_input)

	def toRankine(self, _input):
		"""Converts Kelvin to Rankine"""
		return round(float(_input * (9/5)))

