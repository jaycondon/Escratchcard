from ESCGProject import app

from ESCGProject.database import db_session, init_db
from ESCGProject.models import Card, Card_Detail, User

import random

TOP_PRIZE = 20
SECOND_PRIZE = 10
THIRD_PRIZE = 5
FOURTH_PRIZE = 2
FIFTH_PRIZE = 1

TOP_CHANCE = 1
SECOND_CHANCE = 2
THIRD_CHANCE = 4
FOURTH_CHANCE = 6
FIFTH_CHANCE = 7

CREATE_CARD = 120
MIN_CARD = 20

def RetrieveCard():
	get_a_card = db_session.query(Card.id, Card_Detail.value).join(Card_Detail, Card.id==Card_Detail.card_id).filter(Card.user_id==None)
	for x in get_a_card:
		print(x)
	print(get_a_card)
	if get_a_card.count() < MIN_CARD:
		MoreCards()
	rand_card = random.randrange(0, get_a_card.count(), 1)
	print(get_a_card[rand_card].value)
	print(get_a_card[rand_card].id)
	return get_a_card[rand_card]

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