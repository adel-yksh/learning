from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import pandas as pd
import sqlite3
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
def save_field_link():
    df = pd.DataFrame(pd.read_excel(get_field_xlsx(download_dir['loaded_field_id'])).values)
    df['id_path'] = df.apply(lambda x:'https://operations.cropwise.com/fields/'+str(x[0])+'-'+str(x[1])+'/dashboards/satellite_images?satellite_date=2023-04-18&satellite=s2a', axis=1)
    connect = sqlite3.connect('C:/Users/adel.yakushev/Documents/GitHub/test_project/test.db')
    df[[0, 'id_path']].to_sql('field', connect, if_exists='replace',index=False)
    connect.close()
def get_field_link():
    save_field_link()
    connect = sqlite3.connect('C:/Users/adel.yakushev/Documents/GitHub/test_project/test.db')
    cursor = connect.cursor()
    cursor.execute('SELECT id_path FROM field')
    data = cursor.fetchall()
    connect.close()
    data_array = list(data)
    return data_array
try:
    browser = webdriver.Chrome()
    browser.get("https://operations.cropwise.com/d/users/sign_in")
    browser.implicitly_wait(10)
    browser.find_element(By.CSS_SELECTOR, '#user_email').send_keys("ilsur.sabiryanov@agrosila-holding.ru")
    browser.find_element(By.CSS_SELECTOR, '#user_password').send_keys("hLfuycFX")
    browser.find_element(By.CSS_SELECTOR, "#sign_in_button").click()
    browser.find_element(By.XPATH, "//a[contains(text(), 'Поля')]").click()
    browser.find_element(By.XPATH, "//a[contains(text(), 'Список полей')]").click()
    browser.find_element(By.CSS_SELECTOR, "#ToolTables_all_fields_table_1").click()
    browser.find_element(By.CSS_SELECTOR, "#download-fields-list").click()

    # ToolTables_all_fields_table_1
    browser.get("https://operations.cropwise.com/fields/180829-2635542/dashboards/satellite_images?satellite_date=2023-04-18&satellite=s2a")
    browser.find_element(By.CSS_SELECTOR, "#download-other-formats-buttons").click()
    browser.find_element(By.XPATH, "//a[contains(text(), 'Карта вегетации (NDVI, формат .shp)')]").click()
    browser.find_element(By.CSS_SELECTOR, "#download-other-formats-buttons").click()
    browser.find_element(By.XPATH, "//a[contains(text(), 'Карта вегетации (NDVI, формат .csv)')]").click()
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