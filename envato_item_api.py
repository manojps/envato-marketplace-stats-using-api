import json
import requests
import os
import time

#url='http://marketplace.envato.com/api/edge/item:10431404.json'
theme = open('theme_id.txt','r')
theme_id = theme.readlines()
total_theme = theme_id.__len__()

save_to_file = open('theme_data_Apr05.txt','r+', buffering = -1)

i=0
while i < total_theme:
    url1 = 'http://marketplace.envato.com/api/edge/item:' + theme_id[i] + '.json'
    i += 1
#    data = requests.get(url1).text
#    data = json.loads(data)
    data = requests.get(url1).json()
    try:
        url = data ['item']['url']
    except TypeError:
        url = 'empty'
        pass
    print (url1)
#    print (url)
    themeforest = url.find('http://themeforest.net/')
    if themeforest != -1:
        item_id = data ['item']['id']
        item_name = data ['item']['item']
        user = data ['item']['user']
        sales = data ['item']['sales']
#        rating = data ['item']['rating']
        rating_decimal = data ['item']['rating_decimal']
        cost = data ['item']['cost']
        uploaded_on = data ['item']['uploaded_on']
        last_update = data ['item']['last_update']
        category = data['item']['category']
        tags = data ['item']['tags']
        string = item_id+';'+item_name+';'+user+';'+url+';'+sales+';'+cost+';'+rating_decimal+';'+uploaded_on+';'+last_update+';'+category+';'+tags+'\n'
        string_encode = string.encode('ascii','replace')
#        print(string_encode)
        string_decode = string_encode.decode('ascii','replace')
        save_to_file.write(string_decode)
        save_to_file.flush()
        os.fsync(save_to_file.fileno())
        #time.sleep(4)
    else:
        continue
    
print (item_no)

save_to_file.close()

