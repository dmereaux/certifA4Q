import os,logging
import time
from selenium import webdriver

logging.basicConfig(level=logging.DEBUG)

def test_3_5_1():
    logging.debug("running test_3_5_1")
    driver = webdriver.Firefox()
    # page
    driver.get("http://prestashop.qualifiez.fr/")
    logging.info(driver.find_element_by_id("contact-link").text)
#    driver.find_element_by_id("link-static-page-contact-2").click()
    driver.find_element_by_link_text("Contactez-nous").click()
    assert  driver.title == "Contactez-nous"
    assert "Contact" in driver.title
    driver.quit()


if __name__=="__main__":
    test_3_5_1()
