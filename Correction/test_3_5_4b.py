import os,logging
import time
from selenium import webdriver


logging.basicConfig(level=logging.DEBUG)



def test_3_5_4():
    logging.debug("running test_3_5_4")
    driver = webdriver.Chrome()
    # page
    driver.get("http://prestashop.qualifiez.fr/")
    driver.find_element_by_partial_link_text("Contact").click()
    assert "Contact" in driver.title
    driver.quit()


if __name__=="__main__":
    test_3_5_1()
