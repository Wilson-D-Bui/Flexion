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
            if "." in tempValue:
                if float(tempValue) == False:
                    validity = False
            else:
                if tempValue.isnumeric() == False:
                    validity = False
            if tempUnit.lower() not in validUnits:
                validity = False
        else:
            validity = False

        "Validate the target"
        if _target not in validUnits:
            validity = False

        "Validate the answer"
        if _answer.isnumeric() == False:
            valdity = False
        
        return validity


#------------- END FUNCTION DEFINITIONS ------------- #


if __name__ == '__main__':
    
    print ("Welcome. This is the Flexion CMS Coding Assignment.\n\nThis application is used to check if students' temperature conversions from Fahrenheit <-> Celcius <-> Kelvin <-> Rankine are correct.\n\nPlease be sure to answer each prompt correctly in order to receive the appropriate output.\nIf you wish to exit the program at any time, please type 'exit' into any prompt or push CNTRL+C.\n")

    flexion = FlexionCmsApp()
    fahrenheit = Fahrenheit()
    celcius = Celcius()
    kelvin = Kelvin()
    rankine = Rankine()

    while True:
        temperature = input("Input Temperature (e.g. 84.2 Fahrenheit):\n").lower()
        if temperature.strip() == 'exit':
            break;
        
        target = input("Target Units:\n").lower()
        if target.strip() == 'exit':
            break;
        
        answer = input("Answer:\n").lower()
        if answer.strip() == 'exit':
            break;

        if flexion.validateInputs(temperature, target, answer) == False:
            print ("\nOutput\ninvalid\n")
            continue
        else:
            print ("")

        "Once validation is complete, check the answer"
        tempValue = float(temperature.split()[0])
        tempUnit = temperature.split()[1]
        correctAnswer = 0

        "Temperature conversion logic tree"
        if tempUnit == "fahrenheit":
            if tempUnit == fahrenheit.unit.lower():
                correctAnswer = fahrenheit.toFahrenheit(tempValue)
            elif target == "celcius":
                correctAnswer = fahrenheit.toCelcius(tempValue)
            elif target == "kelvin":
                correctAnswer = fahrenheit.toKelvin(tempValue)
            elif target == "rankine":
                correctAnswer = fahrenheit.toRankine(tempValue)
            else:
                print ("Something is wrong with the input temperature unit.")
                
        elif tempUnit == "celcius":
            if target == "fahrenheit":
                correctAnswer = celcius.toFahrenheit(tempValue)
            elif target == celcius.unit.lower():
                correctAnswer = celcius.toCelcius(tempValue)
            elif target == "kelvin":
                correctAnswer = celcius.toKelvin(tempValue)
            elif target == "rankine":
                correctAnswer = celcius.toRankine(tempValue)
            else:
                print ("Something is wrong with the input temperature unit.")
                
        elif tempUnit == "kelvin":
            if target == "fahrenheit":
                correctAnswer = kelvin.toFahrenheit(tempValue)
            elif target == "celcius":
                correctAnswer = kelvin.toCelcius(tempValue)
            elif target == kelvin.unit.lower():
                correctAnswer = kelvin.toKelvin(tempValue)
            elif target == "rankine":
                correctAnswer = kelvin.toRankine(tempValue)
            else:
                print ("Something is wrong with the input temperature unit.")
                
        elif tempUnit == "rankine":
            if target == "fahrenheit":
                correctAnswer = rankine.toFahrenheit(tempValue)
            elif target == "celcius":
                correctAnswer = rankine.toCelcius(tempValue)
            elif target == "kelvin":
                correctAnswer = rankine.toKelvin(tempValue)
            elif target == rankine.unit.lower():
                correctAnswer = rankine.toRankine(tempValue)
            else:
                print ("Something is wrong with the input temperature unit.")
                
        else:
            print ("Something is wrong with the inputs values...")


        
        
    sys.exit(print ("Thanks for using our application to check your answers! See you next time."))



