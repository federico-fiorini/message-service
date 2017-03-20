from app.tasks import celery_app, TASKS
from app.services import EmailMessage

TEMPLATES = {
    'RESET_PASSWORD': {
        'en': 'a5ddfcd3-0465-4348-9b7f-458fb6459be2',
        'pt': '9ecda4f5-156d-45de-aacb-27fdcc22b9ff'
    }
}


@celery_app.task(name=TASKS['RESET_PASSWORD_EMAIL'])
def reset_password_email(user, reset_password_url):
    """
    Send email to reset user password
    :param user:
    :param reset_password_url:
    :return:
    """
    lang = user['language']
    data = {
        '[user.name]': user['name'],
        '[resetPasswordUrl]': reset_password_url
    }

    email = EmailMessage()
    email.send(
        email_to=user['email'],
        substitutes=data,
        template_id=TEMPLATES['RESET_PASSWORD'][lang]
    )
