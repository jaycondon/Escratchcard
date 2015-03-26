from wtforms import Form, BooleanField, TextField, PasswordField, validators, IntegerField

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])

class LoginForm(Form):
    username = TextField('Username')
    password = PasswordField('Password')


class PaymentForm(Form):
    card_type = TextField('Card Type')
    number = TextField('Card Number')
    month = TextField('Expiry Month')
    year = TextField('Expiry Year')
    cvv2 = TextField('Cvv2 Number')
    firstname = TextField('First Name')
    lastname = TextField('Last Name')
    totalAmount = IntegerField('Total Amount')