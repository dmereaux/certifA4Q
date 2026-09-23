import os,logging
import pytest
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

logging.basicConfig(level=logging.INFO)
driver=webdriver.Chrome()

@pytest.fixture
def my_setUpTearDown():
 #Setup
 logging.debug("setUP")
 yield
 #TearDown
 logging.debug("TearDown")
 driver.quit()

#Redirection vers la Page d'acceuil
def Aller_sur_la_page_accueil():
 driver.get("http://automationpractice.com/index.php")
 logging.info("URL :" + driver.current_url)
 logging.info("Titre :" + driver.title)
 driver.maximize_window()

#Rechecher un elemeent
def Rechercher(txt):
 logging.debug("------- Rechercher --------")
 search = driver.find_element_by_css_selector("#search_query_top")
 driver.get_screenshot_as_file("ScreenShots/Search.png")
 search.clear()
 search.send_keys(txt)
 driver.find_element_by_xpath("//*[@id='searchbox']/button").click()
 assert driver.title == "Search - My Store"

#Selectionner le Premier Element
def Selectionner_le_premier_element():
 logging.debug("------- Selectionner_le_premier_element --------")
  #ProductFaded = driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img')
 ProductFaded = driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[2]/h5/a')
 driver.get_screenshot_as_file("ScreenShots/ProductFaded.png")
 ProductFaded.click()
 sleep(5)

#Ajouter Element au Panier
def Ajouter_au_panier():
 logging.debug("------- Ajouter_au_panier --------")
 AddToCart = driver.find_element_by_xpath('//*[@id="add_to_cart"]/button')
 #AddToCart = driver.find_element_by_css_selector("#add_to_cart > button")
 driver.get_screenshot_as_file("ScreenShots/AddToCart.png")
 AddToCart.click()
 modal = driver.find_element_by_id("layer_cart")
 wait = WebDriverWait(modal,10)
 #Checkout = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@title="Proceed to checkout"]')))
 Checkout = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')))
 driver.get_screenshot_as_file("ScreenShots/Checkout.png")
 Checkout.click()
 print("The product in the list card")
 assert "SHOPPING-CART SUMMARY" in driver.find_element_by_xpath('//*[@id="cart_title"]').text
 assert "Order - My Store" == driver.title



def test_recherche_ajout():
 Aller_sur_la_page_accueil()
 Rechercher("chiffon")
 Selectionner_le_premier_element()
 Ajouter_au_panier()
 driver.quit()

if __name__=="__main__":
 test_recherche_ajout()
