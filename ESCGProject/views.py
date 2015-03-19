import logging

from ESCGProject import app
from flask import Flask, render_template, request, redirect, url_for, flash, session
from ESCGProject.forms import RegistrationForm, LoginForm
from ESCGProject.utils import RetrieveCard

from ESCGProject.database import db_session
from ESCGProject.models import *

from sqlalchemy.exc import StatementError, SQLAlchemyError

import random
import os


balance = 0
#from ESCGProject.database import db_session, init_db
#from ESCGProject.models import Card, Card_Detail, User

#import random

#TOP_PRIZE = 20
#SECOND_PRIZE = 10
#THIRD_PRIZE = 5
#FOURTH_PRIZE = 2
#FIFTH_PRIZE = 1

#TOP_CHANCE = 1
#SECOND_CHANCE = 2
#THIRD_CHANCE = 4
#FOURTH_CHANCE = 6
#FIFTH_CHANCE = 7

#CREATE_CARD = 120
#MIN_CARD = 20

#@app.route('/')
#def hello_world():
#	return redirect(url_for('login'))
#    return 'Hello World!'

#@app.route('/details')
#def details():
#	form = RegistrationForm(request.form)
#	return render_template('details.html', form=form)
@app.route('/', methods=['GET', 'POST'])
def unused():
	return redirect(url_for('main'))

@app.route('/details', methods=['GET', 'POST'])
def details():
	if 'username' in session:
		return "Details"
	else:
		return redirect(url_for('main'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method =='POST':
		user = db_session.query(User).filter(User.name==form.username.data).filter(User.password==form.password.data).first()
		if not user:
			flash('User name or password incorrect')
			return redirect(url_for('login'))
		else:
			session['username'] = form.username.data
			return redirect(url_for('main'))
	return render_template('login.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
	if 'username' in session:
		url_for('static', filename='style.css',image='static/thewinner.jpg')
		return render_template('main.html')
	return redirect(url_for('login'))
#	get_a_card = db_session.query(Card.id, Card_Detail.value).join(Card_Detail, Card.id==Card_Detail.card_id).filter(Card.user_id==None)
#	rand_card = random.randrange(0, get_a_card.count(), 1)
#	print(get_a_card[rand_card].value)
#	print(get_a_card[rand_card].id)


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		user = User()
		user.name = form.username.data
		user.email = form.email.data
		user.password = form.password.data
		user.balance = 0
		db_session.add(user)
		db_session.commit()
		flash('Thanks for registering')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)
       # user = User(form.username.data, form.email.data,
        #            form.password.data)

#def FillCards(chance,prize):
#	if chance == 0:
#		return
#	else:
#		available = db_session.query(Card_Detail).join(Card, Card_Detail.card_id==Card.id).filter(Card_Detail.value==0).filter(Card.user_id==None)
#		rand_number = random.randrange(0, available.count(), 1)
#		available[rand_number].value = prize
#		chance-=1
#		db_session.commit()
#		FillCards(chance, prize)

@app.route('/buyCard', methods=['GET', 'POST'])
def buyCard():
	if 'username' in session:
		a_card = RetrieveCard()
		current_user = db_session.query(User).filter(User.id==120).first()
		put_user = db_session.query(Card).filter(Card.id==a_card.id).first()
		put_user.user_id=current_user.id
		db_session.commit()
		if a_card.value == 0:
			amount = random.choice([1,2,5,10,20])
		else:
			current_user.balance = current_user.balance + a_card.value
			db_session.commit()
			amount = a_card.value
		return render_template('main.html',amount=amount,balance=current_user.balance)
	else:
		return redirect(url_for('login'))

@app.route('/*', methods=['GET', 'POST'])
def WrongUrl():
	return redirect(url_for('main'))