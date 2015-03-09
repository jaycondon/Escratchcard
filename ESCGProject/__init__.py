from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

import ESCGProject.views
import ESCGProject.DBConnection

#if __name__ == '__main__':
#    app.run(host='127.0.0.1', port=12344, debug = True, ssl_context=context)
