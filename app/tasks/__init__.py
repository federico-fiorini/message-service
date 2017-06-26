from celery import Celery
from app import celeryconfig


celery_app = Celery()
celery_app.config_from_object(celeryconfig)

TASKS = {
    'SLACK_MESSAGE': 'tasks.send_slack_message',
    'RESET_PASSWORD_EMAIL': 'tasks.reset_password_email',
    'FEEDBACK_EMAIL': 'tasks.feedback_email',
    'ORDER_CONFIRMATION_EMAIL': 'tasks.order_confirmation_email'
}

from .slack import *
from .email import *
