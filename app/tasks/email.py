from app.tasks import celery_app, TASKS
from app.services import EmailMessage

TEMPLATES = {
    'RESET_PASSWORD': {
        'en': 'a5ddfcd3-0465-4348-9b7f-458fb6459be2',
        'pt': '9ecda4f5-156d-45de-aacb-27fdcc22b9ff'
    },
    'FEEDBACK': {
        'en': '61858e5f-e6bc-4d33-b32e-cbb878a0b629',
        'pt': 'f7c790c6-33b1-4ac5-85c5-c7c7ec38cfce'
    },
    'ORDER_CONFIRMATION': {
        # 'en': '61858e5f-e6bc-4d33-b32e-cbb878a0b629',
        'pt': '87f63d0a-9e85-475f-bf6e-118efeddb0f8'
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


@celery_app.task(name=TASKS['FEEDBACK_EMAIL'])
def feedback_email(user, feedback_url):
    """
    Send email to ask user for feedback
    :param user:
    :param feedback_url:
    :return:
    """
    lang = user['language']
    data = {
        '[feedbackUrl]': feedback_url
    }

    email = EmailMessage()
    email.send(
        email_to=user['email'],
        substitutes=data,
        template_id=TEMPLATES['FEEDBACK'][lang]
    )


@celery_app.task(name=TASKS['ORDER_CONFIRMATION_EMAIL'])
def order_confirmation_email(user, order):
    """
    Send email to confirm order
    :param user:
    :param order:
    :return:
    """
    lang = user['language']
    data = {
        '[user.name]': user['name'],
        '[order.number]': order['number'],
        '[order.hours]': order['hours'],
        '[order.extras]': order['extras'],
        '[order.date]': order['date'],
        '[order.startTime]': order['startTime'],
        '[order.endTime]': order['endTime'],
        '[address]': order['address'],
        '[address.district]': order['addressDistrict'],
        '[address.city]': order['addressCity'],
        '[cleaner.name]': order['cleanerName'],
        '[order.unitPrice]': order['unitPrice'],
        '[order.totalPrice]': order['totalPrice'],
        '[order.paymentMethod]': order['paymentMethod'],
    }

    email = EmailMessage()
    email.send(
        email_to=user['email'],
        substitutes=data,
        template_id=TEMPLATES['ORDER_CONFIRMATION'][lang]
    )
