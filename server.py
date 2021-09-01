
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
import regex_spirit
import regex_curiosity
import random


from jinja2 import StrictUndefined

import os
import requests
import pprint 


app = Flask (__name__)
app.secret_key = 'nosecret'
app.jinja_env.undefined = StrictUndefined
api_key = os.environ.get('NASA_API_KEY')


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

    int_date = rover_date.split('-')
    int_date = ''.join(int_date[0]).join(int_date[1]).join(int_date[2])

    print ('££££££££££££££££')
    print (int_date)

    random.seed(int(int_date))  #turn this into a number and give it to seed and randomly pick from listof posts

    rover_posts = [random.choice(crud.get_posts_by_rover(rover_id))] #this returns a list - call 
   
    name_var = crud.get_rover_name_by_id(rover_id)

    print (crud.get_posts_by_rover(rover_id))


    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{name_var.lower()}/photos?'
    payload = {
      'api_key' : api_key,
      'earth_date': rover_date
    }

    res = requests.get(url, params = payload)

    data = res.json() 

    # print (data['photos'][0]['img_src'])

    pics = data['photos']

    if pics == []:
        flash ('Sorry there is no image for this date. Please try again.')
    else:
        pics = data['photos'][0]['img_src']
        


    return render_template('chosen_date.html',
                           rover_posts = rover_posts,
                           r_name = name_var,
                           r_id = rover_id,
                           rover_datetext = rover_date,
                           pics = pics,
                           data = data
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

