#this script only downloads things.  That's all it does

import requests
import os, sys
from os.path import exists #ensures download path is valid
import time

from clint.textui import puts, progress

def download_file(url, path):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()

    return path
