import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
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
    new_page("http://automationpractice.com/index.php")
    driver.find_element_by_partial_link_text("Faded Short Sleeve T-shirts").click()
    sleep(3)
    driver.find_element_by_css_selector("#add_to_cart > button").click()
    modal = driver.find_element_by_id("layer_cart")
    # equivalent à un find mais avec une attente explicite
    WDW(modal,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a'))).click()
#    element = WebDriverWait(modal,10).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Proceed to checkout']")))
#    element = WebDriverWait(modal,10).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Proceed to checkout']")))
#    element.click()
    assert driver.title == "Order - My Store", "Checkout page is not open"


#    driver.quit()
def test_essai():
    new_page("http://automationpractice.com/index.php")
    elt=driver.find_element_by_id("contact-link")
    elts=elt.find_elements_by_link_text("Contact us")
    assert len(elts) == 2

if __name__=="__main__":
    test_3_8()
