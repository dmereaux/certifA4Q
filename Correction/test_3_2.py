import os,logging
import time
from selenium import webdriver

logging.basicConfig(level=logging.DEBUG)

def test_3_2():
    logging.debug("running test_3_2")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.python.org")
    print(driver.window_handles)
    driver.execute_script("window.open('https://www.python.org/doc/')")
    driver.execute_script("$(window.open('https://www.python.org/doc/'))")
    time.sleep(2)
    assert driver.title == "Welcome to Python.org"
    driver.quit()
if __name__=="__main__":
    test_3_2()
