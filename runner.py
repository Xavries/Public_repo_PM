import requests
#from pyairtable import Table
import time

'''
# empty list to contain and sort data after
table_values = []
# define class from pyairtable Table('apikey', 'base_id', 'table_name')
table = Table('keybQzHGFofRaGHfA', 'appDzh3RGwOHlRi8U', 'MainTable')

for i in table.all():
    # we take only i['fields'], because we don't need stuff around it
    table_values.append(i['fields'])
'''

# I decided not to use pyairtable module in runner too and just 
# hard code the length value
# we can try to take the value from lambda func and pass it here

table_len = 14 #len(table_values)
lich = 0
krok = 3

while True:

    target_url = f'https://bsxhyz300b.execute-api.us-east-2.amazonaws.com/?{lich}'
    r = requests.get(target_url)
    print(r.json())
    if lich in range(table_len+1-krok, table_len+1):#[12, 13, 14]:
        lich = lich-table_len
    
    lich += krok
    time.sleep(1)
