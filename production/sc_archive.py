#!/usr/bin/env python

#primary driver for SoundCloud archive application
#test commit change
import soundcloud, requests, time
import random, pymongo, re

#local module dependencies go here:
import trackScrape
import download

#setup database things with mongodb
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017')
db = client.sc_database
user_sets = db['user_sets'] #stores <set urls> from soundcloud API
set_tracks = db['set_tracks'] #stores tracks found in user_sets (NOT ARCHIVED yet)


#soundcloud API setup (will be added to __init__.py at some point)
CLIENT_ID = 'b1f93bc0faa7e0a4776bcf336eab5638' 
user_url = 'http://www.soundcloud.com/oztrance' #critical setting for script

client = soundcloud.Client(client_id=CLIENT_ID)

def main():
	user = client.get('/resolve', url=user_url)

	print ('\n%d sets found for user: %s | ID: %s\n') %(user.playlist_count, user.username, user.id)

	plst = ('/users/%s/playlists') %user.id
	all_sets = client.get(plst)

	print '\n-----------------'
	print 'storing user sets'
	print '-----------------'
	for set in all_sets:
		user_set = {
		"title": set.title,
		"href": set.permalink_url
		}
		db.user_sets.insert(user_set)
		print set.title + '  --  ' + set.permalink_url

	print '\n---------------'
	print 'scraping tracks'
	print '---------------'

	cursor = db.user_sets.find(no_cursor_timeout=True)
	for item in cursor:
		titleRead= item['title']
		hrefRead = item['href']
		set_id = item['_id'] #for diagnostic purposes
		print ('\nscraping set \' %s \' @ %s\nhref -- %s') %(titleRead, set_id, hrefRead)
		trackScrape.scrape_track_urls(db, hrefRead, set_id) #associate user_set ID with each track found in set

	print '/nscraping complete -- %d tracks found' %db.set_tracks.count()

	print '\n--------------------'
	print 'downloading & tagging'
	print '---------------------'

	cursor = db.set_tracks.find(no_cursor_timeout=True)
	for item in cursor:
		originSetID = item['set ID']
		originSetID_str = str(originSetID)
		outdata = user_sets.find_one({"_id":ObjectId(originSetID)})
		print outdata['title']

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
	print '\n - processing complete -'


