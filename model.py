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

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
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

association = db.Table('association',
    db.column('rover_id', db.Integer, db.ForeignKey('rovers.rover_id')),
    db.column('missionposts', db.Integer, db.ForeignKey('missionposts.missionpost_id')),
    db.column('photos', db.Integer, db.ForeignKey('photos.photo_id'))
   )


class Rover(db.Model):
    """EachRover's Identity outlined"""

    __tablename__ = 'rovers'

    rover_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rovername = db.Column(db.String(50), unique=True)
    missionpost_id = db.Column(db.Integer, db.ForeignKey('missionposts.missionpost_id')) #looks at table in db

    missionpost = db.relationship('MissionPost', backref = 'rovers') #looks at class and refers to rovers table
   #goes back to MissionPost and Photo)

   #to create in db; rover = Rover(rovername='Spirit', missionposts (backref from MissionPost) = (missionpost name?/detail?))
#rover = Rover (rovername ='Spirit', missionposts=title)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'title' is not defined

    def __repr__(self):
        return f"<rovername_id={self.rovername_id}>"



class MissionPost(db.Model):
    """EachRover'sMissionLog"""

    __tablename__ = "missionposts"

    missionpost_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rovername = db.Column(db.String(50), unique=True)
    rover_id = db.Column(db.Integer, db.ForeignKey('rovers.rover_id'))
    photo_id = db.Column(db.Integer, db.ForeignKey('photos.photo_id'))
    title = db.Column(db.String(50))
    text = db.Column(db.Text)

    rover = db.relationship('Rover', backref = 'missionposts')
    photo = db.relationship('Photo', backref = 'missionposts')
   

    def __repr__(self):
        return f"<missionpost_id={self.missionpost_id}>"


class Photo(db.Model):
    """Photos from RoverCameras"""

    __tablename__ = "photos"

    photo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    photoname = db.Column(db.String(50), unique=True)
    missionposts_id = db.Column(db.Integer, db.ForeignKey('missionposts.missionpost_id'))
    rover_id = db.Column(db.Integer, db.ForeignKey('rovers.rover_id'))
    photo_path = db.Column(db.String)

    rover = db.relationship('Rover', backref = 'photos')
    missionpost = db.relationship('MissionPost', backref = 'photos')

   

    def __repr__(self):
        return f"<photoname_id={self.photoname_id}>"

if __name__ == "__main__":
    from server import app


    connect_to_db(app) #should i connect to missiontest db?
    db.create_all()

    #for crud from model.py import User, Rover, MissionPost, Photo