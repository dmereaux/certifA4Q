import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Util import *

logging.basicConfig(level=logging.INFO)

class page_recherche():
    # LOCATOR
    loc_res = "//*[@id='js-product-list-top']/div[1]/p"
    loc_erreur= "//*[@id='content']/h4"

    util=Util()

    def __init__(self, driver):
        self.driver = driver
        self.driver.get_screenshot_as_file("recherche.png")


    def resultat(self):
        return self.driver.find_element_by_xpath(self.loc_res).text

    def msg_erreur(self):
        return self.util.recherche_gen(self.driver,self.loc_erreur).text



