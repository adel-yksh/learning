from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    people_radio = browser.find_element(By.CSS_SELECTOR, "#treasure")
    people_checked = people_radio.get_attribute("valuex")
    print("value of people radio: ", people_checked)

    # x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = people_checked
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option1.click()
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()