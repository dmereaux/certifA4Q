import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Util import *

logging.basicConfig(level=logging.INFO)
driver=webdriver.Firefox()


def new_page(url):
    driver.get(url)
    logging.info("URL" + driver.current_url)
    logging.info("Titre" + driver.title)

def check_option(driver,dropdown,value):
    driver.find_element_by_xpath(dropdown).click()
    liste_option =driver.find_elements_by_xpath(dropdown+'/'+'option')
    for option in liste_option :
        if option.text == value :
            option.click()



def test_3_7_2b():
    logging.debug("running test_7_1_2")
    util = Util()
    util.new_page(driver,"https://www.w3schools.com/html/tryit.asp?filename=tryhtml_elem_select")
    driver.maximize_window()
    driver.find_element_by_id("accept-choices").click()
    frame = driver.find_element_by_id("iframeResult")
    driver.switch_to.frame(frame)
  #  element = driver.find_element_by_id('cars')
    sleep(2)
    option = driver.find_element_by_xpath("//*[@id='cars']/option[2]")
    option.click()
    assert  driver.find_element_by_xpath("//*[@id='cars']/option[2]").is_selected()==True
    sleep(2)


 