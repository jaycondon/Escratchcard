from ESCGProject import app
app.secret_key = 'some_secret'

import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('/home/johnny/Desktop/ESCGProject/ESCGProject/cacert.pem', '/home/johnny/Desktop/ESCGProject/ESCGProject/privkey.pem')

app.config['DB_HOST'] = '127.0.0.1'
app.config['DB_USER'] = 'root'
app.config['DB_PASSWD'] = 'itcarlow'
app.config['DB'] = 'ESCGdb'

app.run(debug=True, ssl_context=context)
