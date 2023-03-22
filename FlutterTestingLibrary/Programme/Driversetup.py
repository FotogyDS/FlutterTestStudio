import os
import time
import Functions 
import json

from selenium.webdriver.common.by import By as by
from appium.webdriver import webdriver
from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from appium.webdriver.common.touch_action import TouchAction

with open('Parameter.json') as para:
    paraObj = json.load(para)

#todo: paraObj als dict zuweisen 
driver = Remote('http://localhost:4723',paraObj)