from app import api
from app.resources import *


# Slack
api.add_resource(SlackAPI, '/slack/<string:channel>', endpoint='index')
