import re

import pandas as pd
import os
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
    return df

def get_field_link():
    save_field_link()
    connect = sqlite3.connect('C:/Users/adel.yakushev/Documents/GitHub/test_project/test.db')
    cursor = connect.cursor()
    cursor.execute('SELECT id_path FROM field')
    data = cursor.fetchall()
    connect.close()
    data_array = list(data)
    return data_array
# for elem in get_field_link():
#     print(elem[0])
# os.mkdir('field_dataset')
def make_dataset_folder():
    get_field_link()
    for row in save_field_link()[1]:
        if not os.path.exists('field_dataset\\'+str(row)+'_data'):
            print(row)
            os.mkdir(os.path.join('field_dataset', str(row)+'_data'))
    os.rename('C:/Users/adel.yakushev/Downloads/ndvi_field_180829_2023-04-18 (1).zip', 'field_dataset/1000010_data/ndvi_field_180829_2023-04-18 (1).zip')
make_dataset_folder()
# print(str(save_field_link()[1][3]))
