import smtplib
import os
from email.message import EmailMessage
import win32com.client as win32
 

my_email = os.environ.get('EMAIL_ADDR')
email_password = os.environ.get('EMAIL_PASS')
recipient = os.environ.get('RECEIVE')

email_message = EmailMessage()
email_message['Subject'] = 'The Fate of Mars Water'

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


 <p> Our latest mission has been posted! You can access it here: 
    
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


 
# connection = smtplib.SMTP("smtp.mail.yahoo.com")  

#     # email_subject = 'Our Mission Log for the Week'
#     # content = 'Our rovers are heading towards sol 1098....and this week'
#     # email_message = f'Subject: {email_subject}\n\n{content}'
#     # smtp.sendmail(my_email, recipient, content)

# connection.starttls()   
# connection.login(my_email, email_password) 
# connection.sendmail(my_email, recipient, "Subject:This is just a 2ndrovermission test" )
# connection.close()