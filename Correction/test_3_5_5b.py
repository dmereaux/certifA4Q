import os,logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


logging.basicConfig(level=logging.DEBUG)

def find_generique(driver,chemin):
    logging.info("je cherche l'element: " + chemin)
    elt = driver.find_element_by_xpath(chemin)
    return elt

# chercher le MUG
def test_3_5_5():
    logging.debug("running test_3_5_5")
    driver = webdriver.Chrome()
    # page
    driver.get("http://prestashop.qualifiez.fr/")
    find_generique(driver, "//*[@name='s']").send_keys("MUG")
    find_generique(driver, "//*[@name='s']").get_property('value')
    find_generique(driver, "//*[@name='s']").send_keys(Keys.RETURN)
    elt = find_generique(driver,'//*[@id="js-product-list-top"]/div[1]/p')
    logging.info(elt.is_displayed())
    logging.info(elt.get_attribute("outerHTML"))
    assert  elt.text == "Il y a 5 produits."

# check des box
def test_3_5_6():
    logging.debug("running test_3_5_6")
    driver = webdriver.Chrome()
    driver.get("http://www.qualifiez.fr/monPrestashop2/prestashop/index.php?id_product=1&id_product_attribute=3&rewrite=hummingbird-printed-t-shirt&controller=product#/2-taille-m/8-couleur-blanc")
    assert find_generique(driver, '//*[@id="group_2"]/li[1]/label/input').is_selected() == True
    find_generique(driver, '//*[@id="group_2"]/li[2]/label/input').click()
    assert find_generique(driver, '//*[@id="group_2"]/li[2]/label/input').is_selected() == True
    assert find_generique(driver, '//*[@id="group_2"]/li[1]/label/input').is_selected() == False
    driver.quit()



if __name__=="__main__":
    test_3_5_5()
    test_3_5_6()
