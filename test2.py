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
df = pd.DataFrame(pd.read_excel(get_field_xlsx(download_dir['loaded_field_id'])).values)
# print(df.iloc[:, 0])
df['id_path'] = df.apply(lambda x:'https://operations.cropwise.com/fields/'+str(x[0])+'-'+str(x[1])+'/dashboards/satellite_images?satellite_date=2023-04-18&satellite=s2a', axis=1)
# print(df[1])

connect = sqlite3.connect('C:/Users/adel.yakushev/Documents/GitHub/test_project/test.db')
df[[0, 'id_path']].to_sql('number', connect, if_exists='replace',index=False)
# print(df['id_path'])


