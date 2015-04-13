from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from ESCGProject.models import *

import random

TOP_PRIZE = 20
SECOND_PRIZE = 10
THIRD_PRIZE = 5
FOURTH_PRIZE = 2
FIFTH_PRIZE = 1

TOP_CHANCE = 2
SECOND_CHANCE = 4
THIRD_CHANCE = 8
FOURTH_CHANCE = 12
FIFTH_CHANCE = 14

CREATE_CARD = 120
MIN_CARD = 20

engine = create_engine('mysql+pymysql://root:itcarlow@localhost/ESCGdb', convert_unicode=True, echo=False)
#metadata = MetaData()
#Base.metadata.create_all(engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=True,
                                         bind=engine))
def init_db():
    Base.metadata.create_all(bind=engine)

def CheckUser(name, password):
	return db_session.query(User).filter(User.name==name).filter(User.password==password).first()

def GetUser(name):
	return db_session.query(User).filter(User.name==name).first()

def AddUser(name,email,password):
	user = User()
	user.name = name
	user.email = email
	user.password = password
	user.balance = 0
	db_session.add(user)
	db_session.commit()

def CheckCard(card_id,session_user):
	theCard = db_session.query(Card.id, Card_Detail.value).join(Card_Detail, Card.id==Card_Detail.card_id).filter(Card.id==card_id).first()
	theUser = GetUser(session_user)
	print("inside CheckCard")
	print(theCard)
	if theCard.value > 0:
		winnings = theCard.value
		theUser.balance = theUser.balance + winnings
		db_session.commit()
	return theUser


def RetrieveCard():
	get_a_card = db_session.query(Card.id, Card_Detail.value).join(Card_Detail, Card.id==Card_Detail.card_id).filter(Card.user_id==None)
	if get_a_card.count() < 1:
		MoreCards()
	rand_card = random.randrange(0, get_a_card.count(), 1)
	return get_a_card[rand_card]

def AddCardToUser(card_id,user_id):
	the_card = db_session.query(Card).filter(Card.id==card_id).first()
	the_card.user_id=user_id
	db_session.commit()

def GetBalance(name):
	return db_session.query(User.balance).filter(User.name==name).first()

def FillCards(chance,prize):
	if chance == 0:
		return
	else:
		available = db_session.query(Card_Detail).join(Card, Card_Detail.card_id==Card.id).filter(Card_Detail.value==0).filter(Card.user_id==None)
		rand_number = random.randrange(0, available.count(), 1)
		available[rand_number].value = prize
		chance-=1
		db_session.commit()
		FillCards(chance, prize)

def MoreCards():
#	init_db()
	print("print inside buy card")
#	if len(db_session.query(Card).all()) < MIN_CARD:
#		print("print Less than 20")
	
	i = 0
	last_card = db_session.query(Card).first()
	print(last_card)
	if last_card is None:
		last_card = Card()
		last_card.card_number = i
		last_card.card_details = Card_Detail(value=0)
		db_session.add(last_card)
		db_session.commit()
	
	while i < CREATE_CARD:
		last_card.card_number+=1
		each_card = Card()
		each_card.card_number = last_card.card_number
		each_card.card_details = Card_Detail(value=0)
		db_session.add(each_card)
		db_session.commit()
		i+=1

	FillCards(FIFTH_CHANCE, FIFTH_PRIZE)
	FillCards(FOURTH_CHANCE, FOURTH_PRIZE)
	FillCards(THIRD_CHANCE, THIRD_PRIZE)
	FillCards(SECOND_CHANCE, SECOND_PRIZE)
	FillCards(TOP_CHANCE, TOP_PRIZE)