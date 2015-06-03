#!/usr/bin/env python

'''
*Purpose of this script is to take a url and figure out how to download it
*ID3 tagging will be added later (probably as it's own functional module)
*ID3 tagging will be applied to individual tracks in this module
*same tags used with ID3 (and those not included) will be written to DB and associated with track & set ID's
'''

import requests, soundcloud
import os, sys
import pymongo

from clint.textui import colored, puts, progress

CLIENT_ID = 'b1f93bc0faa7e0a4776bcf336eab5638' #needs to be a string
client = soundcloud.Client(client_id=CLIENT_ID) #sc client is global

TEST_URL = 'http://www.soundcloud.com/monotropa/fade-into-you-mazzy-star-cover'
TEST_URL1 = 'http://www.soundcloud.com/miumo/people'
TEST_URL2 = 'http://www.soundcloud.com/mickjenkinsmusic/rain-prod-kaytranada'

class _dir:         
      def __init__( self, newPath ):  
        self.savedPath = os.getcwd()
        os.chdir(newPath)

      def __del__( self ):
        os.chdir( self.savedPath )



def dl_stream(url, path):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()

    return path

def get_meta(track): #only requires track
	meta={}
	meta['title'] = track.title
	meta['artist'] = track.user
	meta['user_id'] = track.user_id
	meta['art_url'] = track.artwork_url #used to download cover art
	meta['duration'] = track.duration
	meta['genre'] = track.genre
	meta['tags'] = track.tag_list
	meta['upload_date'] = track.created_at
	meta['waveform'] = track.waveform_url #url to waveform png
	meta['bpm'] = track.bpm
	meta['playback_count'] = track.playback_count
	meta['isrc'] = track.isrc

	return meta

def archive_track(client, url, newPath): #only requires raw url and client
	track_url = url
	track = client.get('/resolve', url=track_url) #url must be set as 'url='
	if (track.downloadable == True):
		puts(colored.green(u'Downloadable')) 
	else:
		puts(colored.red(u'Downloadable')) 
	
	if (track.streamable == True):
		puts(colored.green(u'Streamable')) 
	else:
		puts(colored.red(u'Streamable')) 
		print 'skipping...'
		pass

	if hasattr(track, 'stream_url'):
		track_stream = track.stream_url
	else:
		'parse that stream url on your own time son'
		pass

	filename = get_meta(track)['title'] + '.mp3'
	print 'filename - %s' %filename
	stream_data = client.get(track_stream, allow_redirects=False)
	
	if hasattr(stream_data, 'location'):
		raw_stream_data = stream_data.location
	initPath = os.getcwd()
	print 'current path - %s' %initPath
	print 'navigating to dir - %s' %newPath
	#navigate to new directory
	os.chdir(newPath)
	dl_stream(raw_stream_data, filename)
	print ('%s - archive successful\n') %filename

	print 'navigating back to - %s' %initPath
	os.chdir(initPath)
	print 'returned to - %s' %os.getcwd()

#test case [ Works ]
#archive_track(client, TEST_URL2, '/Users/Alex/Documents/GitHub/SoundCloud-Archive/dl_tank')








