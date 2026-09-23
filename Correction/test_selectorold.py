import os,logging
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep



driver=webdriver.Chrome()


@pytest.fixture
def my_setUp():
    logging.debug("setUP")
    yield
    driver.quit()    

#//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img


def aller_sur_la_page_accueil():
    driver.get("http://automationpractice.com/index.php")

# Page accueil
def Rechercher(item):
    search= driver.find_element_by_css_selector("#search_query_top")
    search.clear()
    search.send_keys(item)
    driver.find_element_by_xpath("//*[@id='searchbox']/button").click()

# Page Panier
def controle():
    return driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[1]').text


#Page recherche
def selectionner_le_premier_element():
    logging.info("fonction se")
    driver.find_element_by_xpath("//*[@id='center_column']/ul/li[1]/div/div[1]/div/a[1]/img").click()  

#Page element 
def Ajouter_au_panier():
    sleep(3)
    #driver.find_element_by_css_selector("#add_to_cart > button").click()
    WDW(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='add_to_cart']/button"))).click()
    modal = driver.find_element_by_id("layer_cart")
    WDW(modal,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a'))).click()



def test_recherche_ajout_chiffon():
    aller_sur_la_page_accueil()
    Rechercher("chiffon")
    selectionner_le_premier_element()
    Ajouter_au_panier()
    assert controle()== str(1)
    
 

if __name__=="__main__":
    test_3_2()
