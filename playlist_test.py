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


def count_tracks(playlist):
	num_tracks = 0
	for track in playlist.tracks:
		num_tracks = num_tracks + 1
	return num_tracks


#soundcloud API info
client_id = '9fbbd1e3baad458473e7cf3f9334f43c'
base_url = 'https://soundcloud.com/oztrance/'

client = soundcloud.Client(client_id=client_id)
user = client.get('/resolve', url=base_url)
playlists = client.get('/users/%d/playlists' %user.id)

#enumerate playlist titles
print '+------------------------------------------+'
print '| Title: |'
for i in range(0,len(playlists)):
	print('%d - %s' %(i, playlists[i].title))
print '+------------------------------------------+'

#enumerate playlist root url's
print '| URL |'
for i in range(0,len(playlists)):
	print('%d - %s' %(i, playlists[i].permalink_url))
print '+------------------------------------------+'

#enumerate tracks in playlists
print '| # Tracks |'
for i in range(0,len(playlists)):
	print('%d - %s tracks') %(i, count_tracks(playlists[i]))
print '+------------------------------------------+'
