
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

import os
import requests



app = Flask(__name__)
app.secret_key = 'nosecret'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """LandingPage - mission details."""
    return render_template('homepage.html')

    
    


@app.route('/curiosity')
def log_Curiosity():
    """Curiosity's Mission log"""
  

    return render_template('curiosity.html')

@app.route('/spirit')
def log_Spirit():
    """Spirit's Mission log"""

    

    return render_template('spirit.html')


@app.route('/opportunity')
def log_opportunity():
    """Opportunity's Mission log"""

    return render_template('opportunity')

# @app.route('/afterparty/search')
# def find_afterparties():
#     """Search for afterparties on Eventbrite"""

#     keyword = request.args.get('keyword', '')
#     postalcode = request.args.get('zipcode', '')
#     radius = request.args.get('radius', '')
#     unit = request.args.get('unit', '')
#     sort = request.args.get('sort', '')

#     url = 'https://app.ticketmaster.com/discovery/v2/events'
#     payload = {'apikey': API_KEY,
#                'keyword': keyword,
#                'postalCode': postalcode,
#                'radius': radius,
#                'unit': unit,
#                'sort': sort}

#     response = requests.get(url, params=payload)

#     data = response.json()
#     events = data['_embedded']['events']

#     return render_template('search-results.html',
#                            pformat=pformat,
#                            data=data,
#                            results=events)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
