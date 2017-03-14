import os

SLACK_TOKEN = os.environ.get('SLACK_TOKEN', 'slack_token')
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')
RABBITMQ_USER = os.environ.get('RABBITMQ_USER', 'tdlimpo')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD', 'tdlimpo_password')
