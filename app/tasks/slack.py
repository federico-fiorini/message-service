from app.tasks import celery_app, TASKS
from app.services.slack_service import SlackMessage


@celery_app.task(name=TASKS['SLACK_MESSAGE'])
def send_slack_message(message, channel):
    """
    Send slack message to give channel
    :param message:
    :param channel:
    :return:
    """
    message = SlackMessage(message=message, channel=channel)
    message.send()
