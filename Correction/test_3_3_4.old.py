import os,logging
from selenium import webdriver
logging.basicConfig(level=logging.INFO)
driver1=webdriver.Chrome()
driver2=webdriver.Chrome()

def new_page(url):
    driver.get(url)
def test_3_3_4():
    logging.debug("running test_3_3_4")
    driver1.get("https://docs.python.org/2/library/functions.html")
    driver2.get("https://docs.python.org/3/library/functions.html")
    #driver2.switch_to.window("")
    elements = driver1.find_elements_by_partial_link_text('reload')
    assert len(elements) > 0, "Reload function could not be found"
    elements = driver2.find_elements_by_partial_link_text('reload')
    assert len(elements) == 0, "Reload function was found but not expected"
    driver1.quit()
    driver2.quit()
     

 
   
if __name__=="__main__":
    test_3_3_4()
