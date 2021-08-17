
from flask import Flask, render_template, request


import os
import requests

res = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE')

photos = res.json()


# app = Flask(__name__)
# app.secret_key = 'nosecret'



# @app.route('/')
# def homepage():
#     """LandingPage - mission details."""

#     return render_template('homepage.html')


# @app.route('/curiosity')
# def log_Curiosity():
#     """Curiosity's Mission log"""

#     return render_template('curiosity.html')


# @app.route('/spirit')
# def log_Spirit():
#     """Spirit's phMission log"""

    

#     return render_template('spirit.html')


# @app.route('/opportunity')
# def log_opportunity():
#     """Opportunity's Mission log"""

#     return render_template('opportunity')


# if __name__ == '__main__':
#     app.debug = True
#     app.run(host='0.0.0.0')
