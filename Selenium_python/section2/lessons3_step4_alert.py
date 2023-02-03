from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    browser.switch_to.alert.accept()

    my_x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(my_x))
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()


finally:
    time.sleep(10)
    browser.close()
    browser.quit()