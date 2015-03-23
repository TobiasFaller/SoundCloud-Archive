#the actual important standalone script
#the whole point of this is to archive my entire soundcloud, and log when things change

import requests

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

#soundcloud api info (HTTP api not Python API)
client_id = '9fbbd1e3baad458473e7cf3f9334f43c'
client_secret = 'c98e6764e1adb8c4ccd2904dfdcacac6'

#test output
print '+-----------------------+'
print ('Base (w/ user) -> %s') %url_base
print ('Likes ----------> %s ') % url_likes
print ('Playlists ------> %s') %url_plsts
print ('Current User ---> %s') %(user)
print '+-----------------------+'

#other functions

def enumerate_plsts():
#use soundcloud HTTP api to find numer & names of playlists

 

def main():


if __name__ == '__main__':
	main()



