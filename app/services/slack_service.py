from app import config
from slackclient import SlackClient


class SlackMessage:

    def __init__(self):
        self.slack_client = SlackClient(config.SLACK_TOKEN)

    def send(self, message, channel):
        """
        Send slack message to channel
        :param message:
        :param channel:
        :return:
        """
        self.slack_client.api_call(
            "chat.postMessage",
            channel="#%s" % channel,
            text=message,
            username='Andy',
            icon_emoji=':robot_face:'
        )
