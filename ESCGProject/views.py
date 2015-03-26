import logging

from ESCGProject import app
from flask import Flask, render_template, request, redirect, url_for, flash, session
from ESCGProject.forms import RegistrationForm, LoginForm, PaymentForm
from ESCGProject.utils import RetrieveCard

from ESCGProject.database import db_session
from ESCGProject.models import *

from ESCGProject.paypal import MakeAPayment, StoreACard

from sqlalchemy.exc import StatementError, SQLAlchemyError

import random
import os


balance = 0

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
		current_user = db_session.query(User).filter(User.name==session['username']).first()
		url_for('static', filename='style.css',image='static/thewinner.jpg')
		return render_template('main.html',balance=current_user.balance)
	return redirect(url_for('login'))


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


@app.route('/buyCard', methods=['GET', 'POST'])
def buyCard():
	if 'username' in session:
		a_card = RetrieveCard()
		current_user = db_session.query(User).filter(User.name==session['username']).first()
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

@app.route('/Deposit', methods=['GET', 'POST'])
def DepositMoney():
	if 'username' in session:
		form = PaymentForm(request.form)
		if request.method == 'POST':
			print("INSIDE POST")
			current_user = db_session.query(User).filter(User.name==session['username']).first()
			topUp = MakeAPayment(form.card_type.data,form.number.data,form.month.data,form.year.data,form.cvv2.data,form.firstname.data,form.lastname.data,form.totalAmount.data)
			if topUp is None:
				topUp = 0
			current_user.balance = current_user.balance + topUp
			db_session.commit()
			return redirect(url_for('main'))
		return render_template('addcard.html',form=form)

@app.route('/AddCard', methods=['GET', 'POST'])
def AddCard():
	if 'username' in session:
		form = AddCardForm(request.form)
		if request.method == 'POST':
			current_user = db_session.query(User).filter(User.name==session['username']).first()
			StoreACard(form.card_type.data,form.number.data,form.month.data,form.year.data,form.cvv2.data,form.firstname.data,form.lastname.data,current_user.id)	
		return render_template('addcard.html',form=form)
	return redirect(url_for('login'))

@app.route('/*', methods=['GET', 'POST'])
def WrongUrl():
	return redirect(url_for('main'))
