#main application file for soundcloud archive

import soundcloud
import requests
import os, sys
import time
import blessed

#soundcloud API information
client_id = '9fbbd1e3baad458473e7cf3f9334f43c'
base_url = 'https://soundcloud.com/oztrance/'

page_size = 100

#only for data retrieval NOT archiving
def count_tracks(playlist):
	num_tracks = 0
	for track in playlist.tracks:
		num_tracks = num_tracks + 1
	return num_tracks
	

def enumerate_plsts(client_id, base_url):
	#list all playlists for given user
	client = soundcloud.Client(client_id=client_id)
	user = client.get('/resolve', url=base_url)
	playlists = client.get('/users/%d/playlists' %user.id)
	
	for i in range(0,len(playlists)):
		print('%d - %s - %d' %(i, playlists[i].title, count_tracks(playlists[i])))

def enumerate_likes(client_id, base_url, page_size):
	client = soundcloud.Client(client_id=client_id)
	url = base_url + 'likes/'
	
	#get initial set w/out linked partitioning
	tracks = client.get('/resolve', url=url, limit=page_size)
	for track in tracks:
		print track.title

	print '==================='
	#continue paging through
	tracks = client.get('/resolve', url=url, limit=page_size, linked_partitioning=1)
	for track in tracks:
		print track.title

	print '==================='
	tracks = client.get('/resolve', url=url, limit=page_size, linked_partitioning=2)
	for track in tracks:
		print track.title

	#num = 0;
	#for i, track in enumerate(tracks):
		#if isinstance(track, soundcloud.resource.Resource):
			#t_track = {}
			#t_track['title']=track.title
			#num = num + 1
			#print '%d  -- %s' %(num, track.title)

	

print '| Current Sets |'
enumerate_plsts(client_id, base_url)
print '*-----------------------------------------*'

print '| Current Likes |'
enumerate_likes(client_id, base_url, page_size)

