from wtforms import Form, BooleanField, TextField, PasswordField, validators, IntegerField, StringField

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35),validators.Email(message="Not a valid email")])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

class LoginForm(Form):
    username = TextField('Username')
    password = PasswordField('Password')


class PaymentForm(Form):
    card_type = StringField('Card Type')
    number = StringField('Card Number')
    month = IntegerField('Expiry Month')
    year = IntegerField('Expiry Year')
    cvv2 = StringField('Cvv2 Number')
    firstname = StringField('First Name')
    lastname = StringField('Last Name')
    totalAmount = IntegerField('Total Amount')

class WithdrawForm(Form):
    totalAmount = StringField('Withdraw Amount')