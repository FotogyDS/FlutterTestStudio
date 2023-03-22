import os
import time
import Functions
from Driversetup import driver

from selenium.webdriver.common.by import By as by
from appium.webdriver import webdriver
from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from appium.webdriver.common.touch_action import TouchAction

finder = FlutterFinder()

#Definition der Funktion ButtonClick(), zur vereinfachung der Testung
def ButtonClick(Buttonkey):
    clicker = finder.by_value_key(Buttonkey)
    Element_clicking = FlutterElement(driver, clicker)
    Element_clicking.click()

#Definition der Funktion ChangeFinder(), zur vereinfachung der Testung
def ChangeFinder(objectkey_to_be_read,value_to_be_checked):
    counter_finder = finder.by_value_key(objectkey_to_be_read)
    counter_element = FlutterElement(driver, counter_finder)
    print(counter_element.text)

    if counter_element.text == "{}".format(value_to_be_checked):
        print("Test Successful!")
    else:
        print("Test Unsuccessful!")

#Definition der Funktion TextFieldInput(), zur vereinfachung der Testung
def TextFieldInput(TextFieldKey,Input_text_here):
    textField= finder.by_value_key(TextFieldKey)
    textFieldElement = FlutterElement(driver, textField)
    textFieldElement.send_keys(Input_text_here)



'''
def FindElements():
    elementlist = finder.__getattribute__()
    elementListElement = FlutterElement(driver, elementlist)
    print(elementListElement)
'''
