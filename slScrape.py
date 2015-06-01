#!/usr/bin/env python
#just your average soundcloud scraper
#for selenium to see links properly urls MUST end with '/' and finds must be defined '=[]'


'''
Dev Plans:

- need to auto scroll to '::bottom' marker -> while(assert(bottom) != 1) keep scrolling
- write all this stuff to a DB to keep track of time_update & etc.

- very future plans ~ custom comment aggregation to save "cool" parts of tracks

This code is good but unfortunately it can't see all that it needs to

Will be recycled into trackScrape.py (still good things here)

'''

import lxml.html as lh
import re

from selenium import webdriver
from bs4 import BeautifulSoup

tries = 1

sets_url = 'http://www.soundcloud.com/oztrance/sets/'

def sele_sets(url):
	browser = webdriver.PhantomJS()
	browser.set_window_size(1024, 768)
	browser.get(url)
	content = browser.page_source
	browser.quit()
 	
 	print 'page source fetched'
	doc = lh.fromstring(content)
	soup = BeautifulSoup(content)
	print 'page source parsed'
	#print doc
	#print content
	#WORKED
	finds = []
	finds = (soup.find_all(attrs={'class': re.compile("soundTitle__title")}))
	print 'page elements extracted\n'
	return finds

def trim_meta(result):
	for set in range(len(result)):
		look = str(result[set])
		#print look
		setName = re.findall('<span class="">(.*\n?)</span>', look, re.MULTILINE)	
		#print setName
		setHref = str(result[set]['href'])
		setUrl = 'http://www.soundcloud.com' + setHref
		print ('%s -- %s') %(setName, setUrl)

#verify result is ok

print 'starting script\n'
result = sele_sets(sets_url)

if (len(result) < 1):
	while True:
		print 'running again...\n'
		result = sele_sets(sets_url)
		print '>>> re-run complete <<<'
		tries = tries + 1
		trim_meta(result)

		if (len(result) > 0):
			#THEN write to DB
			print ('Tried %d times') %tries
			break
else:
	trim_meta(result)
	print ('\nonly tried once')
	#write results to db


'''
for elt in doc.xpath('//a[(@class,"soundTitle__title sc-link-dark")]'):
    print elt
'''