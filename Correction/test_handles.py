import os,logging
import time
from selenium import webdriver
logging.basicConfig(level=logging.DEBUG)



def test_handles():
    logging.debug("running test_3_1")
    logging.warning("warning")
    logging.error("gros probleme")
    driver = webdriver.Chrome()
    driver.get("http://www.qualifiez.fr/examples/Selenium/project-list.php")
    premiereF = driver.current_window_handle
    logging.warning(premiereF)
    driver.find_element_by_xpath("//*[@id='btnNewWindow']").click()
    elts = driver.window_handles
    secondeF=""
    for handle in elts:
        logging.warning(handle)
        if handle != premiereF:
            secondeF=handle
    driver.switch_to.window("toto")
    assert driver.title == "My Window"
    driver.switch_to.window(premiereF)
    assert driver.title == "Projets"




if __name__=="__main__":
    test_3_1()
