"""Script to seed database."""

import requests
import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb missiontest")
os.system("createdb missiontest")

model.connect_to_db(server.app)
model.db.create_all()


def get_data():

    payload = {
        'api_key': 'HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE',
        'earth_date': '2004-09-25'
    }

    res = requests.get(
        'https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos', data=payload)

    for data in res.json()['items']:
        print(data['img_src'])
