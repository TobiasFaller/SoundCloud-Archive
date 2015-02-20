#Test program created by Alex Crisara on Sun 10.26.2014 @ 8:53 pm in Davenport Commons A
#The only purpose of this is to test Soundcloud API things...
#NOTE when installing things in virtualenv USE SUDO WITH PIP

import soundcloud
i = 1

# create client object with app and user credentials
client = soundcloud.Client(client_id='491887981f67eb79c3c7cefbeccfebf4',
                           client_secret='cc19c241769e2284da6a377452fce946',
                           username='oztran**',
                           password='soundoftheOZ**')

# print authenticated user's username
print "+---------------------+"
print "Active User - %s" %client.get('/me').username  #YUSS THIS WORKED
print "+---------------------+"
# get playlist
#so basically since the API already knows who you are just put '/playlists' before the name of the playlist
playlist = client.get('/playlists/')

# list tracks in playlist
for track in playlist.tracks:
    a = "%d - " %i 
    b = track['title']
    print a + b
    i = i + 1
