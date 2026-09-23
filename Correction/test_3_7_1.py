import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)
driver=webdriver.Chrome()

def new_page(url):
    driver.get(url)
    logging.info("URL" + driver.current_url)
    logging.info("Titre" + driver.title)

def test_3_7_1():
    logging.debug("running test_3_7_1")
    new_page("http://prestashop.qualifiez.fr")
    element = driver.find_element_by_xpath("//*[@id='_desktop_user_info']/div/a")
#    element = (WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="_desktop_user_info"]/div/a'))))
    element.click()
    logging.info("URL: " + driver.current_url)
    assert "authentication" in driver.current_url,  "Incorrect page opened"
    assert driver.title=="Identifiant"
    driver.quit()
if __name__=="__main__":
    test_3_7_1()
