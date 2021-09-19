from flask import Flask, render_template, request, flash, session, redirect, jsonify 
# from model import connect_to_db
from model import db, User, Rover, MissionPost, Photo, connect_to_db
import crud
import regex_spirit
import regex_curiosity
import regext_opportunity
import mission_log
import random
import titles_ran
import quote_day


from jinja2 import StrictUndefined

import os
import requests
import pprint 
import inspect


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
    quote = quote_day.quote_of_day()
    return render_template('homepage.html',
                            quote = quote)


@app.route('/rovers')
def see_rovers():
    return render_template('rovers.html')


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
    # int_date = ''.join(int_date[0]).join(int_date[1]).join(int_date[2])

    if rover_id == "1":
        rover_blogpost_text = regex_curiosity.spock_to_space()
    elif rover_id == "2":
        rover_blogpost_text = regex_spirit.troi_to_Mars()
    elif rover_id == "3":
        rover_blogpost_text = regext_opportunity.captain_to_Mars()
    else:
        print('sorry please come back later')

#if conditional statment here to check if the date chosen by the user is alreayd in the database XXXX
    # print (type(rover_blogpost), rover_blogpost)

    rover_blogpost_missionlive = MissionPost_live(rover_id, rover_blogpost_text['title'], rover_blogpost_text['quote'], rover_blogpost_text['mission'])
    #packing info into a class   
    
    name_var = crud.get_rover_name_by_id(rover_id) #this can stay because we pull from database

    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{name_var.lower()}/photos?'
    payload = {
      'api_key' : api_key,
      'earth_date': rover_date
    }

    res = requests.get(url, params = payload)

    api_data = res.json() 

    picture_path = api_data['photos']

    if picture_path == []:
        flash ('6. Sorry there is no image for this date. Please try again.')
    else:
        picture_path = api_data['photos'][0]['img_src']
        date = rover_date
        title = rover_blogpost_text['title']
        text = rover_blogpost_text['quote'] + rover_blogpost_text['mission']
        db_missionpost = crud.create_missionpost(rover_id, date, title, text)
        max_post_id2 = crud.get_max_missionpost_id()
        db_photo = crud.create_photos(picture_path, max_post_id2)


    return render_template('chosen_date.html',
                           
                        #    rover_posts = rover_blogpost,
                           rover_posts_live = rover_blogpost_missionlive,
                           r_name = name_var,
                           r_id = rover_id,
                           rover_datetext = rover_date,
                           pics = picture_path,
                           data = api_data
                           )    


@app.route('/users', methods = ['POST'])
def register_new_user():
    """Create a new user"""
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = crud.get_user_by_email(email)
    if user:
        return 'This email already exists. Please login.'
    else: 
        new_user = crud.create_user(email, password)
        session["user_email"] = new_user.email
        return 'Your account has been created! You are automatically subscribed to our newsletter.'

@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details of a  user."""

    user = crud.get_user_by_id(user_id)
    return render_template("user_details.html", user=user)

@app.route('/login', methods = ['POST'])
def login():
    """User login."""
    
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        if user.password == password and user.email == email:
        
            session["user_email"] = user.email
            return f"Welcome back, {user.email}!"
        else:
            return "The email or password you entered was incorrect."
    else:
        return "Sorry there appears to be an error with your login. Please try again later."

        # Log in user by storing the user's email in session
    #have a homepage.js that handles the routes for the sign up - can responsd with JSON or string to be
    #rendered. 


@app.route('/logout')
def logout_user():
    session.email = None
    flash("Sorry to see you go.")
    return redirect("/")

@app.route ('/about_you')
def find_out_more():

    return render_template('about_you.html')

@app.route ('/about-user', methods = ["POST"])
def get_to_know_user():
    user_nickname = request.form.get('nickname')
    user_age = request.form.get('age')
    user_hobbies = request.form.get('hobbies')
    user_movie = request.form.get('movie')

    return 'Thank you ' +user_nickname+ ' for telling us more about yourself. We will keep your information confidential'

     
@app.route('/search', methods = ["GET","POST"])
def search():


    if request.method == "GET":

        search_title = request.args.get('search_title')

        if search_title == None:
            flash ("Please enter a title")

        else:


            missionposts = MissionPost.query.filter(MissionPost.title.ilike('%' + search_title + '%')).all()

            if not missionposts:
            
                flash("No results")
            
            print("missionposts")
            print("2.1",missionposts)
            print("2.2",type(missionposts))
            print("2.3",missionposts.__getitem__(0).missionpost_id)
        

            return render_template('search.html', missionposts = missionposts)

    else:
        search_title = request.form.get('search_title')
        missionposts = MissionPost.query.filter(MissionPost.title.like('%' + search_title + '%')).all()

        if not missionposts:
        
            flash("No results")
        
        # print("missionposts")
        # print("3.1",missionposts)
        # print("3.2",type(missionposts))
        # print("3.4",missionposts.__getitem__(0).missionpost_id)
        #return missionposts=mission_data
        return render_template('search.html', missionposts = missionposts)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
    app.debug = True
    connect_to_db(app)
    app.run(host='0.0.0.0')
 