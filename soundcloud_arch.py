#the actual important standalone script
#the whole point of this is to archive my entire soundcloud, and log when things change

import requests
import bs4


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
	response = requests.get(url_plsts) #load target page with requests
	soup = bs4.BeautifulSoup(response.text)
	print [a.attrs.get()]
	
	

def main():
	scrape_playlists(url_base,url_plsts)

if __name__ == '__main__':
	main()


