from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)




    x = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    y = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(x+y))  # ищем элемент с текстом "Python"

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