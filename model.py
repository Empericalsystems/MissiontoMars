"""Models for Mars Mission app."""

from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.sql import func
from datetime import datetime


db = SQLAlchemy()

def connect_to_db(flask_app, db_uri="postgresql:///marstest", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  

    db.app = flask_app
    db.init_app(flask_app) 
    # db.create_all()

    print('Testing it works')



class User(db.Model):
    """the user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    email = db.Column(db.String, unique=True, nullable = False)  
    # password = db.Column(db.String, nullable = False)
    password = db.Column(db.String(500), nullable=False)

  

    def __repr__(self):
        return f'<User user_id = {self.user_id} email = {self.email} password = {self.password}>'

class User_Mission_Links(db.Model):
    """Linking the many users to many missionposts"""

    __tablename__ = 'user_mission'

    user_mission_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    user_id = db.Column(db.Integer, 
                               db.ForeignKey('users.user_id'))
    missionpost_id = db.Column(db.Integer, 
                               db.ForeignKey('missionposts.missionpost_id'))
    missionpost_comment = db.Column(db.Text, nullable=True)


    # Relationships
    missionpost = db.relationship("MissionPost", backref=db.backref("user_mission"))
    user = db.relationship("User", backref=db.backref("user_mission"))

    def __repr__(self):

        return f"<missionpost_id={self.user_comment_id}, user_id = {self.user_id}, user_mission_id ={self.user_mission_id}>"



class Rover(db.Model):
    """EachRover's Identity outlined"""

    __tablename__ = 'rovers'

    rover_id = db.Column(db.Integer, 
                         autoincrement=True, 
                         primary_key=True)
    rovername = db.Column(db.String(50), unique=True)
    
   
    def __repr__(self):
        return f'<rovername={self.rovername}>'



class Photo(db.Model):
    """Photos from RoverCameras"""

    __tablename__ = "photos"

    photo_id = db.Column(db.Integer, 
                         autoincrement=True, 
                         primary_key=True)
    photo_name = db.Column(db.String(50), unique=True)
    photo_path = db.Column(db.String) #URL
    missionpost_id = db.Column(db.Integer, 
                               db.ForeignKey('missionposts.missionpost_id'))
    
    # Relationships
    missionpost = db.relationship('MissionPost', backref = 'photos')

    def __repr__(self):
        return f'<photo_name={self.photo_name}>'


class MissionPost(db.Model):

    """EachRover's Missionlog """

    __tablename__ = "missionposts"

    missionpost_id = db.Column(db.Integer, 
                               autoincrement=True, 
                               primary_key=True)
    
    title = db.Column(db.String(60), unique = False)
    text = db.Column(db.Text)
    # date = db.Column (db.DateTime(timezone=True), default=func.now())
    # date = db.Column (db.DateTime, default=datetime.utcnow)
    date = db.Column (db.Date)

    rover_id = db.Column(db.Integer,
                         db.ForeignKey ('rovers.rover_id'),
                         nullable=False)
    # Relationships
    users = db.relationship('User', secondary = 'user_mission',
                                    backref = 'missionposts')
 
    rover = db.relationship('Rover', backref = 'missionposts') #rover&missionpost = one-to-many


    def __repr__(self):
        return f"<missionpost_id={self.missionpost_id}>"


if __name__ == "__main__":
    from server import app

    connect_to_db(app)  
    
 