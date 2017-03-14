from app.config import RABBITMQ_HOST, RABBITMQ_PASSWORD, RABBITMQ_USER


broker_url = "amqp://%s:%s@%s" % (RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_HOST)
accept_content = ['pickle', 'json', 'msgpack', 'yaml']
imports = ('app.tasks',)