import os,logging
import pytest
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
driver=webdriver.Firefox()
@pytest.fixture
def setup_method():
    driver = webdriver.Firefox()

    base_url = "http://www.qualifiez.fr/monPrestashop2/prestashop/index.php"
    driver.get(base_url)
    driver.implicitly_wait(10)
    yield driver
    driver.close()



def aller_sur_prestashop():
    driver.get("http://www.qualifiez.fr/monPrestashop2/prestashop/index.php")

# page Header
def lancer_une_recherche(item):
    driver.find_element_by_name('s').click()
    driver.find_element_by_name('s').clear()
    driver.find_element_by_name('s').send_keys(item)
    driver.find_element_by_name('s').send_keys(Keys.ENTER)
# page recherche
def renvoyer_message():
    wait = WebDriverWait(driver,10)
    texte = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#js-product-list-top > div.col-lg-5.hidden-sm-down.total-products > p"))).text
    return texte
# page recherche
def renvoyer_liste_lien():
    liste=driver.find_elements_by_xpath('//*[@id="js-product-list"]/div[1]/div/article/div/div[2]/h2/a')
    return liste
# page recherche
def selectionner_un_element(nb):
    driver.find_element_by_xpath('//*[@id="js-product-list"]/div[1]/div['+ str(nb) +']/article/div/div[1]/a/picture/img').click()
# page element
def ajouter_au_panier():
    wait = WebDriverWait(driver,10)
    elt=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button')))
    try:
        driver.find_element_by_css_selector("#field-textField1").send_keys("mon message")
        driver.find_element_by_css_selector("#main > div.row.product-container.js-product-container > div:nth-child(2) > div.product-information > section > div > form > div > button").click()
        pass
    except NoSuchElementException:
        pass
    wait = WebDriverWait(driver,10)
    elt=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button')))
    elt.click()
def test_recherche_MUG(setup_method):
    # sur le site
    aller_sur_prestashop()
    # lancer une recherche sur MUG
    lancer_une_recherche('Mug')
     # vérification
    texte = renvoyer_message()
    assert texte=="Il y a 5 produits."
    liste=renvoyer_liste_lien()
    for elt in liste:
        assert "Mug" in elt.text 
    selectionner_un_element(1)
    ajouter_au_panier()
 #   driver.close()
def test_recherche_TShirt(setup_method):
    # sur le site
    driver=aller_sur_prestashop()
    # lancer une recherche sur MUG
    lancer_une_recherche('T-shirt')
     # vérification
    texte = renvoyer_message()
    assert texte=="Il y a 1 produit."
    liste=renvoyer_liste_lien()
    for elt in liste:
        assert "T-Shirt" in elt.text 
    selectionner_un_element(1)
    ajouter_au_panier()


