#!/usr/bin/env python3.6

"""
Application - Flexion CMS Coding Challenge
Usage:
  flexion.py 
  flexion.py (-h | --help)
  flexion.py --version
Options:
  -h, --help    Show this screen.
  --version     Show version.
"""

__author__ = 'Wilson Bui'
__copyright__ = 'Copyright 2018, Bui Technologies'
__license__ = 'N/A'
__version__ = '1.0.0'
__maintainer__ = 'Wilson Bui'
__email__ = 'wilson.d.bui@hotmail.com'
__status__ = 'Development'

#------------- BEGIN FUNCTION DEFINITIONS ------------- #

import os
import sys


class FlexionCmsApp:
    """
    Top-level class that calls application
    """
    def __init__(self):
        """
        Initialize main class with necessary variables.
        """
        self._input = ''
        self._answer = ''

    def compare(_conversion, _answer):
        """
        Compares the problem to the student's answer and returns 'correct' or 'incorrect'
        """
        print ("C")

    def validateTemp(_temperature):
        """
        Determines the validity of the input from the end user
        """
        print ("V")

    def fahrenheit(_input):
        """
        Calls fahrenheit.py to convert units to Fahrenheit
        """
        print ("F")

    def celcius(_input):
        """
        Calls celcius.py to convert units to Celcius
        """
        print ("C")

    def kelvin(_input):
        """
        Calls kelvin.py to convert units to Kelvin
        """
        print ("K")

    def rankine(_input):
        """
        Calls rankine.py to convert units to Rankine
        """
        print ("Rs")

#------------- END FUNCTION DEFINITIONS ------------- #


if __name__ == '__main__':
    
    print ("Welcome. This is the Flexion CMS Coding Assignment.\n\nThis application is used to check if students' temperature conversions from F <-> C <-> K <-> R are correct.\n\nPlease be sure to answer each prompt correctly in order to receive the appropriate output.\nIf you wish to exit the program at any time, please type 'exit' into any prompt or push CNTRL+C.\n")

    app = FlexionCmsApp()

    while True:
        temperature = input("Please enter the value and unit of temperature using the following format (e.g. 84.2 Fahrenheit):\n")
        targetUnit = input("Please enter the target unit of temperature:\n")
        answer = input("Please enter the student's answer:\n")

        if temperature.strip().upper() == 'EXIT':
            print ("Thanks for using our application to check your answers! See you next time.")
            break;
    
    sys.exit(app)



