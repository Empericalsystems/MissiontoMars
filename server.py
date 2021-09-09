
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
import regex_spirit
import regex_curiosity
import regext_opportunity
import mission_log
import random
import titles_ran
from werkzeug.security import generate_password_hash, check_password_hash



from jinja2 import StrictUndefined

import os
import requests
import pprint 


app = Flask (__name__)
app.secret_key = 'nosecret'
app.jinja_env.undefined = StrictUndefined
api_key = os.environ.get('NASA_API_KEY')

class MissionPost_live:
    def __init__(self, rover_id, title, quote, mission):
        self.rover_id = rover_id
        self.title = title
        self.quote = quote
        self.mission = mission


@app.route('/')
def homepage():
    """LandingPage - mission details."""
    return render_template('homepage.html')


@app.route('/rover/<rover_id>', methods = ['GET','POST'])
def log_rover(rover_id):
    """Each rover's Mission log"""

    rover_posts = crud.get_posts_by_rover(rover_id)
    name_var = crud.get_rover_name_by_id(rover_id)

    if request.method == 'POST':
        rover_date = request.form.get('date')
    else:
        if rover_id == '1':
            rover_date = '2013-09-23'
        elif rover_id == '2':
            rover_date = '2005-08-03'
        else:
            rover_date = '2006-09-03'


    print ("THIS IS A TEST*************") 
    print (rover_date)
    print (name_var)
    print (request.method)
    print ('******************checking the photos&&&&&&&&&&&&&&&&&&&')


    return render_template('rover_posts.html',
                           rover_posts = rover_posts,
                           r_name = name_var,
                           r_id = rover_id,
                           rover_datetext = rover_date
                           )

@app.route('/new_date/<rover_id>', methods = ['GET','POST'])


def show_user_choice(rover_id):
    """Post mission from date chosen by user"""

    rover_date = request.form.get('date')
    rover_blogpost_text=""
    int_date = rover_date.split('-')
    int_date = ''.join(int_date[0]).join(int_date[1]).join(int_date[2])

    print ('££££££££££££££££')
    print (int_date)

   
    # random.seed(int(int_date))  #turn this into a number and give it to seed and randomly pick from listof posts

    # rover_blogpost = [random.choice(crud.get_posts_by_rover(rover_id))] #this returns a list - call 
    # print(rover_blogpost, type(rover_blogpost))


    if rover_id == "1":
        rover_blogpost_text = regex_curiosity.spock_to_space()
    elif rover_id == "2":
        rover_blogpost_text = regex_spirit.troi_to_Mars()
    elif rover_id == "3":
        rover_blogpost_text = regext_opportunity.captain_to_Mars()
    else:
        print('sorry please come back later')
     
    
    # date_database_check = crud.get_posts_by_date(rover_date) 
    # if date_database_check == []:
    #     date_database_check = MissionPost_live(rover_id, rover_blogpost_text['title'], rover_blogpost_text['quote'], rover_blogpost_text['mission'])
    # # else: 
        # rover_blogpost_missionlive == get_posts_by_date(rover_date)
        
#if conditional statment here to check if the date chosen by the user is alreayd in the database XXXX
    # print (type(rover_blogpost), rover_blogpost)

    rover_blogpost_missionlive = MissionPost_live(rover_id, rover_blogpost_text['title'], rover_blogpost_text['quote'], rover_blogpost_text['mission'])
    #packing info into a class   
    
    print ('SECOND TESTS!!!!!!@@@@@@@@@@@@@@@')
    # print (rover_blogpost.rover_id)
    # print (rover_blogpost.title)
    # print (rover_blogpost.quote)
    # print (rover_blogpost.mission)
    # print (type(rover_blogpost))

    name_var = crud.get_rover_name_by_id(rover_id) #this can stay because we pull from database


    # print (crud.get_posts_by_rover(rover_id))


    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{name_var.lower()}/photos?'
    payload = {
      'api_key' : api_key,
      'earth_date': rover_date
    }

    res = requests.get(url, params = payload)

    api_data = res.json() 

    # print (data['photos'][0]['img_src'])
    # print("$$$$$$$$$$$API DATA")
    # print(type(api_data),api_data)

    picture_path = api_data['photos']

    if picture_path == []:
        flash ('Sorry there is no image for this date. Please try again.')
    else:
        picture_path = api_data['photos'][0]['img_src']
        date = rover_date
        title = rover_blogpost_text['title']
        text = rover_blogpost_text['quote'] + rover_blogpost_text['mission']
        db_missionpost = crud.create_missionpost(rover_id, date, title, text)
        max_post_id2 = crud.get_max_missionpost_id()
        db_photo = crud.create_photos(picture_path, max_post_id2)

    # print ("******&&&&&&&&&&&&&&&&&&&&&&**********")
    # # print (crud.get_post_by_id(missionpost_id))
    # print ("******&&&&&&&&&&&&&&&&&&&&&&**********")

    return render_template('chosen_date.html',
                           
                        #    rover_posts = rover_blogpost,
                           rover_posts_live = rover_blogpost_missionlive,
                           r_name = name_var,
                           r_id = rover_id,
                           rover_datetext = rover_date,
                           pics = picture_path,
                           data = api_data
                           )    #red matches html


@app.route('/users', methods = ['POST'])
def register_new_user():
    """Create a new user"""
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = crud.get_user_by_email(email)
    if user:
        flash('This email already exists. Please login.')
    else: 
        crud.create_user(email, password)
        flash('Your account has been created! Please login.')

    return redirect ('/')

@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details of a  user."""

    user = crud.get_user_by_id(user_id)
    return render_template("user_details.html", user=user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    """User login."""
    
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        if user.password == password:
        # check_password_hash(user.password, pwhash, password):
            session["user_email"] = user.email
            flash(f"Welcome back, {user.email}!")
    elif not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        flash("Sorry there appears to be an error with your login. Please try again later.")

        # Log in user by storing the user's email in session
        
    return redirect("/")

@app.route('/logout')
def logout_user():
    session.pop('user_email')
    flash("Sorry to see you go.")
    return redirect("/")
    

if __name__ == '__main__':
    app.debug = True
    connect_to_db(app)
    app.run(host='0.0.0.0')

