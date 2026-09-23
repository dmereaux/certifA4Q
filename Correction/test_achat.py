import os,logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logging.basicConfig(level=logging.DEBUG)
URL="http://prestashop.qualifiez.fr/"
LOCATOR_ITEM = "//*[@id='content']/section[1]/div/div[1]/article/div/div[1]/a/picture/img"

def find_generique(driver,chemin):
    logging.info("je cherche l'element: " + chemin)
    elt = driver.find_element_by_xpath(chemin)

    return elt

def aller_sur_la_page(driver,url):
    driver.get(url)

def selectionner_un_item(driver,chemin):
    driver.find_element_by_xpath(chemin).click()

def ajouter_au_panier(driver):
    driver.find_element_by_xpath('//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()

def proceder_aux_achats(driver):
    wait=WebDriverWait(driver,10)
    modal=wait.until(EC.visibility_of_element_located((By.ID,"blockcart-modal")))
    #modal=driver.find_element_by_id("blockcart-modal")
    modal.find_element_by_xpath('//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/a').click()


def retourner_le_titre_de_la_page(driver):
    return driver.title


# chercher le MUG
def test_modal():
    logging.debug("running test_modal")
    driver = webdriver.Chrome()

    aller_sur_la_page(driver,URL)
    selectionner_un_item(driver,LOCATOR_ITEM)
    ajouter_au_panier(driver)
    proceder_aux_achats(driver)
    assert retourner_le_titre_de_la_page(driver)=="Panier"



if __name__=="__main__":
    test_modal()

