from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

download_dir = {
    'loaded_field_id':'C:/Users/adel.yakushev/Downloads/'
}
def get_field_xlsx(file_dir):
    max_value = 0
    for file in os.listdir(file_dir):
        if file.startswith('#field'):
            file_int = int(file.split('.')[0].split('-')[1])
            if file_int > max_value:
                max_value = file_int
                youngest_file = file
            else:
                continue
    return (file_dir+youngest_file).replace('/', '\\')
print(get_field_xlsx(download_dir['loaded_field_id']))

try:
    browser = webdriver.Chrome()
    browser.get("https://operations.cropwise.com/d/users/sign_in")
    browser.implicitly_wait(10)
    # time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, '#user_email').send_keys("ilsur.sabiryanov@agrosila-holding.ru")
    # time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '#user_password').send_keys("hLfuycFX")
    # time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "#sign_in_button").click()
    # time.sleep(1)

    browser.find_element(By.XPATH, "//a[contains(text(), 'Поля')]").click()
    browser.find_element(By.XPATH, "//a[contains(text(), 'Список полей')]").click()
    browser.find_element(By.CSS_SELECTOR, "#ToolTables_all_fields_table_1").click()
    browser.find_element(By.CSS_SELECTOR, "#download-fields-list").click()

    # ToolTables_all_fields_table_1
    time.sleep(10)



    # elements = browser.find_elements(By.TAG_NAME, "input")
    # for element in elements:
    #     element.send_keys("Мой ответ")


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла