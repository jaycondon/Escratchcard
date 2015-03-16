import logging

from ESCGProject import app
from flask import Flask, render_template, request, redirect, url_for, flash
from ESCGProject.forms import RegistrationForm

from ESCGProject.database import db_session, init_db
from ESCGProject.models import Card




@app.route('/')
def hello_world():
	return redirect(url_for('login'))
#    return 'Hello World!'

@app.route('/details')
def details():
	form = RegistrationForm(request.form)
	return render_template('details.html', form=form)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template('main.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		user = form.username.data
#		db_session.add(user)
		flash('Thanks for registering')
		return redirect(url_for('main'))
	return render_template('register.html', form=form)
       # user = User(form.username.data, form.email.data,
        #            form.password.data)

@app.route('/buyCard', methods=['GET', 'POST'])
def buyCard():
	init_db()
	if len(Card.query.all()) < 20:
		i = 0		
		while i < 120:
#			obj = db_session.query(Card).order_by(Card.number.desc()).first()
			obj = Card.query.order_by(Card.number.desc()).first()
			logging.debug(obj)
			if obj is None:
				obj = i
			eachCard = Card(obj, None)
			print(obj)
			db_session.add(eachCard)
			db_session.commit()
			i+=1
	return "Hello World!"	
