"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app) 

    print("Connected todb")

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(25))

    def __repr__(self):
        return

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
    """UserComments/Likes"""

    __tablename__ = "rovers"

    rover_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rovername = db.Column(db.String(50), unique=True)
    missionposts_id = db.Column(db.Integer, db.ForeignKey("missionposts.missionpost_id"))
   

    def __repr__(self):
        return f"<rovername_id={self.rovername_id}>"


class MissionPost(db.Model):
    """UserComments/Likes"""

    __tablename__ = "missionposts"

    missionpost_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rovername = db.Column(db.String(50), unique=True)
    rover_id = db.Column(db.Integer, db.ForeignKey("missionposts.missionpost_id"))
    photo_id = db.Column(db.Integer, db.ForeignKey("photos.photo_id"))
    title = db.Column(db.String(50))
    text = db.Column(db.Text)
   

    def __repr__(self):
        return f"<missionpost_id={self.missionpost_id}>"



if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
    db.create_all()