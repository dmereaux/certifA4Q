# https://dealy.com/iphone-17/165376-450327-etui-iphone-17-compatible-magsafe-avec-porte-cartes-rfid.html#/11-color-black
import os,logging
from selenium import webdriver
import time
logging.basicConfig(level=logging.INFO)
driver=webdriver.Chrome()
def test_modale():
    logging.debug("running test_modale")
    driver.get("https://dealy.com/iphone-17/165376-450327-etui-iphone-17-compatible-magsafe-avec-porte-cartes-rfid.html#/11-color-black")
    logging.info("URL" + driver.current_url)
    logging.info("Titre" + driver.title)

    driver.find_element_by_css_selector(".btn.btn-primary").click()
    modale = driver.find_element_by_xpath('//div[@class="modal-content"]')
    time.sleep(2)
    modale.find_element_by_css_selector('#blockcart-modal > div > div > div.modal-header.modal-header--primary > div > button > span > svg').click()
    driver.quit()