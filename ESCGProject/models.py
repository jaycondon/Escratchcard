from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from ESCGProject.database import metadata, db_session

class User(object):
    query = db_session.query_property()

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

class User_Card(object):
    query = db_session.query_property()

    def __init__(self, User_ID, Card_ID):
        self.User_ID = User_ID
        self.Card_ID = Card_ID

    def __repr__(self):
        return '<Card %r>' % (self.User_ID)

class Card(object):
    query = db_session.query_property()

    def __init__(self, number, detail=None):
        self.number = number
        self.detail = detail

    def __repr__(self):
        return '<Card %r>' % (self.number)

class Card_Detail(object):
    query = db_session.query_property()

    def __init__(self, detail=None):
        self.detail = detail

    def __repr__(self):
        return '<Card %r>' % (self.detail)

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), unique=True),
    Column('email', String(120), unique=True),
	Column('password', String(120), unique=False)
)

users_cards = Table('users_cards', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, unique=True),
    Column('card_id', Integer, unique=True),
)

cards = Table('cards', metadata,
    Column('id', Integer, primary_key=True),
    Column('number', Integer, unique=True),
    Column('detail', Integer, unique=True),
)

card_details = Table('card_details', metadata,
    Column('id', Integer, primary_key=True),
    Column('value', Integer, unique=True),
)

mapper(User, users)
mapper(User_Card, users_cards)
mapper(Card, cards)
mapper(Card_Detail, card_details)
