import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Util import *

logging.basicConfig(level=logging.INFO)
driver=webdriver.Chrome()


def new_page(url):
    driver.get(url)
    logging.info("URL" + driver.current_url)
    logging.info("Titre" + driver.title)

def check_option(driver,dropdown,value):
    driver.find_element_by_xpath(dropdown).click()
    liste_option =driver.find_elements_by_xpath(dropdown+'/'+'option')
    for option in liste_option :
        if option.text == value :
            option.click()
def test_3_7_2b():
    driver=webdriver.Chrome()
    util = Util()
    logging.debug("running test_7_1_2")
    driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_elem_select")
    driver.maximize_window()
    driver.switch_to.frame("fast-cmp-iframe")
    driver.find_element_by_xpath("//*[@id='fast-cmp-home']/nav/span[1]/button").click()
    driver.switch_to.parent_frame()
    frame = driver.find_element_by_id("iframeResult")
    driver.switch_to.frame(frame)
    sleep(2)
    element = driver.find_element_by_id('cars')
    element.click()
    option = driver.find_element_by_xpath("//*[@id='cars']/option[1]")
    option.click()
    assert  driver.find_element_by_xpath("//*[@id='cars']/option[1]").is_selected()==True
    util.changer_option(driver,"//*[@id='cars']","//*[@id='cars']/option[2]")
    #    changer_option(driver,"//*[@id='cars']","//*[@id='cars']/option[2]")
    assert  driver.find_element_by_xpath("//*[@id='cars']/option[2]").is_selected()==True
    check_option(driver,"//*[@id='cars']","Volvo")
    assert  driver.find_element_by_xpath("//*[@id='cars']/option[1]").is_selected()==True
    driver.quit()



def test_3_7_2():
    driver=webdriver.Chrome()
    logging.debug("running test_7_1_2")
    driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_elem_select")
    driver.maximize_window()
    driver.switch_to.frame("fast-cmp-iframe")
    driver.find_element_by_xpath("//*[@id='fast-cmp-home']/nav/span[1]/button").click()
    driver.switch_to.parent_frame()
    frame = driver.find_element_by_id("iframeResult")
    driver.switch_to.frame(frame)
    element = driver.find_element_by_id('cars')
    # cast en objet de type select
    select = Select(driver.find_element_by_id("cars"))
    all_selected_options = select.all_selected_options
    for option in all_selected_options:
        print("Value is: %s" % option.get_attribute("value"))
    select.select_by_visible_text("Volvo")
    logging.info(select.first_selected_option)
    driver.quit()



def changer_option(driver, path_dropdown, path_option):
    driver.find_element_by_xpath(path_dropdown)
    driver.find_element_by_xpath(path_option).click()
def test_check():
    driver=webdriver.Chrome()
    logging.debug("running test_check")
    driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_elem_select")
    driver.maximize_window()
    driver.switch_to.frame("fast-cmp-iframe")
    driver.find_element_by_xpath("//*[@id='fast-cmp-home']/nav/span[1]/button").click()
    driver.switch_to.parent_frame()
    driver.get_screenshot_as_file("fenetre.png")
    frame = driver.find_element_by_id("iframeResult")
    driver.switch_to.frame(frame)
    changer_option(driver,"//select[@id='cars']", "//option[@value='saab']")
    assert driver.find_element_by_xpath("//option[@value='saab']").is_selected()
    driver.quit()

def changer_etat_checkbox(driver,checke, path_checkBox):
    if checke and not driver.find_element_by_xpath(path_checkBox).is_selected() :
        driver.find_element_by_xpath(path_checkBox).click()
    elif not checke and driver.find_element_by_xpath(path_checkBox).is_selected():
        driver.find_element_by_xpath(path_checkBox).click()

if __name__=="__main__":
    test_3_7_2()
