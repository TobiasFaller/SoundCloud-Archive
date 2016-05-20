
# Created by Alex Crisara on August 29 2015 @15:09 in Snell Library
# this script downloads track streams to the host the archiver script is running on
# not sure how to do this directly to S3 so this script is a polished placeholder for local dl

import requests, soundcloud
from clint.textui import colored, puts, progress # makes console output pretty

CLIENT_ID = 'b1f93bc0faa7e0a4776bcf336eab5638' 
client = soundcloud.Client(client_id=CLIENT_ID) # sc client is global

TEST_URL1 = 'https://soundcloud.com/georgeclanton/runaways'

def  stream_dl(url, path):
	r = requests.get(url, stream=True)
	with open(path, 'wb') as f:
		total_length = int(r.headers.get('content-length'))
		for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
			if chunk:  # filter and remove keep-alive new chunks
				f.write(chunk)
				f.flush()

	return path

def get_meta(track): #only requires track
	meta={}
	meta['title'] = track.title
	meta['artist'] = track.user
	meta['user_id'] = track.user_id
	meta['art_url'] = track.artwork_url 
	meta['duration'] = track.duration
	meta['genre'] = track.genre
	meta['tags'] = track.tag_list
	meta['upload_date'] = track.created_at
	meta['waveform'] = track.waveform_url 
	meta['bpm'] = track.bpm
	meta['playback_count'] = track.playback_count
	meta['isrc'] = track.isrc

	return meta

def archive_track(client, track_url): #only requires raw url and client
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
	
	stream_dl(raw_stream_data, filename)
	print ('%s - archive successful\n') %filename

archive_track(client, TEST_URL1)

def settags(track, filename, album='Soundcloud'):
    """
    Set the tags to the mp3
    """
    logger.info('Settings tags...')
    user = client.get('/users/{0.user_id}'.format(track), allow_redirects=False)

    artwork_url = track.artwork_url
    if artwork_url is None:
        artwork_url = user.avatar_url
    artwork_url = artwork_url.replace('large', 't500x500')
    urllib.request.urlretrieve(artwork_url, '/tmp/scdl.jpg')

    audio = mutagen.File(filename)
    audio['TIT2'] = mutagen.id3.TIT2(encoding=3, text=track.title)
    audio['TALB'] = mutagen.id3.TALB(encoding=3, text=album)
    audio['TPE1'] = mutagen.id3.TPE1(encoding=3, text=user.username)
    audio['TCON'] = mutagen.id3.TCON(encoding=3, text=track.genre)
    if artwork_url is not None:
        audio['APIC'] = mutagen.id3.APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover',
                                         data=open('/tmp/scdl.jpg', 'rb').read())
    else:
        logger.error('Artwork can not be set.')
    audio.save()
