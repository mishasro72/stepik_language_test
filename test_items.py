from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_button(driver):

   # browser = webdriver.Chrome()

    driver.get(BASE_URL)
    time.sleep(10)
    ADD_BUTTON = driver.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert ADD_BUTTON.is_displayed()


