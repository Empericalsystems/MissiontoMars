from model import db, User, Rover, MissionPost, Photo connect_to_db


def create_user(email, password):
    """Creating a new user"""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user



def get_users():
    """Get a list all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Find a user by user_id."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Find a user by email address."""

    return User.query.filter(User.email == email).first()


def create_rovers()

def create_missionpost(rovername, title, text, photo_id):
    """Create and return a new movie."""

    missionlog = MissionPost(
        rovername = rovername,
        photo_id = photo_id,
        title = title,
        text = text,
    )

    db.session.add(missionlog)
    db.session.commit()

    return missionlog

if __name__ == '__main__':
    from server import app
    connect_to_db(app)