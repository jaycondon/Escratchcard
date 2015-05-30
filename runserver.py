import os
from ESCGProject import app

import paypalrestsdk

from ESCGProject.database import init_db

app.secret_key = 'some_secret'


import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('ESCGProject/cacert.pem', 'ESCGProject/privkey.pem')

init_db()

#app.debug=True
#app.run()
app.run(ssl_context=context)#host='127.0.0.1', 