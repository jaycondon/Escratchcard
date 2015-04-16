from wtforms import Form, BooleanField, TextField, PasswordField, validators, IntegerField, StringField, HiddenField, SubmitField, IntegerField, ValidationError
import datetime

now = datetime.datetime.now()

class RegistrationForm(Form):
    hidden_tag = HiddenField()
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35),validators.Email(message="Not a valid email")])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit_button = SubmitField('Sign Up')

class LoginForm(Form):
    hidden_tag = HiddenField()
    username = TextField('Username',[validators.Required()])
    password = PasswordField('Password',[validators.Required()])
    submit_button = SubmitField('Login')

# #Taken from http://en.wikipedia.org/wiki/Luhn_algorithm
# def luhn_checksum(card_number):
#     def digits_of(n):
#         return [int(d) for d in str(n)]
#     digits = digits_of(card_number)
#     odd_digits = digits[-1::-2]
#     even_digits = digits[-2::-2]
#     checksum = 0
#     checksum += sum(odd_digits)
#     for d in even_digits:
#         checksum += sum(digits_of(d*2))
#     print(checksum)
#     return checksum % 10
 
# def is_luhn_valid(card_number):
#     return luhn_checksum(card_number) == 0

# Taken from http://rosettacode.org/wiki/Luhn_test_of_credit_card_numbers#Python
def luhn(n):
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0


def check_card_no(form, field):
    print(luhn(field.data))
    if luhn(field.data) is False:
        raise ValidationError('This cards number is invalid')

def validate_month(form, field):
    if field.data < 1 or field.data > 12:
        raise ValidationError('The month you have entered is incorrect. Please enter a digit between 1 and 12 (M). 1 for January and  12 for December')
    elif form.year.data == now.year and field.data < now.month:
        raise ValidationError('This card has expired')

def validate_year(form, field):
    if len(str(field.data)) < 4:
        raise ValidationError('The year you have entered is incorrect. Please enter a 4 digit number for the year. (YYYY)')
    elif field.data < now.year:
        print(now.year)
        raise ValidationError('This card has expired')

class PaymentForm(Form):
    hidden_tag = HiddenField()
    card_type = StringField('Card Type',[validators.Required()])
    number = StringField('Card Number',[validators.Required(),check_card_no])
    month = IntegerField('Expiry Month(M)',[validators.Required(),validate_month])
    year = IntegerField('Expiry Year(YYYY)',[validators.Required(),validate_year])
                                                                                #taken from http://regexlib.com/
    cvv2 = StringField('Cvv2 Number',[validators.Required(),validators.Regexp("^([0-9]{3,4})$", flags=0, message="That is not a valid cvv number")])
    firstname = StringField('First Name',[validators.Required()])
    lastname = StringField('Last Name',[validators.Required()])
                                                                                        #taken from http://regexlib.com/
    totalAmount = StringField('Deposit Amount',[validators.Required(), validators.Regexp("^\$?([0-9]{1,3},([0-9]{3},)*[0-9]{3}|[0-9]+)(.[0-9][0-9])?$", flags=0, message="That is not a valid currency. Try. 1234.12")])
 #   totalAmount = IntegerField('Total Amount',[validators.Required()])
    submit_button = SubmitField('Deposit')

#,validators.Regexp("([0-9]{2})", flags=0, message="That is not the correct format for Month. Try (MM)")


class WithdrawForm(Form):
    hidden_tag = HiddenField()
    totalAmount = StringField('Withdraw Amount',[validators.Required(), validators.Regexp("^\$?([0-9]{1,3},([0-9]{3},)*[0-9]{3}|[0-9]+)(.[0-9][0-9])?$", flags=0, message="That is not a valid currency. Try. 1234.12")])
    submit_button = SubmitField('Withdraw')