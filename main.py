import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим текст ссылки, используя формулу для расшифровки
    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link_element = browser.find_element(By.LINK_TEXT, link_text)
    link_element.click()

    # Заполняем форму
    input1 = browser.find_element(By.TAG_NAME, "input[name='first_name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Для удобства копирования кода оставляем браузер открытым на некоторое время
    time.sleep(30)
    browser.quit()
