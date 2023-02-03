from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    for selector in ['.form-group [name="firstname"]', '.form-group [name="lastname"]', '.form-group [name="email"]']:
        browser.find_element(By.CSS_SELECTOR, selector).send_keys('Test')

    with open("file.txt", "w") as file:
        content = file.write("automationbypython")  # create file.txt file




    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.ID, 'file').send_keys(file_path)





    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()


finally:
    time.sleep(10)
    browser.quit()
