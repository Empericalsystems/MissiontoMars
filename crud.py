from model import db, User, Rover, MissionPost, Photo, connect_to_db


def create_user(email, password):
    """Creating a new user"""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

    # create_user('e@t', 'dust')

def get_users():
    """Get a list all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Find a user by user_id."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Find a user by email address."""

    return User.query.filter(User.email == email).first()


def create_rover(rovername):
    """Create and return a new rover."""
    add_rovers = Rover(rovername = rovername)
    db.session.add(add_rovers)
    db.session.commit()

    return add_rovers

def get_rovers():
    """Get a list all rovers."""

    return Rover.query.all()

def get_rover_by_id(rover_id):
    """Find a rover by rover_id."""

    return Rover.query.get(rover_id)

def create_photos(photo_name, photo_path, missionpost_id):
    """ Create and return new pics"""

    add_photos = Photo (
        photo_name = photo_name,
        photo_path = photo_path,
        missionpost_id = missionpost_id
    )
    db.session.add(add_photos)
    db.session.commit()
    return add_photos

def create_missionpost(rovername, title, text, photo_id):
    """Create and return a new missionpost."""

    missionlog = MissionPost(
        rovername = rovername,
        rover_id = rover_id,
        title = title,
        text = text,
    )

    db.session.add(missionlog)
    db.session.commit()

    return missionlog

if __name__ == '__main__':
    from server import app
    connect_to_db(app)