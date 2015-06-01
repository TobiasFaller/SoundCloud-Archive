#!/usr/bin/env python

#primary driver for SoundCloud archive application

import soundcloud, requests, time
import random, pymongo, re

#local module dependencies go here:
import trackScrape

#setup database things with mongodb
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client.sc_database
user_sets = db['user_sets'] #stores <set urls> from soundcloud API


#soundcloud API setup
CLIENT_ID = 'b1f93bc0faa7e0a4776bcf336eab5638'
user_url = 'http://www.soundcloud.com/oztrance' #critical setting for script

client = soundcloud.Client(client_id=CLIENT_ID)

def main():
	user = client.get('/resolve', url=user_url)

	print ('\n%d sets found for user: %s | ID: %s\n') %(user.playlist_count, user.username, user.id)

	plst = ('/users/%s/playlists') %user.id
	all_sets = client.get(plst)

	for set in all_sets:
		print set.title + '  --  ' + set.permalink_url
		user_set = {
		"title": set.title,
		"href": set.permalink_url
		}
		db.user_sets.insert(user_set)
		print 'stored in DB'


	print '\nscraping...'
	for entry in fake_db:
		print ('scraping set - %s') %(str(entry[0][0]))
		trackScrape.scrape_track_urls(entry[0][1])

#just a test case
def trackTest():
	test_url = 'http://www.soundcloud.com/augustrosenbaum/film-cph-dox-official-festival?in=oztrance/sets/experimental'

	track = client.get('resolve', url=test_url)
	print track.title
	print track.user['username']
	print ('%d ms') %track.duration

#run the things
if __name__ == '__main__':
	main()
	print '\n>>> processing complete <<<'


