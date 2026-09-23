import os,logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from page_recherche import *
from selenium.webdriver.common.keys import Keys
from Util import *
logging.basicConfig(level=logging.INFO)
class page_accueil():
    # LOCATORS
    loc_champ_recherche="//*[@id='search_widget']/form/input[2]"

    util = Util()
    # Initialisation du PO
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://prestashop.qualifiez.fr/")


    # Actions
    def rechercher(self, chaine):
        champRecherche=self.util.recherche_gen(self.driver,self.loc_champ_recherche)
        champRecherche.send_keys(chaine)
        champRecherche.send_keys(Keys.RETURN)
        return page_recherche(self.driver)

    def rechercherRien(self):
        champRecherche=self.util.recherche_gen(self.driver,self.loc_champ_recherche)
        champRecherche.send_keys(Keys.RETURN)
        return page_recherche(self.driver)

    # Contrôle





