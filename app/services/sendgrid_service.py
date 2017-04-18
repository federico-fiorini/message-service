import sendgrid
import urllib.error
from sendgrid.helpers.mail import *
from app.config import SENDGRID_API_KEY, TD_LIMPO_EMAIL_SENDER
from app import logger


class EmailMessage:

    def __init__(self):
        """
        Init email message with sendgrid service
        """
        self.sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
        self.from_email = Email(TD_LIMPO_EMAIL_SENDER)

    def send(self, email_to, substitutes, template_id):
        """
        Send email message with given template and substitutes
        :param email_to:
        :param substitutes:
        :param template_id:
        :return:
        """
        mail_helper = Mail()
        mail_helper.set_template_id(template_id)
        mail_helper.set_from(self.from_email)

        personalization = Personalization()

        for key, value in substitutes.items():
            personalization.add_substitution(Substitution(key, value))

        to_email = Email(email_to)
        personalization.add_to(to_email)
        mail_helper.add_personalization(personalization)

        try:
            self.sg.client.mail.send.post(request_body=mail_helper.get())
        except urllib.error.HTTPError as err:
            errors = json.loads(err.read().decode("utf8", 'ignore'))
            errors = '; '.join(list(map(lambda x: x['message'], errors['errors'])))
            logger.error("Sendgrid API returned %s with following errors: %s" % (err.code, errors))
