import json
from pyairtable import Table

def sort_key(key):
    '''
    a func to give sort(key=) a key as a value of ID from the table for 
    correct sorting, because pyairtable sort it by some another way
    '''
    return key['ID']


def lambda_handler(event, context):
    
    # empty list to contain and sort data after
    table_values = []
    # define class from pyairtable Table('apikey', 'base_id', 'table_name')
    # these values should be encrypted or uploaded from secure source
    table = Table('keybQzHGFofRaGHfA', 'appDzh3RGwOHlRi8U', 'MainTable')

    for i in table.all():
        # we take only i['fields'], because we don't need stuff around it
        table_values.append(i['fields'])
        #print(i['fields'])

    table_values.sort(key=sort_key)
    #print(table_values)

    lich = int(event["rawQueryString"])

    val_3 = 0
    my_response = {}

    while val_3 < 3:
        if lich < len(table_values):
            my_response[lich] = table_values[lich]['title']
            lich += 1
            val_3 += 1

        if lich >= len(table_values) and val_3 < 3:
            lich = 0
            my_response[lich] = table_values[lich]['title']
            lich += 1
            val_3 += 1
    
    return {
        'statusCode': 200,
        'body': json.dumps(my_response)
    }
