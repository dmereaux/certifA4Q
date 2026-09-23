import os,logging
from selenium import webdriver
from datetime import datetime
logging.basicConfig(level=logging.INFO)
driver=webdriver.Chrome()

def new_page(url):
    driver.get(url)
def take_screenshot():
    try:
        os.mkdir("./screenshots")
    except OSError:
        pass
    screenshot_name = ("./screenshots/" + driver.title.replace(" ","_") + datetime.now().strftime("%Y%m%d%H%M%S%f") + ".png")
    driver.get_screenshot_as_file(screenshot_name)
    logging.info("Screenshot de la page est stocké " + screenshot_name)
def test_3_3_4():
    logging.debug("running test_3_3_4")
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    take_screenshot()
    driver.maximize_window()
    take_screenshot()
    driver.switch_to.frame("iframeResult")
    take_screenshot()
    driver.find_element_by_css_selector('[onclick*="myFunction()"]')
    driver.switch_to.default_content()
    take_screenshot()
    assert "Tryit Editor" in driver.title
    driver.quit()
if __name__=="__main__":
    test_3_3_4()
