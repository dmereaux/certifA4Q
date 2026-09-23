import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Util import *

logging.basicConfig(level=logging.INFO)





def test_3_7_2():
    driver=webdriver.Chrome()
    util = Util()
    logging.debug("running test_7_1_2")
    driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_elem_select")
    driver.maximize_window()
    driver.switch_to.frame("fast-cmp-iframe")
    driver.find_element_by_xpath("//*[@id='fast-cmp-home']/nav/span[1]/button").click()
    driver.switch_to.parent_frame()
    frame = driver.find_element_by_id("iframeResult")
    driver.switch_to.frame(frame)
    time.sleep(2)
    # selectionner la dropbox
    # selectionner l'option 1
    # vérifier que l'option 1 est sélectionnée
    # selectionner l'option 2
    # vérifier que l'option 2 est sélectionnée  
    element = driver.find_element_by_id('cars')
    element.click()
    option = driver.find_element_by_xpath("//*[@id='cars']/option[1]")
    option.click()
    assert  driver.find_element_by_xpath("//*[@id='cars']/option[1]").is_selected()==True
    driver.find_element_by_xpath("//*[@id='cars']").click()
    driver.find_element_by_xpath("//*[@id='cars']/option[2]").click()
    assert  driver.find_element_by_xpath("//*[@id='cars']/option[2]").is_selected
    time.sleep(2)
    driver.quit()


