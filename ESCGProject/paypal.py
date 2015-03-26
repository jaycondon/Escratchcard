#import paypalrestsdk
import logging
from paypalrestsdk import Payout, ResourceNotFound, Payment

import os

# Include Headers and Content by setting logging level to DEBUG, particularly for
# Paypal-Debug-Id if requesting PayPal Merchant Technical Services for support
logging.basicConfig(level=logging.INFO)

#PAYPAL_MODE = os.environ.get("PAYPAL_MODE", None)
#PAYPAL_CLIENT_ID = os.environ.get("PAYPAL_CLIENT_ID",None)
#PAYPAL_CLIENT_SECRET = os.environ.get("PAYPAL_CLIENT_SECRET",None)

def MakeAPayment(cardType,cardNo,month,year,cvv2,first,last,totalAmount):
  payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
      "payment_method": "credit_card",
      "funding_instruments": [{
        "credit_card": {
          "type": cardType,
          "number": cardNo,
          "expire_month": month,
          "expire_year": year,
          "cvv2": cvv2,
          "first_name": first,
          "last_name": last }}]},
    "transactions": [{
      "amount": {
        "total": totalAmount,
        "currency": "EUR" },
      "description": "This is the payment transaction description." }]})

  if payment.create():
    print("Payment created successfully")
    return totalAmount
  else:
    print(payment.error)
    pass

def Payout():
payout = Payout({
    "sender_batch_header": {
        "sender_batch_id": "batch_1",
        "email_subject": "You have a payment"
    },
    "items": [
        {
            "recipient_type": "EMAIL",
            "amount": {
                "value": 0.99,
                "currency": "USD"
            },
            "receiver": "shirt-supplier-one@mail.com",
            "note": "Thank you.",
            "sender_item_id": "item_1"
        }
    ]
})

if payout.create(sync_mode=True):
    print("payout[%s] created successfully" %
          (payout.batch_header.payout_batch_id))
else:
    print(payout.error)

def StoreACard(cardType,cardNo,month,year,first,last,userID):
  paypalrestsdk.configure({
  "mode": PAYPAL_MODE, # sandbox or live
  "client_id": PAYPAL_CLIENT_ID,
  "client_secret": PAYPAL_CLIENT_SECRET })

  credit_card = paypalrestsdk.CreditCard({
  "type": cardType,
  "number": cardNo,
  "expire_month": month,
  "expire_year": year,
  "first_name": first,
  "last_name": last,
  "external_customer_id": userID })


  if credit_card.create(): # Return True or False
    print("Card stored successfully")
    return credit_card
  else:
    print(credit_card.error)
    pass
