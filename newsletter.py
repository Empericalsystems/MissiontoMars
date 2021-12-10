import smtplib
import os
from email.message import EmailMessage
from datetime import *
import time
from dateutil.relativedelta import *
import calendar
import crud
import model
import server
from flask import Flask, render_template, request, flash, session, redirect, jsonify 
from model import db, User, Rover, MissionPost, Photo, connect_to_db


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    
    email_list=crud.get_users() #list of users from crud
    
    list_to_send=[] #need to create a list because the send function requires list for multiple users
    for email_item in email_list: #iterating through the class object iterating through and add to a list
      list_to_send.append(email_item.email)
      print("adding email to send list: ",email_item.email)

 
# https://dateutil.readthedocs.io/en/stable/index.html

    today = date.today() 
    # print(today)

    # set_date = today + relativedelta(weekday=MO/SU/FRI)
    # set_date =today+relativedelta(day=13)

    set_date = today + relativedelta(minutes=+1)
    # print (set_date)

    
    if set_date == set_date:

      my_email = os.environ.get('EMAIL_ADDR')
      email_password = os.environ.get('EMAIL_PASS')
      # recipient = os.environ.get('RECEIVE')

      recipient = list_to_send

      email_message = EmailMessage()
      email_message['Subject'] = 'The Ensigns of Command'

      email_message['From'] = my_email
      email_message['To'] = recipient
      email_message.set_content('plain text')

      email_message.add_alternative("""\
          <!doctype html>
      <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>

        <h1> Mars Day 342: </h1>

        <h2>"Operation Fearless" </h2>
        <img src="https://mars.nasa.gov/mer/gallery/all/2/f/562/2F176268749EFFAD92P1214R0M1-BR.JPG" />


      <p> "Mission's Log, stardate 2947.3. We have been through a severe ion storm. \
      One crewman is dead. The ship's damage is considerable. \
          I have ordered a nonscheduled layover on Starbase 11 for repairs. \
          A full report of damages was made to the commanding officer of Starbase 11, Commodore Stone.”
          
        </p>


          """, subtype = 'html')


      with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
          connection.ehlo()
          connection.starttls() #makes the connection secure and encyrpts email
          connection.login(my_email, email_password) #log into to email provider
       
          connection.send_message(email_message)

          print ("Email was sent")


 
