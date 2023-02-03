from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')

    x_element = browser.find_element(By.CSS_SELECTOR, 'img[src="images/chest.png"]').get_attribute('valuex')

    response = browser.find_element(By.ID, 'answer')
    response.send_keys(calc(x_element))

    for selector in ['#robotCheckbox', '#robotsRule', 'button.btn']:
        browser.find_element(By.CSS_SELECTOR, selector).click()


finally:
    time.sleep(10)
    browser.quit()
