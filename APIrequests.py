import requests

from sys import argv
from pprint import pprint


# API_key = 'HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE'

payload = {
    'api_key' : 'HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE',
    'earth_date': '2004-09-25'
}


res = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?', params = payload)
print (res.json())

