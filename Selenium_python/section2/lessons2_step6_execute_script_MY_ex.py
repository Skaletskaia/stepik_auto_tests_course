from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')

    # text чтобы взять именно значение и дальше работать с ним
    my_x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(my_x))
    browser.execute_script("window.scrollBy(0, 150);")

    for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', 'button.btn']:
        browser.find_element(By.CSS_SELECTOR, selector).click()


finally:
    time.sleep(10)
    browser.close()
    browser.quit()
