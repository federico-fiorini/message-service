ERROR_404_HELP = False

import os

# Secret authorization key
AUTHORIZATION_KEY = os.environ.get('AUTHORIZATION_KEY', 'secret_token')
SLACK_TOKEN = os.environ.get('SLACK_TOKEN', 'slack_token')
