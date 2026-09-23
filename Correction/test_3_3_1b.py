import os,logging
import time
from selenium import webdriver



logging.basicConfig(level=logging.DEBUG)



def test_3_3_1():
    logging.debug("running test_3_3_1")
    driver = webdriver.Chrome()
    # page
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    driver.find_element_by_id('accept-choices').click()
    driver.switch_to.frame("iframeResult")
    driver.find_element_by_xpath('//button[@onclick="myFunction()"]').click()
    #time.sleep(4)
    mon_alert = driver.switch_to.alert
    assert mon_alert.text == "Hello! I am an alert box!"
    mon_alert.accept()
    driver.switch_to.parent_frame()
    driver.minimize_window()
    driver.maximize_window()
    assert "Tryit" in driver.title
    driver.quit()

def test_3_3_1bis():
    logging.debug("running test_3_3_1")
    driver = webdriver.Chrome()
    # page
    driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_elem_select")
    driver.find_element_by_id('accept-choices').click()
    driver.switch_to.frame("iframeResult")
    # selectionner la dropdown list
    elt = driver.find_element_by_id("cars")
    # cliquer sur la liste
    elt.click()
    # selectionner l'option
    elt = driver.find_element_by_xpath("//option[@value='fiat']")
    # cliquer sur l'option
    elt.click()
    assert elt.is_selected() == True
    driver.quit()


if __name__=="__main__":
    test_3_3_1()
    test_3_3_1bis()
