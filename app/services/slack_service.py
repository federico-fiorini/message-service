from app import app
from slackclient import SlackClient


class SlackMessage:

    def __init__(self, message, channel):
        self.slack_client = SlackClient(app.config['SLACK_TOKEN'])
        self.message = message
        self.channel = channel

    def send(self):
        self.slack_client.api_call(
            "chat.postMessage",
            channel="#%s" % self.channel,
            text=self.message,
            username='Andy',
            icon_emoji=':robot_face:'
        )