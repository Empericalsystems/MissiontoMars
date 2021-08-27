from model import db, User, Rover, MissionPost, Photo, connect_to_db
import random 


def create_user(email, password):
    """Creating a new user"""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

    # create_user('e@t', 'dust') - working

def get_users():
    """Get a list all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Find a user by user_id."""

    return User.query.get(user_id)
#get_users() - working

def get_user_by_email(email):
    """Find a user by email address."""

    return User.query.filter(User.email == email).first()
    
# get_user_by_email('e@t') working



def delete_user(user_id):
    user_delete = User.query.get(user_id)

    db.session.delete(user_delete)
    db.session.commit()

    return user_delete

#Works delete_user(4)

def create_rover(rovername):
    """Create and return a new rover."""
    add_rovers = Rover(rovername = rovername)
    db.session.add(add_rovers)
    db.session.commit()

    return add_rovers

def get_rovers():
    """Get a list all rovers."""

    return Rover.query.all()
#working

def get_rover_by_id(rover_id):
    """Find a rover by rover_id."""

    return Rover.query.get(rover_id)

#working

def get_rover_by_name(rovername):
    """Find a rover by its name"""

    return Rover.query.filter(Rover.rovername == rovername).all()
#working

def delete_rover(rover_id):
    rover_delete = Rover.query.get(rover_id)

    db.session.delete(rover_delete)
    db.session.commit()

    return rover_delete
#working     

def create_photos(photo_path, missionpost_id):
    """ Create and return new pics"""

    add_photos = Photo (
        # photo_name = photo_name,
        photo_path = photo_path,
        missionpost_id = missionpost_id
    )
    db.session.add(add_photos)
    db.session.commit()

    return add_photos


def get_photos():
    """Get a list all photos."""

    return Photo.query.all()


def get_photo_by_id(photo_id):
    """Find a photo by photo_id."""

    return Photo.query.get(photo_id)


def delete_photo(photo_id):
    photo_delete = Photo.query.get(photo_id)

    db.session.delete(photo_delete)
    db.session.commit()

    # return photo_delete


def get_photo_by_missionpost(missionpost_id):
    """Find a user by missionpost_id"""

    return Photo.query.get(missionpost_id)
 

def delete_photo(photo_id):
    photo_delete = Photo.query.all()

    db.session.delete(photo_delete)
    db.session.commit()

    # return photo_delete
 

def create_missionpost(rover_id, title, text, date):
    """Create and return a new missionpost."""

    missionlog = MissionPost(
        rover_id = rover_id,
        title = title,
        text = text,
        date = date
    )

    db.session.add(missionlog)
    db.session.commit()

    return missionlog
# working!

def get_random_missionpost_id():
    """create random"""
    return random.choice(MissionPost.query.filter(MissionPost.rover_id == random.randint(1, 3)).all()).missionpost_id
#getint ghte mission post id

def get_post_by_id(missionpost_id):
    """Find a post by missionpost_id."""

    return MissionPost.query.get(missionpost_id)
#working

def get_missionposts():
    """Get a list all missionposts."""

    return MissionPost.query.all()
 

def get_posts_by_title(title):
    """Find a photo by title."""

    return MissionPost.query.filter(MissionPost.title == title).all()


def get_posts_by_date(date):
    """Find a photo by date."""

    return MissionPost.query.filter(MissionPost.date == date).all()

def get_posts_by_rover(rover_id):
    """Find a missionpost by rover_id"""

    return MissionPost.query.filter(MissionPost.rover_id == rover_id).options(db.joinedload(MissionPost.photos)).all() #when have all missionpost objects can do .photos - 
    #will preload the photos attribute
#Not working? MIssionPost not defined??

def delete_missionpost(missionpost_id):
    posts_delete = MissionPost.query.all()

    db.session.delete(posts_delete)
    db.session.commit()

    # return posts_delete
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)