#/usr/bin/python3.4.3

import soundcloud
import requests

CLIENT_ID = 'b1f93bc0faa7e0a4776bcf336eab5638'
CLIENT_SECRET = '868315eb8d295487d73be9c000922f94'
client = soundcloud.Client(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri='www.alexcrisara.com')
redirect(client.authorize_url())

print('auth - GOOD')
