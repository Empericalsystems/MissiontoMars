from flask import Flask, render_template, request, flash, session, redirect, jsonify 
# from model import connect_to_db
from model import db, User, Rover, MissionPost, Photo, connect_to_db
import regex_spirit
import regex_curiosity
import regext_opportunity
import mission_log
import titles_ran


from jinja2 import StrictUndefined

import os
import requests
import pprint 
import inspect
import crud
import random 
from sqlalchemy import update
from sqlalchemy import func
from werkzeug.security import generate_password_hash, check_password_hash





if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    email_list=crud.get_users()
    #email_list=crud.get_user_by_id(0)
    print(type(email_list))
    print(email_list)
    for email_item in email_list:
        print(email_item,email_item.user_id,email_item.email,type(email_item))

    list_to_send=[]
    print(type(list_to_send))
    for email_item in email_list:
        list_to_send.append(email_item.email)
        print("adding email to send list: ",email_item.email)
    
    print("Final List to Send is : ",list_to_send)
    for email2 in list_to_send:
        print(email2)
