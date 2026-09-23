import os,logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Util() :

    def new_page(self,driver,url):
        driver.get(url)
        logging.info("URL" + driver.current_url)
        logging.info("Titre" + driver.title)

    def changer_option(self,driver, path_dropdown, path_option):
        driver.find_element_by_xpath(path_dropdown).click()
        driver.find_element_by_xpath(path_option).click()

    def recherche_gen(self,driver,chemin):
        return driver.find_element_by_xpath(chemin)
    def click_gen(self,driver,chemin):
        wait = WebDriverWait(driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,chemin))).click()