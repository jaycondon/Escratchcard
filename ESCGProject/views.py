from ESCGProject import app
from flask import Flask, render_template, request, redirect, url_for, flash
from ESCGProject.forms import RegistrationForm

#from DBConnection import UseDatabase

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
