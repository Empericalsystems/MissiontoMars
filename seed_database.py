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

with open ('data/photo.json') as f:
    photo_data = json.loads(f.read())


photo_in_db = []
for photo in photo_data:
    photo_name, photo_path, missionpost_id = (
        photo ["photo_name"],   
        photo ["photo_path"],
        photo ["missionpost_id"]
    )

    db_photo = crud.create_photos(photo_name, photo_path, missionpost_id)
    photo_in_db.append(db_photo)


with open ('data/missionpost.json') as f:
    missionpost_data = json.loads(f.read())


missionpost_in_db = []
for missionpost in missionpost_data:
    rover_id, title, text, date = (
        missionpost["rover_id"],
        missionpost["title"],
        missionpost["text"],
        missionpost["date"]
    )
    date = datetime.strptime(missionpost["date"], "%Y-%m-%d")

    db_missionpost = crud.create_missionpost(rover_id, title, text, date)
    missionpost_in_db.append(db_missionpost)

 


 