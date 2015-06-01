#!/usr/bin/env python

import lxml.html as lh
import re, time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

tries = 1
#endBool is 1 if end marker is found at bottom of page 
endBool = 0

sets_url = 'http://www.soundcloud.com/oztrance/sets/'
tracks_url = 'https://soundcloud.com/oztrance/likes/'

def scroll_to_end(browser):	
	elem = browser.find_element_by_tag_name("body")
	#theEnd = browser.find_element_by_class_name("paging-eof sc-border-light-top")
	#assert browser.find_element_by_xpath(".//div[@class='header__left left']")
	try:
		assert browser.find_element_by_xpath(".//div[@class='paging-eof sc-border-light-top']")
		print 'bottom found'
	except:
		print 'end not found'
		pgDown = 0;
		while True:
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			#elem.send_keys(Keys.PAGE_DOWN)
			time.sleep(0.1)
			try:
				assert browser.find_element_by_xpath(".//div[@class='paging-eof sc-border-light-top']")
				print 'end found'
				break
			except:
				pgDown += 1
				print pgDown
				browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				pgDown += 3

				if (pgDown > 10):
					for i in range(0, 1000):
						browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
						pgDown += 1
						time.sleep(0.1)
						print pgDown
						if pgDown > 200:
							break

			if pgDown > 200:
				break
	if pgDown > 200:
		pass

def sele_sets(url):
	browser = webdriver.PhantomJS()
	browser.set_window_size(1024, 4032)
	browser.get(url)

	#scroll through entire page
	scroll_to_end(browser)

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
		trackName = str(re.findall('<span class="">(.*\n?)</span>', look, re.MULTILINE))
		trackUrl = 'http://www.soundcloud.com' + result[set]['href']
		print ('%s -- %s') %(trackName, trackUrl)
		


result = sele_sets(tracks_url)

if (len(result) < 1):
	while True:
		print 'running again...\n'
		result = sele_sets(tracks_url)
		print '>>> re-run complete <<<'
		tries = tries + 1
		trim_meta(result)

		if (len(result) > 0):
			#THEN write to DB
			print ('Tried %d times') %tries
			print ('The End - %d') %endBool
			break
else:
	trim_meta(result)
	print ('\nonly tried once')
	print ('The End - %d') %endBool
	print ('%d - tracks found') %(len(result))
	#write results to db

'''
*footnotes* needs functionality to identify if url is 'set' if so (scrape set links to same DB)
'<div class="l-footer sc-text-verylight sc-border-light-top">' AT bottom of
'''

	