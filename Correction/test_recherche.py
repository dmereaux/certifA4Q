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
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.INFO)
driver=webdriver.Chrome()

def aller_sur_prestashop():
    driver.get("http://www.qualifiez.fr/monPrestashop2/prestashop/index.php")
def rechercher(item):
    driver.find_element_by_name('s').click()
    driver.find_element_by_name('s').clear()
    driver.find_element_by_name('s').send_keys(item+Keys.ENTER)
def renvoyer_message():
    wait = WebDriverWait(driver,10)
    texte = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#js-product-list-top > div.col-lg-5.hidden-sm-down.total-products > p"))).text
    return texte
def renvoyer_liste_lien():
    liste=driver.find_elements_by_xpath('//*[@id="js-product-list"]/div[1]/div/article/div/div[2]/h2/a')
    return liste
def selectionner_un_element(nb):
    driver.find_element_by_xpath('//*[@id="js-product-list"]/div[1]/div['+ str(nb) +']/article/div/div[1]/a/picture/img').click()

def test_recherche():
    # sur le site
    aller_sur_prestashop()
    # lancer une recherche sur MUG
    rechercher('mug')
    assert renvoyer_message()=="Il y a 5 produits."
    liste_Mug=renvoyer_liste_lien()
    for elt in liste_Mug:
        assert "Mug" in elt.text
    driver.quit()
