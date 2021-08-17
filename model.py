"""Models for Mars Mission app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app) 

    print('Testing it works')

class User(db.Model):
    """the user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    # username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(25))

    def __repr__(self):
        return f'<User user_id = {self.user_id} email = {self.email} password = {self.password}'

# class Comments_Likes(db.Model):
#     """UserComments/Likes"""

#     __tablename__ = "comments"

#     usercomments_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
#     missionposts_id = db.Column(db.Integer, db.ForeignKey("missionposts.missionpost_id"))
#     comments = db.Column(db.Text)
    


#     def __repr__(self):
#         return f"<usercomments_id={self.usercomments_id}>"
#  CONSIDER LEAVING FOR NICE TO HAVE!!
   

class Rover(db.Model):
    """EachRover's Identity outlined"""

    __tablename__ = 'rovers'

    rover_id = db.Column(db.Integer, 
                         autoincrement=True, 
                         primary_key=True)
    rover_name = db.Column(db.String(50), unique=True)
    # missionpost_id = db.Column(db.Integer, db.ForeignKey('missionposts.missionpost_id')) #looks at table in db

    # missionpost = db.relationship('MissionPost', backref = 'rovers') #*************!!CHECKING11X*****
    #  #looks at class and refers to rovers table
   #goes back to MissionPost; one-to-many - one rover has  many posts)

    def __repr__(self):
        return f"<rover_name_id={self.rover_name_id}>"



class MissionPost(db.Model):
    """EachRover'sMissionLog"""

    __tablename__ = "missionposts"

    missionpost_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # rover_name = db.Column(db.String(50), unique=True)
    rover_id = db.Column(db.Integer, db.ForeignKey('rovers.rover_id')) #unclear if this will stay because of the association table?
    #kept it here because rover-MissionPost = one-to-many - ForeignKey stays?errors keeps showing - but when include
    #error persists
    title = db.Column(db.String(60))
    text = db.Column(db.Text)

    rover = db.relationship('Rover', backref = 'missionposts') #rover&missionpost = one-to-many
    photo = db.relationship('Photo', secondary = 'photo_missions', #many-to-many
                             backref = 'missionposts') #backref to missionposts
   

    def __repr__(self):
        return f"<missionpost_id={self.missionpost_id}>"


class Photo(db.Model):
    """Photos from RoverCameras"""

    __tablename__ = "photos"

    photo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    photo_name = db.Column(db.String(50), unique=True)
    photo_path = db.Column(db.String) #URL

    rover = db.relationship('Rover', backref = 'photos') #one rover has many photos. one to many
    # missionpost = db.relationship('MissionPost', 
    #                                secondary = 'photo_missions', 
    #                                backref = 'photos') #DON"T NEED THIS? IT"S LINKED/DEFINED IN PHOTOS?
    #in lecture demo on modelling the second class didn't show the many to many - only the first

class Photo_Mission(db.Model):
    """Association table for many-to-many"""
    __tablename__ = 'photo_missions'
 
    photo_mission_id = db.Column(db.Integer, primary_key = True)
    missionpost_id = db.Column(db.Integer,
                               db.ForeignKey('missionposts.missionpost_id'),
                               nullable = False)
    photo_id = db.Column(db.Integer,
                         db.ForeignKey('photos.photo_id'),
                         nullable = False)  

    def __repr__(self):
        return f"<photoname_id={self.photoname_id}>"

if __name__ == "__main__":
    from server import app


    connect_to_db(app) #should i connect to missiontest db?
    db.create_all()


    #dbmissiontest - name of db
    #git put to 'first' not 'origin' - 'git push -u first main'

    #making tables:
    #rover_first = Rover(rover_name = 'Spirit')

    #for crud from model.py import User, Rover, MissionPost, Photo, association