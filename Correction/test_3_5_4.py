import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
logging.basicConfig(level=logging.INFO)
driver=webdriver.Chrome()

def new_page(url):
    driver.get(url)
def test_3_5_4():
    logging.debug("running test_3_5_4")
    new_page("http://prestashop.qualifiez.fr/")
    logging.info("URL" + driver.current_url)
    logging.info("Titre" + driver.title)
    try:
         driver.find_element_by_link_text('Contactez-nous')
         pass
    except NoSuchElementException:
        print ("element pas trouvé")
    driver.quit()
if __name__=="__main__":
    test_3_5_4()
