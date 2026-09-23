import os,logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

logging.basicConfig(level=logging.DEBUG)



def setup_module():
    logging.info("setup")


def teardown_module():
    logging.info("teardown")
    driver.quit()

def test_3_3_1():
    logging.debug("running test_3_3_1")
    global driver
    driver = webdriver.Chrome()

    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    driver.find_element_by_id("accept-choices").click()
    driver.get_screenshot_as_file("maFenetre.png")
    driver.find_element_by_id("iframeResult").screenshot("myFrame.png")
    elt = driver.find_element_by_id("iframeResult")
    elt.screenshot("myFrame.png")

    driver.switch_to.frame("iframeResult")
    driver.switch_to.parent_frame()
    driver.minimize_window()
    driver.maximize_window()
    assert "Troit" in driver.title



if __name__=="__main__":
    test_3_3_1()
