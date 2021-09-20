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

os.system("dropdb marstest")
os.system("createdb marstest")

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
        text = regex_curiosity.spock_to_space()
    elif rover_id == 2:
        text = regex_spirit.troi_to_Mars()
    elif rover_id == 3:
        text = regext_opportunity.captain_to_Mars()
    else:
        print('sorry please come back later')

    # #fix this for more posts later.

    date = datetime.strptime(missionpost["date"], "%Y-%m-%d")
    title=text["title"]
    text=text["quote"]+text["mission"]


    db_missionpost = crud.create_missionpost(rover_id, date, title, text)
    # print ("MAXXXXXXX")
    # print (max_post_id2)

    missionpost_in_db.append(db_missionpost)

 
with open ('data/photo.json') as f:
    photo_data = json.loads(f.read())


photo_in_db = []
for photo in photo_data['photos']:
    
    print (photo)
   
    photo_path  = photo ["img_src"]
    mission_id = crud.get_random_missionpost_id()
      
    db_photo = crud.create_photos(photo_path, mission_id)
    #the expression gets called first taking random mission post and getting hte mission id from it

 



 