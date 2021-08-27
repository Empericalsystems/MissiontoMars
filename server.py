
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
import regex_spirit
import regex_curiosity


from jinja2 import StrictUndefined

import os
import requests
import pprint 


app = Flask (__name__)
app.secret_key = 'nosecret'
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """LandingPage - mission details."""
    return render_template('homepage.html')

    
@app.route('/missionposts', methods = ['GET','POST'])
def see_all_missionposts():
    """See all mission posts"""

   
    missions = crud.get_random_missionpost_id()
    return render_template('all_missionposts.html', 
                            missions = missions)

def see_all_pics(photo_path, missionpost_id): 
    post_pics = crud.create_photos(photo_path, missionpost_id)

    return render_template('all_missionposts.html', 
                             missions = missions,
                            post_pics = post_pics)

@app.route('/rover/<rover_id>', methods = ['GET','POST'])
def log_rover(rover_id):
    """Curiosity's Mission log"""

    rover_posts = crud.get_posts_by_rover(rover_id)


    return render_template('rover_posts.html',
                           rover_posts = rover_posts)


@app.route('/curiosity', methods = ['GET','POST'])
def log_Curiosity():
    """Curiosity's Mission log"""

    rover_id = 1

    curiosity_post = crud.get_posts_by_rover(rover_id)

    return render_template('curiosity.html',
                           curiosity_post = curiosity_post)

@app.route('/spirit' , methods = ['GET','POST'])
def log_Spirit():
    """Spirit's Mission log"""

    earth_date = request.args.get('earth_date', '')
    img_src = request.args.get('img_src', '')

    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?'
    payload = {
      'api_key' : 'HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE',
      'earth_date': '2005-8-3'
    }

# list of dates - run in a random loop for the day - predfine 10 dates and then random choice

    res = requests.get(url, params = payload)

    data = res.json() 
    pic = data['photos'][0]['img_src']


    text = regex_spirit.twain_to_Mars()


    return render_template('spirit.html',
                           data=data,
                           img_src=img_src,
                           text=text)



@app.route('/opportunity')
def log_opportunity():
    """Opportunity's Mission log"""

    earth_date = request.args.get('earth_date', '')
    img_src = request.args.get('img_src', '')

    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?'
    payload = {
      'api_key' : 'HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE',
      'earth_date': '2015-9-3' #rANDOM DATE GENERATOR  https://www.kite.com/python/answers/how-to-generate-a-random-date-between-two-dates-in-python
    }

    res = requests.get(url, params = payload)

    data = res.json() 
    pic = data['photos'][2]['img_src']

    return render_template('opportunity.html',
                           data=data,
                           img_src=img_src)


   

# @app.route('/archive')
# def log_archive():
    
#     return render_template ('archive.html')

@app.route("/users")
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template("users.html", users=users)


@app.route('/users', methods = ['POST'])
def register_new_user():
    """Create a new user"""
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = crud.get_user_by_email(email)
    if user:
        flash ('This email already exists. Please login')
    else: 
        crud.create_user(email, password)
        flash('Your account has been created! Please login')

    return redirect ('/')

@app.route('/login', methods = ['POST'])
def login():
    """Process user login."""
    
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/")

@app.route('/logout')
def logout():
    return '<p>logout</p>'





if __name__ == '__main__':
    app.debug = True
    connect_to_db(app)
    app.run(host='0.0.0.0')



# @app.route('/curiosity', methods = ['GET','POST'])
# def log_Curiosity():
#     """Curiosity's Mission log"""


#     earth_date = request.args.get('earth_date', '')
#     img_src = request.args.get('img_src', '')
    

#     url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?'
#     payload = {
#       'api_key' : 'HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE',
#       'earth_date': '2019-08-12'
#     }

#     res = requests.get(url, params = payload)

#     data = res.json() 
#     pic = data['photos'][0]['img_src']

#     text = regex_curiosity.twain_to_space()

#     return render_template('curiosity.html',
#                            data=data,
#                            img_src=img_src,
#                            text = text)

# @app.route('/spirit' , methods = ['GET','POST'])
# def log_Spirit():
#     """Spirit's Mission log"""

#     earth_date = request.args.get('earth_date', '')
#     img_src = request.args.get('img_src', '')

#     url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?'
#     payload = {
#       'api_key' : 'HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE',
#       'earth_date': '2005-8-3'
#     }

# # list of dates - run in a random loop for the day - predfine 10 dates and then random choice

#     res = requests.get(url, params = payload)

#     data = res.json() 
#     pic = data['photos'][0]['img_src']


#     text = regex_spirit.twain_to_Mars()


#     return render_template('spirit.html',
#                            data=data,
#                            img_src=img_src,
#                            text=text)



# @app.route('/opportunity')
# def log_opportunity():
#     """Opportunity's Mission log"""

#     earth_date = request.args.get('earth_date', '')
#     img_src = request.args.get('img_src', '')

#     url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?'
#     payload = {
#       'api_key' : 'HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE',
#       'earth_date': '2015-9-3' #rANDOM DATE GENERATOR  https://www.kite.com/python/answers/how-to-generate-a-random-date-between-two-dates-in-python
#     }

#     res = requests.get(url, params = payload)

#     data = res.json() 
#     pic = data['photos'][2]['img_src']

#     return render_template('opportunity.html',
#                            data=data,
#                            img_src=img_src)

