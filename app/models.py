from app import db, login_manager
from flask_login import UserMixin

# SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#     username="kampuswerk",
#     password="thecatsatonthemat",
#     hostname="127.0.0.1",
#     databasename="kampuslocal",
# )
# app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

# db = SQLAlchemy(app)

# app.config['OAUTH_CREDENTIALS'] = {
#     'facebook': {
#         'id': '837483683053553',
#         'secret': 'bce2321650fbb754b955453e1d10b2f0'
#     },
#     'google': {
#         'id': '838769494183-f2e9i6s0ng8eps3075bfsmlgoo3e7hvk.apps.googleusercontent.com',
#         'secret': '51V_GgfoNr52oB0X9vhVXd3E'
#     },
#     'twitter': {
#         'id': 'dDu5qMg32Rsh94P89UCcQoLJO',
#         'secret': 'EB6LF33hBYjhKsiPqxofG1NN8PFSQ1i007zjdIvDekgCnkbkp7'
#     }
# }


#Oauth decorators for social media login
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    hangboardwerkouts = db.relationship('HangboardWerkout', backref='author', lazy='dynamic')
    kampuswerkouts = db.relationship('KampusWerkout', backref='author', lazy='dynamic')

class Bodyweight(db.Model):

    __tablename__ = "bodyweight"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096))
    bodyweight_kg = db.Column(db.Float)
    notes = db.Column(db.String(4096))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, bodyweight_kg, notes, timestamp, user_id):
        self.name = name
        self.bodyweight_kg = bodyweight_kg
        self.notes = notes
        self.timestamp = timestamp
        self.user_id = user_id

class HangboardWerkout(db.Model):

    __tablename__ = "hangboardwerkout"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096))
    board = db.column(db.String(96))
    holds_used = db.Column(db.Integer)
    arm_used = db.Column(db.String(96))
    hangtime = db.Column(db.Integer)
    resttime = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    setrest = db.Column(db.Integer)
    weight_kg = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, board, holds_used, reps, sets, setrest, arm_used, hangtime, resttime, weight_kg, timestamp, user_id):
        self.name = name
        self.board = board
        self.holds_used = holds_used
        self.arm_used = arm_used
        self.hangtime = hangtime
        self.resttime = resttime
        self.reps = reps
        self.sets = sets
        self.setrest = setrest
        self.weight_kg = weight_kg
        self.timestamp = timestamp
        self.user_id = user_id

class KampusWerkout(db.Model):
    __tablename__ = "kampuswerkout"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(4096))
    hand = db.Column(db.String(4096))
    rung1 = db.Column(db.Integer)
    rung2 = db.Column(db.Integer)
    rung3 = db.Column(db.Integer)
    rung4 = db.Column(db.Integer)
    rung5 = db.Column(db.Integer)
    rung6 = db.Column(db.Integer)
    rung7 = db.Column(db.Integer)
    rung8 = db.Column(db.Integer)
    rung9 = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    def __init__(self, name, hand, rung1, rung2, rung3, rung4, rung5, rung6, rung7, rung8, rung9, timestamp, user_id):
        self.name = name
        self.hand = hand
        self.rung1 = rung1
        self.rung2 = rung2
        self.rung3 = rung3
        self.rung4 = rung4
        self.rung5 = rung5
        self.rung6 = rung6
        self.rung7 = rung7
        self.rung8 = rung8
        self.rung9 = rung9
        self.timestamp = timestamp
        self.user_id = user_id


class CircuitMoves(db.Model):

    __tablename__ = "circuitmoves"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(4096))
    numberofmoves = db.Column(db.Integer)
    intensity = db.Column(db.Integer)
    werktime = db.Column(db.Integer)
    grade = db.Column(db.String(4096))
    comments = db.Column(db.String(4096))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, numberofmoves, intensity, werktime, grade, comments, timestamp, user_id):
        self.name = name
        self.numberofmoves = numberofmoves
        self.intensity = intensity
        self.werktime = werktime
        self.grade = grade
        self.comments = comments
        self.timestamp = timestamp
        self.user_id = user_id


class Routes(db.Model):

    __tablename__ = "routes"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(4096))
    height = db.Column(db.Integer)
    intensity = db.Column(db.Integer)
    werktime = db.Column(db.Integer)
    grade = db.Column(db.String(96))
    venue = db.Column(db.String(96))
    angle = db.Column(db.String(96))
    style = db.Column(db.String(96))
    comments = db.Column(db.String(4096))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, height, intensity, werktime, grade, venue, angle, style, comments, timestamp, user_id):
        self.name = name
        self.height = height
        self.intensity = intensity
        self.werktime = werktime
        self.grade = grade
        self.venue = venue
        self.angle = angle
        self.style = style
        self.comments = comments
        self.timestamp = timestamp
        self.user_id = user_id

class Blocs(db.Model):

    __tablename__ = "blocs"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(4096))
    intensity = db.Column(db.Integer)
    werktime = db.Column(db.Integer)
    grade = db.Column(db.String(96))
    venue = db.Column(db.String(96))
    angle = db.Column(db.String(96))
    style = db.Column(db.String(96))
    comments = db.Column(db.String(4096))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, intensity, werktime, grade, venue, angle, style, comments, timestamp, user_id):
        self.name = name
        self.intensity = intensity
        self.werktime = werktime
        self.grade = grade
        self.venue = venue
        self.angle = angle
        self.style = style
        self.comments = comments
        self.timestamp = timestamp
        self.user_id = user_id