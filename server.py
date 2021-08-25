
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


@app.route('/')
def homepage():
    """LandingPage - mission details."""
    return render_template('homepage.html')

    

@app.route('/curiosity', methods = ['GET','POST'])
def log_Curiosity():
    """Curiosity's Mission log"""


    earth_date = request.args.get('earth_date', '')
    img_src = request.args.get('img_src', '')
    

    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?'
    payload = {
      'api_key' : 'HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE',
      'earth_date': '2019-08-12'
    }

    res = requests.get(url, params = payload)

    data = res.json() 
    pic = data['photos'][0]['img_src']

    text = regex_curiosity.twain_to_space()

    return render_template('curiosity.html',
                           data=data,
                           img_src=img_src,
                           text = text)

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


@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        # email = request.get('email') #check where this is going to be accessed?
        # a form on the HTML?
        pass


    return '<p>please register</p>'     

@app.route('/archive')
def log_archive():
    
    return render_template ('archive.html')


@app.route('/login')
def login():
    return '<p>login</p>'

@app.route('/logout')
def logout():
    return '<p>logout</p>'




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
