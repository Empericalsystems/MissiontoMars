"""Models for Mars Mission app."""

from flask_sqlalchemy import SQLAlchemy
 

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri="postgresql:///missiontest", echo=True):
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
    password = db.Column(db.String(25), nullable = False)

  

    def __repr__(self):
        return f'<User user_id = {self.user_id} email = {self.email} password = {self.password}>'

class User_Mission(db.Model):
    """Linking the many users to many missionposts"""

    __tablename__ = 'user_mission'

    user_mission_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    user_id = db.Column(db.Integer, 
                               db.ForeignKey('users.user_id'))
    missionpost_id = db.Column(db.Integer, 
                               db.ForeignKey('missionposts.missionpost_id'))


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
    
    missionpost = db.relationship('MissionPost', backref = 'photos')

    def __repr__(self):
        return f'<photo_name={self.photo_name}>'


class MissionPost(db.Model):

    """EachRover's Missionlog """

    __tablename__ = "missionposts"

    missionpost_id = db.Column(db.Integer, 
                               autoincrement=True, 
                               primary_key=True)
    
    title = db.Column(db.String(60), unique = True)
    text = db.Column(db.Text)
    date = db.Column (db.DateTime)
    rover_id = db.Column(db.Integer,
                         db.ForeignKey ('rovers.rover_id'),
                         nullable=False)

    users = db.relationship('User', secondary = 'user_mission',
                                    backref = 'missionposts')
 
    rover = db.relationship('Rover', backref = 'missionposts') #rover&missionpost = one-to-many


    def __repr__(self):
        return f"<missionpost_id={self.missionpost_id}>"


if __name__ == "__main__":
    from server import app


    connect_to_db(app) #should i connect to missiontest db?
    


    #dbmissiontest - name of db
    #git put to 'first' not 'origin' - 'git push -u first main'

    #making tables:
# ethan = User(email = 'ethan@mars.base', password = 'kerbals')
# >>> db.session.add(ethan)
# >>> db.session.commit()

# jeb = User (email = 'jeb@kerbals.space' , password = 'planet_elu')
# >>> db.session.add(jeb)
# >>> db.session.commit()

# bob = User(email = 'bob@kerbals.space', password = 'I_love_Rockets')
# >>> db.session.add(bob)
# >>> db.session.commit()

# spirit = Rover(rovername = 'Spirit')
# >>> db.session.add(spirit)
# >>> db.session.commit()

#  p = Rover.query.first()
#   p.missionposts

#  opportunity = Rover (rovername = 'Opportunity')
# >>> db.session.add(opportunity)
# >>> db.session.commit()

#jeb.missionposts.append(day1)

# mars1 = Photo(photo_name = 'edr_rcam', photo_path = 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01004/opgs/edr/rcam/RLB_486615482EDR_F0481570RHAZ00323M_.JPG')
# >>> db.session.add(mars1)
# >>> db.session.commit()
#day1.photos


# day1 = MissionPost (title = 'The endless night', text = 'The planet Mars is a hostile place...', date='2021-08-19', rover_id = 2)
# >>> db.session.add(day1)>>> db.session.commit()
# mars1.missionpost

#  day590 = MissionPost(title='The dust storm', text='It wiped out our connection to earth...', date='2045-09-29', rover_id=3)
# >>> db.session.add(day590)>>> db.session.commit()

# photo1 = Photo (photo_name = 'A good start', photo_path = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key= HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE', missionpost_id = 1)
# >>> db.session.add(photo1)
# >>> db.session.commit()
# users.password

    #for crud from modelpy import User, Rover, MissionPost, Photo, association
#db.session.rollback()
#R= Rover.query.all()[0]
#R.missionposts  [<missionpost_id=2>, <missionpost_id=3>]


#m= MissionPost.query.first()
#  m.users