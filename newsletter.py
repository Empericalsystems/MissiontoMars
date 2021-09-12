import smtplib
import os
from email.message import EmailMessage
from datetime import *
import time
from dateutil.relativedelta import *
import calendar


# https://dateutil.readthedocs.io/en/stable/index.html

today = date.today() 
print(today)

# set_date = today + relativedelta(weekday=MO/SU/FRI)
# set_date =today+relativedelta(day=13)

set_date = today + relativedelta(minutes=+1)
print (set_date)

 
if set_date == set_date:

  my_email = os.environ.get('EMAIL_ADDR')
  email_password = os.environ.get('EMAIL_PASS')
  recipient = os.environ.get('RECEIVE')

  email_message = EmailMessage()
  email_message['Subject'] = 'The Rover Broke'

  email_message['From'] = my_email
  email_message['To'] = recipient
  # email_message.set_content('Our rovers are heading towards sol 1098....and this week')
  email_message.set_content('plain text')

  email_message.add_alternative("""\
      <!doctype html>
  <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>

    <h1> Mars Day 342: </h1>

    <h2>"The Day the Rover Broke" </h2>
    <img src="https://mars.nasa.gov/mer/gallery/all/2/f/562/2F176268749EFFAD92P1214R0M1-BR.JPG" />


  <p> "Mission's Log, stardate 2947.3. We have been through a severe ion storm. \
  One crewman is dead. The ship's damage is considerable. \
      I have ordered a nonscheduled layover on Starbase 11 for repairs. \
      A full report of damages was made to the commanding officer of Starbase 11, Commodore Stone.”
      
    </p>


      """, subtype = 'html')

  # email_subject = 'Our Mission Log for the Week'
  # content = 'Our rovers are heading towards sol 1098....and this week'
  # email_message = f'Subject: {email_subject}\n\n{content}'

  with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
      connection.ehlo()
      connection.starttls() #makes the connection secure and encyrpts email
      connection.login(my_email, email_password) #log into to email provider
      # connection.sendmail(my_email, 
      #                     recipient, 
      #                     email_message)
      
      connection.send_message(email_message)

      print ("Email was sent")


 
# connection = smtplib.SMTP("smtp.mail.yahoo.com")  

#     # email_subject = 'Our Mission Log for the Week'
#     # content = 'Our rovers are heading towards sol 1098....and this week'
#     # email_message = f'Subject: {email_subject}\n\n{content}'
#     # smtp.sendmail(my_email, recipient, content)

# connection.starttls()   
# connection.login(my_email, email_password) 
# connection.sendmail(my_email, recipient, "Subject:This is just a 2ndrovermission test" )
# connection.close()