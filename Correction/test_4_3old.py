import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

logging.basicConfig(level=logging.INFO)
driver=webdriver.Chrome()



def new_page(url):
    driver.get(url)
    logging.info("URL" + driver.current_url)
    logging.info("Titre" + driver.title)

def doSearch(search_text): 
    driver.find_element_by_xpath("//form[@id = 'searchbox']").click() 
    driver.find_element_by_name("search_query").clear() 
    driver.find_element_by_name("search_query").send_keys(search_text) 
    driver.find_element_by_xpath("//button[@type='submit']").click()

def itemAddtoCartByNum(item): 
    driver.find_elements_by_xpath("//a[@title='Add to cart']")[item].click()

def test_4_3(): 
    new_page("http://automationpractice.com")
    doSearch("chiffon")
    itemAddtoCartByNum(0)
    assert driver.find_elements_by_xpath("//a[@class='product-name']")[0].text == 'Printed Chiffon Dress' 
    driver.close()
if __name__=="__main__":
    test_4_3()
