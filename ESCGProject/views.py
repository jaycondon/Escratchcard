import logging

from ESCGProject import app, paypal
#from ESCGProject import app, paypal
from flask import Flask, render_template, request, redirect, url_for, flash, session
from ESCGProject.forms import RegistrationForm, LoginForm, PaymentForm, WithdrawForm
from ESCGProject.utils import getImages, encrypt, decrypt

from ESCGProject.database import db_session, CheckUser, GetUser
from ESCGProject.models import *

from ESCGProject.paypal import MakeAPayment, PayOut

from sqlalchemy.exc import StatementError, SQLAlchemyError

import random
import os
import array

@app.route('/', methods=['GET', 'POST'])
def empty():
	if 'username' in session:
		return render_template('info.html')
	return redirect(url_for('login'))

@app.route('/CheckWinServer', methods=['GET', 'POST'])
def CheckWinServer():
	thecard = request.form['card_id']
	# Taken from https://www.youtube.com/watch?v=lsflaKpeB7Q
	inlist = [int(s) for s in thecard[1:-1].split(',')]
	decypted_card_id = decrypt(array.array('B', inlist).tostring())
	current_user = database.CheckCard(int(decypted_card_id),session['username'])
	balance = current_user.balance
	return str(balance)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method =='POST':
		overlay_img=url_for('static', filename='overlay.jpg')
		user = database.CheckUser(form.username.data,form.password.data)
		if not user:
			flash('User name or password incorrect')
			return render_template('login.html',form=form)
		else:
			session['username'] = form.username.data
			return render_template('info.html')
	return render_template('login.html',form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
	form = LoginForm(request.form)
	session.pop('username', None)
	return render_template('login.html',form=form)

@app.route('/main', methods=['GET', 'POST'])
def main():
	if 'username' in session:
		current_user = database.GetUser(session['username'])
		overlay_img=url_for('static', filename='overlay.jpg')
		return render_template('main.html',balance=current_user.balance,overlay_img=overlay_img)
	return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		user = database.GetUser(form.username.data)
		if user is None:
			database.AddUser(form.username.data,form.email.data,form.password.data)
			flash('Thanks for registering')
			session['username'] = form.username.data
			return render_template('info.html')
		flash('Username already exists')
		return render_template('register.html', form=form)
	return render_template('register.html', form=form)


@app.route('/buyCard', methods=['GET', 'POST'])
def buyCard():
	if 'username' in session:
		current_user = database.GetUser(session['username'])
		if current_user.balance < 1:
			flash('You do not have enough funds')
			return render_template('main.html',balance=current_user.balance,overlay_img="./static/overlay.jpg")
		else:
			current_user.balance = current_user.balance - 1
			a_card = database.RetrieveCard()
			current_user = database.GetUser(session['username'])
			database.AddCardToUser(a_card.id,current_user.id)
			encrypted_card_id = encrypt(a_card.id)
			if a_card.value == 0:
				amount = random.choice([1,2,5,10,20])
				image_list = getImages(False,6)
			else:
				db_session.commit()
				image_list = getImages(True,6)
				amount = a_card.value
			return render_template('main.html',amount=amount,balance=current_user.balance,imagelist=image_list,card_id=encrypted_card_id)
	return redirect(url_for('login'))

@app.route('/Deposit', methods=['GET', 'POST'])
def DepositMoney():
	if 'username' in session:
		form = PaymentForm(request.form)
		if request.method == 'POST' and form.validate():
			current_user = database.GetUser(session['username'])
			payment_result = paypal.MakeAPayment(form.card_type.data,form.number.data,form.month.data,form.year.data,form.cvv2.data,form.firstname.data,form.lastname.data,form.totalAmount.data)
			if payment_result == True:
				topUp = form.totalAmount.data
				current_user.balance = current_user.balance + float(topUp)
				db_session.commit()
				return render_template('main.html',balance=current_user.balance,overlay_img="./static/overlay.jpg")
			else:
				flash("Payment unsuccessful")
				return render_template('main.html',balance=current_user.balance,overlay_img="./static/overlay.jpg")
		return render_template('deposit.html',form=form)
	return redirect(url_for('login'))

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
	if 'username' in session:
		form = WithdrawForm(request.form)
		current_user = database.GetUser(session['username'])
		if request.method == 'POST'  and form.validate():
			if int(form.totalAmount.data) > current_user.balance:
				flash("You do not have enough funds")
				return render_template('withdraw.html',balance=current_user.balance,form=form)
			payout_result = PayOut(current_user.email,form.totalAmount.data)
			print(payout_result)
			if payout_result == "SUCCESS":
				current_user.balance = current_user.balance - int(form.totalAmount.data)
				db_session.commit()
			else:
				flash("There has been a problem in the payout process. Please try again")
				return render_template('withdraw.html',balance=current_user.balance,form=form)
		return render_template('withdraw.html',balance=current_user.balance,form=form)
	return redirect(url_for('main'))

@app.route('/info', methods=['GET', 'POST'])
def info():
	if 'username' in session:
		return render_template('info.html')
	return redirect(url_for('login'))
