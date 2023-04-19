import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '100')
    )

    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)


    input2 = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    y = calc(input2)

    # Ваш код, который заполняет обязательные поля
    input2 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input2.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()