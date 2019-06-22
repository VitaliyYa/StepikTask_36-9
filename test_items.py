import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_product_button(browser):
    browser.get(link)
    assert WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[type = submit]:nth-child(3)"))
        ), 'There is no product add button'
    time.sleep(5)
