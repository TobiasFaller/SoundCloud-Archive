import soundcloud

# create a client object with your app credentials
client = soundcloud.Client(client_id='9fbbd1e3baad458473e7cf3f9334f43c')
base_url = 'https://soundcloud.com/oztrance/'

page_size = 200

# get first 100 tracks

print '########################################'

user = client.get('/resolve', url=base_url)
tracks = client.get('/users/%d/favorites' %user.id, limit=page_size, order='created_at')
num = 0
for track in tracks:
	num = num+1
	print '%d - %s' %(num, track.title)

print '********* TRANSITION **********'
# start paging through results, 100 at a time
#user = client.get('/resolve', url=base_url)
"""tracks = client.get('/users/%d/tracks' %user.id, limit=page_size, linked_partitioning=1, order='created_at')
for track in tracks:
    print track.title"""

tracks = client.get('/users/%s/favorites' %user.id, order='created_at', limit=page_size, linked_partitioning=1)

for track in tracks:
    print track.title

print '########################################'
