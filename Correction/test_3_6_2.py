import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
logging.basicConfig(level=logging.INFO)
driver=webdriver.Firefox()

def new_page(url):
    driver.get(url)
    logging.info("URL" + driver.current_url)
    logging.info("Titre" + driver.title)

def test_3_6_2():
    logging.debug("running test_3_6_2")
    new_page("http://prestashop.qualifiez.fr/")
    element=driver.find_element_by_css_selector("#_desktop_user_info > div > a > span")
    element_outerHTML = element.get_attribute("outerHTML")
    print("outerHTML: " + element_outerHTML)
    driver.quit()
if __name__=="__main__":
    test_3_6_2()
