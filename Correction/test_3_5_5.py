import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
logging.basicConfig(level=logging.INFO)
driver=webdriver.Firefox()

def new_page(url):
    driver.get(url)
def test_3_5_5():
    logging.debug("running test_3_5_5")
    new_page("http://prestashop.qualifiez.fr/")
    logging.info("URL" + driver.current_url)
    logging.info("Titre" + driver.title)
    try:
         driver.find_element_by_xpath('//*[@id="search_widget"]/form/input[2]').send_keys("MUG")
         driver.find_element_by_css_selector('.ui-autocomplete-input"]/form/input[2]')
         pass
    except NoSuchElementException:
        logging.error("element pas trouvé")
    driver.quit()
if __name__=="__main__":
    test_3_5_5()
