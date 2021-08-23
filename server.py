
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

import os
import requests


app = Flask (__name__)
app.secret_key = 'nosecret'


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

    return render_template('opportunity.html')

 

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
