import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
#from time import sleep
import time
from selenium.webdriver.support.ui import Select
logging.basicConfig(level=logging.INFO)
driver=webdriver.Chrome()

def new_page(url):
    driver.get(url)
    logging.info("URL" + driver.current_url)
    logging.info("Titre" + driver.title)

def test_3_6_3():

    logging.debug("running test_3_6_3")
    new_page("http://www.qualifiez.fr/monPrestashop2/prestashop/index.php?id_product=1&id_product_attribute=3&rewrite=hummingbird-printed-t-shirt&controller=product#/2-taille-m/8-couleur-blanc")
    
    element1 = driver.find_element_by_xpath('//*[@id="group_2"]/li[1]/label/input')
    assert element1.is_selected()==True
    element2 = driver.find_element_by_xpath('//*[@id="group_2"]/li[2]/label/input')
    assert element2.is_selected()==False
    element2.click()
#    element = driver.find_element_by_xpath('//*[@id="group_2"]/li[1]/label/input')
    assert element1.is_selected()==False
#    element = driver.find_element_by_xpath('//*[@id="group_2"]/li[2]/label/input')
    assert element2.is_selected()==True
    driver.find_element_by_id("group_1").click()
    driver.find_element_by_xpath("//option[@title='M']").click()
    assert driver.find_element_by_xpath("//option[@title='M']").is_selected()==True

    select = Select(driver.find_element_by_id("group_1"))
    select.select_by_visible_text('S')
    assert select.first_selected_option.text=='S'



#    print("Selected: " + str(element.is_selected()))
#    print("Now click the white checkbox")
#    assert element.is_selected()==True
#    time.sleep(1)
#    driver.find_element_by_xpath('//*[@id="group_2"]/li[2]/label/input').click()
#    time.sleep(2)
#    element = driver.find_element_by_xpath('//*[@id="group_2"]/li[1]/label/input')
#    assert element.is_selected()==False
#    element = driver.find_element_by_xpath('//*[@id="group_2"]/li[1]/label/input')
#    element_state = element.is_selected()
#    print("Selected: " + str(element_state))
    driver.quit()
if __name__=="__main__":
    test_3_6_3()
