from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get('http://suninjuly.github.io/wait1.html')

    browser.find_element(By.ID, 'verify').click()
    message = browser.find_element(By.ID, 'verify_message').text

    assert "Verification was successful!" == message

finally:
    time.sleep(10)
    browser.close()
    browser.quit()
