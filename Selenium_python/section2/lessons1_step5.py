from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    my_input = browser.find_element(By.ID, 'answer')
    my_input.send_keys(y)

    check_box = browser.find_element(By.ID, 'robotCheckbox')
    check_box.click()
    radio_button = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radio_button.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
