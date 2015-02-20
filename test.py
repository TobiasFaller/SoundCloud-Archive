#the actual important standalone script
#the whole point of this is to archive my entire soundcloud, and log when things change

import requests
from lxml import html

from blessed import Terminal
t = Terminal()


#baseline variables for scraping
url_null = 'http://www.soundcloud.com/' #generic web address
user = 'oztrance' #change to specific user to archive
arch_path = 'path/to/archive/location' #path to location where archive will be stored

#sub url definitions
url_base = url_null + user + '/' # '/' is important
url_likes = url_base + 'likes' #url for likes
url_plsts = url_base + 'sets' #url for playlists

#test output
print '+-----------------------+'
print ('Base (w/ user) -> %s') %url_base
print ('Likes ----------> %s ') % url_likes
print ('Playlists ------> %s') %url_plsts
print ('Current User ---> %s') %(user)
print '+-----------------------+'

#other functions

def scrape_playlists(url_base,url_plsts):
	print 'starting to scrape playlists'
	page = requests.get(url_plsts) #load target page with requests
	tree = html.fromstring(page.text) #translate target page into text tree

	#list of plsts names '<span class>Smooth R&B</span>'
	#list of target urls (to scrape individually) '<a class="soundTitle__title sc-link-dark " href="/oztrance/sets/smooth-r-b">

	playlists = tree.xpath('//span[@class="class"]/text()')
	print 'Playlists:', playlists

def main():
	scrape_playlists(url_base,url_plsts)

if __name__ == '__main__':
	main()