#test file for enumerating playlists

import requests, os.path, soundcloud
import time


#encapsulated function for future use
def enumerate_plsts(client_id,base_url):
	#list all playlists for given user
	client = soundcloud.Client(client_id=client_id)
	user = client.get('/resolve', url=base_url)
	playlists = client.get('/users/%d/playlists' %user.id)
	
	for i in range(0,len(playlists)):
		print('%d - %s' %(i, playlists[i].title))

start_time = time.time() #start execution timer

#count tracks in playlist (can't identify track specific data)
def count_tracks(playlist):
	num_tracks = 0
	for track in playlist.tracks:
		num_tracks = num_tracks + 1
	return num_tracks

#Identify if 100% of tracks within playlist are currently streamable (avoid future archiving errors)
def stream_present(playlist):
	if playlist.streamable > 0:
		return 'Yes'
	else:
		return 'No'

def enumerate_tracks(playlist,client_id):
	client_tracks = soundcloud.Client(client_id=client_id)
	for trak in playlist.tracks:
			track = client.get('/resolve', url=track_url)
    		track = client_tracks.get('/tracks/%d' % track_id)
    		return track.title	

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
	print("%d - %s tracks | Streamable: %s ") %(i, count_tracks(playlists[i]), stream_present(playlists[i]))
print '+------------------------------------------+'

print 'Tracks in Playlist 0:'
enumerate_tracks(playlists[0],client_id)

print ("Completed in %s seconds") % (time.time() - start_time) #stop execution timer and report time