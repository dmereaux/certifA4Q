import os,logging
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)
driver=webdriver.Chrome()

def new_page(url):
    driver.get(url)
def test_3_3_1():
    logging.debug("running test_3_3_1")
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    driver.maximize_window()
    driver.switch_to.frame("fast-cmp-iframe")
#    wait = WebDriverWait(driver,10)
#    bouton= wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='fast-cmp-home']/nav/span[1]/button")))
#    bouton.click()
    driver.switch_to.parent_frame()
    driver.quit()
if __name__=="__main__":
    test_3_3_1()
