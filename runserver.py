import os
from ESCGProject import app
import stripe

app.secret_key = 'some_secret'

import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('/home/johnny/Desktop/ESCGProject/ESCGProject/cacert.pem', '/home/johnny/Desktop/ESCGProject/ESCGProject/privkey.pem')

stripe_keys = {
#	'secret_key': os.environ['SECRET_KEY'],
# 	'publishable_key': os.environ['PUBLISHABLE_KEY']
	'secret_key': 'sk_test_90QSPzGyaKLlKGWF2pc1rLX8',
 	'publishable_key': 'pk_test_8YSPSyKffBfyXamjvd1RLsWe'
}


stripe.api_key = stripe_keys['secret_key']

app.run(debug=True, ssl_context=context)

