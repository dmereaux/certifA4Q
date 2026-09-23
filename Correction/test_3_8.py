import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

logging.basicConfig(level=logging.INFO)
driver=webdriver.Chrome()



def new_page(url):
    driver.get(url)
    logging.info("URL" + driver.current_url)
    logging.info("Titre" + driver.title)

def test_3_8():
    logging.debug("running test_3_8")

    new_page("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert") 
    driver.maximize_window()
    driver.switch_to.frame("fast-cmp-iframe")
    driver.find_element_by_xpath("//*[@id='fast-cmp-home']/nav/span[1]/button").click()
    driver.switch_to.parent_frame()
    frame = driver.find_element_by_id("iframeResult")
    driver.switch_to.frame(frame)
    time.sleep(2)

    try_it_button = driver.find_element_by_css_selector('[onclick*="myFunction()"]')
    try_it_button.click()
    alert = driver.switch_to.alert
    assert "Hello!" in alert.text, "Incorrect text"
    alert.dismiss()
    driver.quit()
if __name__=="__main__":
    test_3_8()
