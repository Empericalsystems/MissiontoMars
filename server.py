
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


@app.route('/rover/<rover_id>', methods = ['GET','POST'])
def log_rover(rover_id):
    """Each rover's Mission log"""

    rover_date = request.form.get('date')

    print ("THIS IS A TEST*************") 
    print (rover_date)



    rover_posts = crud.get_posts_by_rover(rover_id)
    name_var = crud.get_rover_name_by_id(rover_id)

    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?'
    payload = {
      'api_key' : 'HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE',
      'earth_date': rover_date
    }

    res = requests.get(url, params = payload)

    data = res.json() 
    # first = data['photos'][0]['img_src']
      
    print ('*********************')

    print (data)

    print ('******************')

    # print (first)


    return render_template('rover_posts.html',
                           rover_posts = rover_posts,
                           r_name = name_var,
                           r_id = rover_id,
                           rover_datetext = rover_date
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
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/")





if __name__ == '__main__':
    app.debug = True
    connect_to_db(app)
    app.run(host='0.0.0.0')

