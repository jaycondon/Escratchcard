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
    credit_cards = relationship("CreditCard")
#insert into user (id,name,email,password,balance) Values (120, 'Johnny', 'johnnycndn@yahoo.ie', 'password', 0);

class CreditCard(Base):
    __tablename__ = 'credit_card'

    id = Column(Integer, primary_key=True)
    usersCC = relationship("User")
    user_id = Column(ForeignKey('user.id'))


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