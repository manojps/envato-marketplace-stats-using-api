import json
import requests
import os

#url='http://marketplace.envato.com/api/edge/item:10431404.json'
theme = open('theme_author.txt','r')
theme_id = theme.readlines()
total_theme = theme_id.__len__()

save_to_file = open('theme_author_data.txt','r+', buffering = -1)

i=0
while i < total_theme:
    url1 = 'http://marketplace.envato.com/api/edge/user:' + theme_id[i] + '.json'
    i += 1
#    data = requests.get(url1).text
#    data = json.loads(data)
    data = requests.get(url1).json()
    try:
        author = data ['user']['username']
    except TypeError:
        url = 'empty'
        pass
    print (url1)
    country = data ['user']['country']
    sales = data ['user']['sales']
    location = data ['user']['location']
    followers = data ['user']['followers']
    string = author+';'+sales+';'+country+';'+location+';'+followers+'\n'
    string_encode = string.encode('ascii','replace')
#        print(string_encode)
    string_decode = string_encode.decode('ascii','replace')
    save_to_file.write(string_decode)
    save_to_file.flush()
    os.fsync(save_to_file.fileno())


save_to_file.close()

