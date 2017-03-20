import os

SLACK_TOKEN = os.environ.get('SLACK_TOKEN', 'slack_token')
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', 'sendgrid_api_key')
TD_LIMPO_EMAIL_SENDER = "no-reply@tdlimpo.com.br"
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')
RABBITMQ_USER = os.environ.get('RABBITMQ_USER', 'tdlimpo')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD', 'tdlimpo_password')
LOG_FILE = os.environ.get('LOG_FILE', '/tmp/message-service.log')
