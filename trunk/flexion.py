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

from fahrenheit import Fahrenheit
from celcius import Celcius
from kelvin import Kelvin
from rankine import Rankine


class FlexionCmsApp:

    def __init__(self):
        """Constructor for this class"""

    def compare(self, _conversion, _answer):
        """Compares the problem to the student's answer and returns 'correct' or 'incorrect'"""
        print ("C")

    def validateInputs(self, _temperature, _target, _answer):
        """Determines the validity of the inputs from the end user"""
        
        validUnits = ["fahrenheit", "celcius", "kelvin", "rankine"]
        validity = True

        "Validate the problem"
        if len(_temperature.split()) == 2:
            tempValue = _temperature.split()[0]
            tempUnit = _temperature.split()[1]
            if tempValue.isdigit() == False or tempUnit.lower() not in validUnits:
                validity = False
        else:
            validity = False

        "Validate the target"
        if _target not in validUnits:
            validity = False

        "Validate the answer"
        if _answer.isdigit() == False:
            valdity = False
        
        return validity


#------------- END FUNCTION DEFINITIONS ------------- #


if __name__ == '__main__':
    
    print ("Welcome. This is the Flexion CMS Coding Assignment.\n\nThis application is used to check if students' temperature conversions from Fahrenheit <-> Celcius <-> Kelvin <-> Rankine are correct.\n\nPlease be sure to answer each prompt correctly in order to receive the appropriate output.\nIf you wish to exit the program at any time, please type 'exit' into any prompt or push CNTRL+C.\n")

    app = FlexionCmsApp()

    while True:
        temperature = input("Input Temperature:\n")
        if temperature.strip().lower() == 'exit':
            break;
        
        target = input("Target Units:\n")
        if target.strip().lower() == 'exit':
            break;
        
        answer = input("Answer:\n")
        if answer.strip().lower() == 'exit':
            break;

        if app.validateInputs(temperature, target, answer) == False:
            print ("\nOutput\ninvalid\n")
        else:
            print ("")
        
    sys.exit(print ("Thanks for using our application to check your answers! See you next time."))



