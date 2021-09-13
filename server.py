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


    print ("1. THIS IS A TEST*************") 
    print ("1.2", rover_date)
    print ("1.3", name_var)
    print ("1.4", request.method)
    print ('2. ******************checking the photos&&&&&&&&&&&&&&&&&&&')


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

    print ('3. ££££££££££££££££')
    # print (int_date)

   
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
        print('4. sorry please come back later')
     
    
    # date_database_check = crud.get_posts_by_date(rover_date) 
    # if date_database_check == []:
    #     date_database_check = MissionPost_live(rover_id, rover_blogpost_text['title'], rover_blogpost_text['quote'], rover_blogpost_text['mission'])
    # # else: 
        # rover_blogpost_missionlive == get_posts_by_date(rover_date)
        
#if conditional statment here to check if the date chosen by the user is alreayd in the database XXXX
    # print (type(rover_blogpost), rover_blogpost)

    rover_blogpost_missionlive = MissionPost_live(rover_id, rover_blogpost_text['title'], rover_blogpost_text['quote'], rover_blogpost_text['mission'])
    #packing info into a class   
    
    print ('5. SECOND TESTS!!!!!!@@@@@@@@@@@@@@@')
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
        flash('This email already exists. Please login.')
    else: 
        crud.create_user(email, password)
        flash('Your account has been created!')

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
    session.mail = None
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

    # print('1', user_nickname)
    # print ('R$$$$$$$$$$$%%%%%%%%%%%%%')

    return 'Thank you ' +user_nickname+ ' for telling us more about yourself. We will keep your information confidential'

     
@app.route('/search', methods = ["GET","POST"])
def search():


    if request.method == "GET":

        search_title = request.args.get('search_title')

        missionposts = MissionPost.query.filter(MissionPost.title.like('%' + search_title + '%')).all()

        if not missionposts:
        
            flash("No results")

        return render_template('search.html', missionposts = missionposts)

    else:
        search_title = request.form.get('search_title')

        missionposts = MissionPost.query.filter(MissionPost.title.like('%' + search_title + '%')).all()

        mission_data = []
        for posts in missionposts:
            mission_data.append({"title": posts.title, "text":posts.text, "date":posts.date})

        return jsonify(mission_data)

# @app.route('/search_ajax', methods = ["POST"])
# def search2nd():

#     search_title2_ajax = request.form.get('search_title')

#     testindex=0
#     missionposts_id_linked_title_ajax = MissionPost.query.filter(MissionPost.title.like('%' + search_title2_ajax+ '%')).all()
#     if  missionposts_id_linked_title_ajax == []:
#         flash


#         missionpost_index_searched_ajax=missionposts_id_linked_title_ajax.__getitem__(testindex).missionpost_id
#     # finding_title2_ajax=MissionPost.query.filter(missionpost_index_searched_ajax).all()
#         finding_title2_ajax=MissionPost.query.filter(MissionPost.missionpost_id==missionpost_index_searched_ajax).all()
#         print("ajax info",finding_title2_ajax)
#         print(type (finding_title2_ajax))
  
#     return jsonify( )
    


if __name__ == '__main__':
    app.debug = True
    connect_to_db(app)
    app.run(host='0.0.0.0')
 