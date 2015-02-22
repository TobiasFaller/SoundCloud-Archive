#just a script to test the soundcloud HTTP api

from blessed import Terminal
t = Terminal()

import requests
import json

#soundcloud api info (HTTP api not Python API)
client_id = '9fbbd1e3baad458473e7cf3f9334f43c'
client_secret = 'c98e6764e1adb8c4ccd2904dfdcacac6'

#test request to enumerate playlists via HTTP api
payload = {'9fbbd1e3baad458473e7cf3f9334f43c'} #client_id

url = 'http://api.soundcloud.com/users/58608651/playlists.json?client_id=9fbbd1e3baad458473e7cf3f9334f43c'
headers = {'Content-Type': 'application/json'}

filters = [dict(name='title', op='like', val='%y%')]
params = dict(q=json.dumps(dict(filters=filters)))

r = requests.get(url, params=params, headers=headers)
assert response.status_code == 200
print(response.json())

#r = requests.get(url, headers=headers)
r_out = r.json()
r_out = str(r_out)
print 'printing to file...'

json_output = open("json_output.txt", "w")

json_output.write(r_out)
json_output.close()
print 'export completed'



#use this command to identify user {id} -- user id for 'oztrance' : 58608651
#curl -v 'http://api.soundcloud.com/resolve.json?url=http://soundcloud.com/oztrance&client_id=9fbbd1e3baad458473e7cf3f9334f43c

//*[@id="content"]/div/div/div[2]/div/div[2]/div[2]/ul/li[1]/div/div[1]/div[1]/div[2]/div[2]/a/span