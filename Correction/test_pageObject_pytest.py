import pytest
import os
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from page_accueil import *
from page_recherche import *

class TestRecherche():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_MUG(self):
         print("MUG")
         hp= page_accueil(self.driver)
         rp= hp.rechercher("Mug")
         assert rp.resultat()=="Il y a 5 produits."

    def test_rien(self):
         print("dress1")
         hp= page_accueil(self.driver)
         rp= hp.rechercherRien()
         assert   rp.msg_erreur() =="Aucun produit ne correspond à votre recherche"

    def test_nimporte_quoi(self):
        hp= page_accueil(self.driver)
        rp= hp.rechercher("xxxxxxxxxxxxxxxxxxxxxxxxx")
        assert   rp.msg_erreur() =="Aucun produit ne correspond à votre recherche"  , "msg erreur"
