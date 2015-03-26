import os
from ESCGProject import app

import paypalrestsdk

from ESCGProject.database import init_db

app.secret_key = 'some_secret'



import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('/home/johnny/Desktop/ESCGProject/ESCGProject/cacert.pem', '/home/johnny/Desktop/ESCGProject/ESCGProject/privkey.pem')

PAYPAL_MODE = os.environ.get("PAYPAL_MODE", None)
PAYPAL_CLIENT_ID = os.environ.get("PAYPAL_CLIENT_ID",None)
PAYPAL_CLIENT_SECRET = os.environ.get("PAYPAL_CLIENT_SECRET",None)

init_db()

if not PAYPAL_MODE or not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET:
	print("Problems")
else:
	print("Mode "+PAYPAL_MODE)
	print("Client ID"+PAYPAL_CLIENT_ID)
	print("Client Secret"+PAYPAL_CLIENT_SECRET)

paypalrestsdk.configure({
  "mode": PAYPAL_MODE, # sandbox or live
  "client_id": PAYPAL_CLIENT_ID,
  "client_secret": PAYPAL_CLIENT_SECRET })

app.run(debug=True, ssl_context=context)

