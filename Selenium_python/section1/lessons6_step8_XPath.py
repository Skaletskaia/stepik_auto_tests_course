from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys('Nastya')
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Scaletchi")
    input3 = browser.find_element(By.NAME, 'firstname')
    input3.send_keys('Amsterdam')
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys('Nederland')
    my_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    my_button.click()

finally:
    time.sleep(30)
    browser.quit()
