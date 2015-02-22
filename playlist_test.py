#test file for enumerating playlists

import requests, os.path, soundcloud

def enumerate_plsts(client_id,base_url):
	#list all playlists for given user
	client = soundcloud.Client(client_id=client_id)
	user = client.get('/resolve', url=base_url)
	playlists = client.get('/users/%d/playlists' %user.id)
	print playlists


client_id = '9fbbd1e3baad458473e7cf3f9334f43c'
base_url = 'https://soundcloud.com/oztrance/'

client = soundcloud.Client(client_id=client_id)
user = client.get('/resolve', url=base_url)
playlists = client.get('/users/%d/playlists' %user.id)

for i in range(0,len(playlists)):
	print('%d - %s' %(i, playlists[i].title))