#!/usr/bin/env python

#link generator to start scraping process
#will eventually use DB to store these links 

import re, urllib2

from bs4 import BeautifulSoup
from time import sleep
import requests

username = 'oztrance'
base_url = 'https://www.soundcloud.com/'

likes_url = base_url + username + '/likes/'

sets_url = base_url + username + '/sets/'

def status(url):
	page = requests.get(url)
	status = page.status_code
	return status

print ('\nLikes URL -- %s') %likes_url
print ('page status - %d') %status(likes_url)

print ('\nSets URL -- %s') %sets_url
print ('page status - %d') %status(sets_url)

print ('\nFinding playlist URLS...')

page = urllib2.urlopen(sets_url)
soup = BeautifulSoup(page.read())
finds = (soup.find_all(attrs={'class': re.compile("soundTitle")}))

print finds

#bs4 is having issues, might just be too much JS
