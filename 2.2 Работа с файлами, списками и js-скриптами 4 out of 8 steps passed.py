import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
y = calc(x)
input1 = browser.find_element(By.TAG_NAME, "input")
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)

input2 = browser.find_element(By.CSS_SELECTOR, '#answer')
input2.send_keys(y)

option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
option1.click()

option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
option2.click()
# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()
button.click()
time.sleep(5)

# // javascript
# button = document.getElementsByTagName("button")[0];
# button.scrollIntoView(true);
