#!/usr/bin/env python

'''
this module is only used for scraping tracks INSIDE identified sets
flow: 
set_url -> THIS MODULE -> enumerates tracks and writes to DB
'''

import lxml.html as lh
import re, time
import pymongo

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

track_tries = 1

#sets_url = 'http://www.soundcloud.com/oztrance/sets/'
#tracks_url = 'https://soundcloud.com/oztrance/sets/experimental/'


def scroll_to_eof(browser):	
	elem = browser.find_element_by_tag_name("body")
	#theEnd = browser.find_element_by_class_name("paging-eof sc-border-light-top")
	#assert browser.find_element_by_xpath(".//div[@class='header__left left']")
	try:
		assert browser.find_element_by_xpath(".//div[@class='paging-eof sc-border-light-top']")
		print '- eof found -'
	except:
		print '- eof NOT found -'
		pgDown = 0;
		while True:
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			#elem.send_keys(Keys.PAGE_DOWN)
			time.sleep(0.1)
			try:
				assert browser.find_element_by_xpath(".//div[@class='paging-eof sc-border-light-top']")
				print '- eof found -'
				break
			except:
				pgDown += 1
				print ('EXCEPTION - trying again...')
				browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				pgDown += 3

				if (pgDown > 10):
					for i in range(0, 100):
						browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
						pgDown += 1
						time.sleep(0.1)
						print pgDown
						if pgDown > 200:
							break
		

def sele_tracks(url):
	browser = webdriver.PhantomJS()
	browser.set_window_size(1024, 4032)
	browser.get(url)

	#scroll through entire page
	scroll_to_eof(browser)

	content = browser.page_source
	browser.quit()
 	
 	print 'page fetched'
	doc = lh.fromstring(content)
	soup = BeautifulSoup(content)
	print 'page indexed'
	
	#WORKED
	finds = []
	finds = (soup.find_all(attrs={'class': re.compile("__trackTitle")}))
	print 'page elements extracted\n'
	return finds


def trim_track_meta(db, result, set_id):
	for set in range(len(result)):
		look = str(result[set])
		found_track = {}
		found_track['title'] = result[set].contents[0]
		#trackUrl = 'http://www.soundcloud.com' + result[set]['href']
		found_track['href'] = result[set]['href']
		print ('%d -- %s  --  %s') %((set+1), found_track['title'], found_track['href'])
		set_track = {
		"title": found_track['title'],
		"href": found_track['href'],
		"set ID": set_id #id to associate with origin set
		}
		db.set_tracks.insert(set_track)
		

def scrape_track_urls(db, href_to_scrape, set_id):
	print 'starting script\n'
	result = sele_tracks(href_to_scrape)

	if (len(result) < 1):
		while True:
			print 're-attempt...\n'
			result = sele_tracks(href_to_scrape)
			print '>>> re-attempt complete <<<'
			trim_track_meta(db, result, set_id) 

			if (len(result) > 0):
				print 'tracks found successfully'
				break
	else:
		trim_track_meta(db, result, set_id)
		print ('\nfirst attempt GOOD')
		print ('%d - tracks identified') %(len(result))



'''
"trackItem__trackTitle sc-link-dark sc-type-h3" USE FOR CORRECT HREF
'soundTitle__title sc-link-dark '
'''