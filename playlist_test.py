#test file for enumerating playlists

import requests, os.path, soundcloud

#encapsulated function for future use
def enumerate_plsts(client_id,base_url):
	#list all playlists for given user
	client = soundcloud.Client(client_id=client_id)
	user = client.get('/resolve', url=base_url)
	playlists = client.get('/users/%d/playlists' %user.id)
	
	for i in range(0,len(playlists)):
		print('%d - %s' %(i, playlists[i].title))

#soundcloud API info
client_id = '9fbbd1e3baad458473e7cf3f9334f43c'
base_url = 'https://soundcloud.com/oztrance/'

client = soundcloud.Client(client_id=client_id)
user = client.get('/resolve', url=base_url)
playlists = client.get('/users/%d/playlists' %user.id)

print '+------------------------------------------+'
print '| Raw Title: |'
for i in range(0,len(playlists)):
	print('%d - %s' %(i, playlists[i].title))
print '+------------------------------------------+'

print '| Raw URL |'
for i in range(0,len(playlists)):
	print('%d - %s' %(i, playlists[i].permalink_url))
print '+------------------------------------------+'
