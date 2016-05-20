# Created by Alex Crisara on August 29 2015 @15:01 EST in Snell Library
# This script crawls a SoundCloud User's playlists (sets) and likes storing them in a mongoDB schema
# This script is designed to run headlessly, hence, selenium and some fancy windowing tools are used

import sys, time
import pyMongo