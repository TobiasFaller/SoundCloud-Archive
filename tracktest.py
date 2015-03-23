import soundcloud
import requests

from clint.textui import progress

client_id = '9fbbd1e3baad458473e7cf3f9334f43c'
base_url = 'https://soundcloud.com/oztrance/'

#from url

track_url = 'https://soundcloud.com/italdredrecords/al-rusty' #static value for testing
filename = 'attempt.mp3'

client = soundcloud.Client(client_id=client_id) #api endpoint
track = client.get('/resolve', url=track_url) #resolve id of track?

stream_url = client.get(track.stream_url, allow_redirects=False)

location = stream_url.location #preferred format

location_a = stream_url.url #alternative format if .location is not available

print 'value -> %s' %track.title

print 'value -> %s' %location

def download_file(url, path):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()

    return path

download_file(location_a, filename)

print 'process complete'

