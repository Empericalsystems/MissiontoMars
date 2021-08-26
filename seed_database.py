"""Script to seed database."""

import requests
import os
import json
from random import choice, randint
from datetime import datetime
import regex_curiosity
import regex_spirit
import regext_opportunity

import crud
import model
import server

os.system("dropdb missiontest")
os.system("createdb missiontest")

model.connect_to_db(server.app)
model.db.create_all()


with open ('data/rover.json') as f:
    rover_data = json.loads(f.read())


rover_in_db = []
for rover in rover_data:
    rovername = (
        rover["rovername"]   
    )

    db_rover = crud.create_rover(rovername)
    rover_in_db.append(db_rover)

for n in range(10):
    email = f"user{n}@mars.com"   
    password = "space"

    user = crud.create_user(email, password)



with open ('data/missionpost.json') as f:
    missionpost_data = json.loads(f.read())


missionpost_in_db = []
for missionpost in missionpost_data:
    title = missionpost["title"]
    # text = regex_curiosity.twain_to_space()
    rover_id = missionpost["rover_id"]

    if rover_id == 1:
        text = regex_curiosity.twain_to_space()
    elif rover_id == 2:
        text = regex_spirit.twain_to_Mars()
    else:
        text = regext_opportunity.opportunity_to_Mars()

    # #fix this for more posts later.

    date = datetime.strptime(missionpost["date"], "%Y-%m-%d")

    db_missionpost = crud.create_missionpost(rover_id, title, text, date)

    missionpost_in_db.append(db_missionpost)

 
with open ('data/photo.json') as f:
    photo_data = json.loads(f.read())


photo_in_db = []
for photo in photo_data['photos']:
    
    print (photo)
   
    photo_path  = photo ["img_src"]
    mission_id = crud.get_random_missionpost_id()
        # photo ["photo_name"],   
    
        # photo ["missionpost_id"]
    # print (photo_path, mission_id)
    db_photo = crud.create_photos(photo_path, mission_id)
    #the expression gets called first taking random mission post and getting hte mission id from it

    photo_in_db.append(db_photo)

 