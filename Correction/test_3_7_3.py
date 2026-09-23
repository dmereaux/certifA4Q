import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

logging.basicConfig(level=logging.INFO)
driver=webdriver.Firefox()

def new_page(url):
    driver.get(url)
    
    logging.info("URL" + driver.current_url)
    logging.info("Titre" + driver.title)

def test_3_7_3():
    logging.debug("running test_7_1_3")
    new_page("http://prestashop.qualifiez.fr/")
    driver.find_element_by_xpath("//*[@id='content']/section[1]/div/div[1]/article/div/div[1]/a/picture/img").click()
    driver.find_element_by_xpath("//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button").click()
    wait = WebDriverWait(driver,10)
    modal=wait.until(EC.presence_of_element_located((By.ID,"blockcart-modal")))
#    modal = driver.find_element_by_id("blockcart-modal")
#    modal = driver.find_element_by_class_name("modal-dialog")
    element = WebDriverWait(modal,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/a")))
#    element = modal.find_element_by_xpath("//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/a")
    element.click()

    assert driver.title == "Panier", "Checkout page is not open"
    driver.quit()


if __name__=="__main__":
    test_3_7_3()
