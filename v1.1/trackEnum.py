#!/usr/bin/python3.4.3
# Created by Alex Crisara on May 20, 2016 for SC-Archive v1.1
# This project is to be used for experimental purposes only ~ never to be used to download copyrighted content!

from objectpath import *
import requests

# test client_id
client_ID = 'b1f93bc0faa7e0a4776bcf336eab5638'
_testURL_ = 'https://soundcloud.com/oztrance/sets/synthy'

# take set url & return list of track
def getTracks(set_url, client_ID):
    # generate json get request from SoundCloud API
    json_url = 'http://api.soundcloud.com/resolve.json?url=' + set_url + '&client_id=' + client_ID
    # get raw JSON from API
    json_set = requests.get(json_url).json()

    # generate Tree from json
    respTree = Tree(json_set)
    track_ids = list(respTree.execute("$.*['tracks']['id']"))
    print('{} - tracks found!'.format(len(track_ids)))
    return {
        '_type' : 'user_playlist',
        '_setId': respTree.execute("$.*['id']"),
        '_setTitle' : respTree.execute("$.*['title']"),
        'tracks' : track_ids,
        'count' : len(track_ids) }
        

# tests
getTracks(_testURL_, client_ID)
print('tests finished')
