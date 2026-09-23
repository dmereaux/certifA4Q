import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from page_recherche import *
from Util import *
logging.basicConfig(level=logging.INFO)
class page_accueil():
    # LOCATORS
    loc_champ_recherche="//*[@id='search_widget']/form/input[2]"
    loc_bouton="//*[@id='search_widget']/form/button/i"
    util = Util()
    # Initialisation du PO
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://prestashop.qualifiez.fr/en/")


    # Actions
    def rechercher(self, chaine):
        champRecherche=self.util.recherche_gen(self.driver,self.loc_champ_recherche)
        champRecherche.send_keys(chaine)
        self.util.click_gen(self.driver,self.loc_bouton)
        return page_recherche(self.driver)

    def rechercherRien(self):
        boutonRecherche=self.driver.find_element_by_xpath(self.loc_bouton)
        boutonRecherche.click()
        return page_recherche(self.driver)

    # Contrôle





