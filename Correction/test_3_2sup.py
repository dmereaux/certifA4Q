import os,logging,time

import pytest
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

@pytest.fixture
def my_setUpTearDown():
    #setup
    logging.debug("setUP")
    yield
    #teardown
    logging.debug("teardown")
    driver.quit()


#@pytest.fixture
def my_tearDown(my_setUpTearDown):
    logging.debug("teardown")
    time.localtime().tm_hour
#    driver.quit()


def test_3_2(my_setUpTearDown):
    
    logging.debug("running test_3_2")
    driver.get("https://www.python.org/")
    driver.implicitly_wait(10)
    driver.find_element_by_id("gyfzefgz")
    logging.info("URL" + driver.current_url)
    driver.find_element_by_id("fgekrhgy")
    assert driver.title=="Welcome to Python.org"
    assert "Python"  in driver.title
    logging.info("Titre" + driver.title)
    liste= driver.find_elements_by_xpath("")
    for elt in liste :
        assert "Mug" in elt.text
#    for x  in driver.window_handles :
##        logging.warning( str(x) )
#    assert "Python" in driver.title , "ca marche pas"

def test_3_3():
    driver=webdriver.Chrome()
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    driver.maximize_window()
    sleep(2)
#    assert driver.find_element_by_xpath("/html/body/h1").text=="The Window Object"
    driver.find_element_by_id("accept-choices").screenshot("./toto.png")
    driver.find_element_by_id("accept-choices").click()
    driver.switch_to.frame("iframeResult")
    driver.get_screenshot_as_file("./titi.png")
    assert driver.find_element_by_xpath("/html/body/h1").text=="The Window Object"
    driver.switch_to.default_content
    



if __name__=="__main__":
    test_3_2()
