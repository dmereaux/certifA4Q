import os,logging
import time
from selenium import webdriver

def test_essai():

    logging.info("running essai")
    driver=webdriver.Firefox()
    driver.get("https://www.python.org")
    driver.fullscreen_window()
    assert driver.title == 'Welcome to Python.org'
    driver.quit()
