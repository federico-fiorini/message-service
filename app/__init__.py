from flask import Flask
from flask_restful import Api

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config.from_object('config')

api = Api(app)

from app import routes