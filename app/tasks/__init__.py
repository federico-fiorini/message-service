from celery import Celery
from app import celeryconfig


celery_app = Celery()
celery_app.config_from_object(celeryconfig)

TASKS = {
    'SLACK_MESSAGE': 'tasks.send_slack_message',
    'RESET_PASSWORD_EMAIL': 'tasks.reset_password_email'
}

from .slack import *
from .email import *
