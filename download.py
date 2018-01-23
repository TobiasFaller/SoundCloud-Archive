#!/usr/bin/env python

#the sole purpose of this script is to take a url and figure out how to download it
#ID3 tagging will be added later (probably as it's own functional module)

import requests, soundcloud
import argparse

from clint.textui import colored, puts, progress


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

def archive_track(client, url, stream, download): #only requires raw url and client
	track_url = url
	track = client.get('/resolve', url=track_url) #url must be set as 'url='
	
	if (track.streamable == True):
		puts(colored.green(u'Streamable')) 
	else:
		puts(colored.red(u'Streamable')) 

	if (track.downloadable == True):
		puts(colored.green(u'Downloadable')) 
	else:
		puts(colored.red(u'Downloadable'))

	if track.streamable != True and stream:
		print 'skipping ...'
		return

	if track.downloadable != True and download:
		print 'skipping...'
		return

	if hasattr(track, 'stream_url'):
		track_stream = track.stream_url
	else:
		'parse that stream url on your own time son'
		return

	filename = get_meta(track)['title'] + '.mp3'
	print 'filename - %s' %filename
	stream_data = client.get(track_stream, allow_redirects=False)
	
	if hasattr(stream_data, 'location'):
		raw_stream_data = stream_data.location
	
	dl_stream(raw_stream_data, filename)
	print ('%s - archive successful\n') %filename


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Downloud soundcloud streams to your storage')
	parser.add_argument('-d', action='store_true', help='archive download stream')
	parser.add_argument('-s', action='store_true', help='archive listen stream')
	parser.add_argument('songs', metavar='link', nargs='+', help='song link(s)')

	args = parser.parse_args()

	CLIENT_ID = 'b1f93bc0faa7e0a4776bcf336eab5638' #needs to be a string
	client = soundcloud.Client(client_id=CLIENT_ID) #sc client is global
	stream = args.s
	download = args.d
	for song in args.songs:
		archive_track(client, song, stream, download)
