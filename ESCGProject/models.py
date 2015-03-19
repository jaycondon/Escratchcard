# from sqlalchemy import Table, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import mapper, relationship, backref
# from ESCGProject.database import metadata, db_session
# from sqlalchemy.ext.declarative import declarative_base



# class User(object):
#     __tablename__ = 'user'
#     query = db_session.query_property()

#     def __init__(self, name=None, email=None, password=None, users_cards_id=None):
#         self.name = name
#         self.email = email
#         self.password = password
#         self.users_cards_id = users_cards_id

#     def __repr__(self):
#         return '<User %r>' % (self.name)

# class User_Card(object):
#     __tablename__ = 'users_cards'
#     query = db_session.query_property()

#     def __init__(self, User_ID=None, Card_ID=None):
#         self.User_ID = User_ID
#         self.Card_ID = Card_ID

#     def __repr__(self):
#         return '<Card %r>' % (self.User_ID)

# class Card(object):
#     __tablename__ = 'cards'
#     query = db_session.query_property()

#     def __init__(self, number, detail=None):
#         self.number = number
#         self.detail = detail

#     def __repr__(self):
#         return '<Card %r>' % (self.number)

# class Card_Detail(object):
#     __tablename__ = 'card_details'
#     query = db_session.query_property()

#     def __init__(self, detail=None):
#         self.detail = detail

#     def __repr__(self):
#         return '<Card %r>' % (self.detail)

# users = Table('users', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String(50), unique=True),
#     Column('email', String(120), unique=True),
# 	Column('password', String(120), unique=False),
# #    children = relationship("Card"),
#     users_cards_id = relationship('Card', backref='users',
#                                 lazy='dynamic')
# )

# users_cards = Table('users_cards', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('user_id', Integer, unique=True),
#     Column('card_id', Integer, unique=True),
# )

# cards = Table('cards', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('number', Integer, unique=False),
#     Column('detail', Integer, unique=True),
#     Column('users_id', Integer, ForeignKey('users.id')),
#     cards_value = relationship('Card_Detail', backref='cards',
#                             lazy='dynamic')
#  #   parent_id = Column(Integer, ForeignKey('users.id')),
# #    child = relationship("Child", uselist=False, backref="parent")
# )

# card_details = Table('card_details', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('value', Integer, unique=True),
#     cards_id = Column(Integer, ForeignKey('cards.id')),
# #    parent_id = Column(Integer, ForeignKey('parent.id'))
# )

# mapper(User, users)
# mapper(User_Card, users_cards)
# mapper(Card, cards)
# mapper(Card_Detail, card_details)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    email = Column(String(120))
    password = Column(String(120))
    balance = Column(Integer)

    users_cards = relationship("Card")
#insert into user (id,name,email,password,balance) Values (120, 'Johnny', 'johnnycndn@yahoo.ie', 'password', 0);

class Card(Base):
    __tablename__ = 'card'

    id = Column(Integer, primary_key=True)
    card_number = Column(Integer)
    user_id = Column(ForeignKey('user.id'))
    card_details = relationship("Card_Detail", uselist=False)

class Card_Detail(Base):
    __tablename__ = 'card_detail'

    id = Column(Integer, primary_key=True)
    card_id = Column(ForeignKey('card.id'))
    value = Column(Integer)