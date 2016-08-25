from app.resources import auth
from app.services.slack_service import SlackMessage
from flask import abort
from flask_restful import Resource, reqparse, fields, marshal_with

address_fields = {
    'message': fields.String
}


class SlackAPI(Resource):
    """
    Resource to manage slack messages
    """
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('message', type=str, required=True, help='No message provided', location='json')
        super(SlackAPI, self).__init__()

    @auth.login_required
    def post(self, channel):

        # Post new message
        args = self.parser.parse_args()
        message = SlackMessage(message=args['message'], channel=channel)
        message.send()

        return {"success": True}, 200
