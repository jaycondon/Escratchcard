from flask import Flask, render_template

import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('/home/johnny/Desktop/ESCGProject/cacert.pem', '/home/johnny/Desktop/ESCGProject/privkey.pem')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=12344, debug = True, ssl_context=context)
