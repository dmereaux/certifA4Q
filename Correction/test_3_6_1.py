import os,logging
from selenium import webdriver
logging.basicConfig(level=logging.INFO)
driver=webdriver.Firefox()

def new_page(url):
    driver.get(url)
def test_3_6_1():
    new_page("http://prestashop.qualifiez.fr/")
    element=driver.find_element_by_css_selector("#_desktop_user_info > div > a > span")
    print("Element Text:" + element.text)
    driver.quit()
if __name__=="__main__":
    test_3_6_1()
