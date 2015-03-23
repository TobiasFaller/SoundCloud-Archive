import soundcloud
from blessed import Terminal
t = Terminal()
import arrow
import os, sys

import Tkinter as tk
import tkFileDialog as tkD

time = arrow.utcnow().format('HH:mm:ss')

set = [0,1,2,3,4,5]

def print_set(arr):
	for i in range(0,(len(arr))):
		print i

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
		print('  %-5d%-17s%-12d' %(i, playlists[i].title, count_tracks(playlists[i]))) #formatting for tabbed table output

#general information
base_url = 'https://soundcloud.com/oztrance/'
client_id = '9fbbd1e3baad458473e7cf3f9334f43c'

client = soundcloud.Client(client_id=client_id)
user = client.get('/resolve', url=base_url)

sc_user = user.username
sc_user_id = user.id
sc_playlist_ct = user.playlist_count
sc_likes = user.public_favorites_count
dl_path = os.path.dirname(os.path.realpath(__file__))


print("press 'q' to quit.")
with t.cbreak():
    val = None
    while val not in (u'q', u'Q',u'\x1b[3~'): #exit if KEY_DELETE is pressed
        with t.fullscreen():
    		print(t.bold(t.standout(' Soundcloud Archive Tool 0.01 ')) + '  ~  %s  ~  ' %time) #title bar
    		#top information section
    		print(t.bold(' User ----------> ') + ' %s' %sc_user) #soundcloud user
    		print(t.bold(' User ID -------> ') + ' %s' %sc_user_id) #user ID
    		print(t.bold(' Playlists ct.--> ') + ' %s' %sc_playlist_ct) #user playlist count
    		print(t.bold(' Likes ct. -----> ') + ' %s' %sc_likes) #user likes count
    		print(t.bold(' Download Path -> ') + ' %s' %dl_path) #path to download files to
    		print(' API id: %s' %client_id)

    		print(t.move_y(t.height/4) + t.bold(t.standout(' Current Sets ')))
    		print(t.bold('| %-5s%-15s%-8s|' %('ID', 'Title', 'Track Ct.')))
    		enumerate_plsts(client_id, base_url)

    		while val in (u'd',):
				dl_path = tkD.askdirectory()
				root = tk.Tk()
				root.withdraw()
    		
    		with t.location(0, t.height - 2):
    			print(t.center('| A) Total Archive ~ U) Update Archive ~ D) Update dl path ~ press DEL to exit|'))


        val = t.inkey()
        #do important things here I guess?
    print('script closed sucessfully')


    #(t.move_y(t.height/2)
   	#print('some terminals {standout} more than others'.format(standout=t.green_reverse('standout')))