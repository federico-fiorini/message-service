FROM python:3

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
WORKDIR /home/user

COPY . /home/user
ENV CELERY_CONFIG_MODULE app.celeryconfig

ENV CELERY_VERSION 4.0.2

RUN pip3 install celery=="$CELERY_VERSION"
RUN pip3 install -r /home/user/requirements.txt

RUN mkdir -p /var/log/message-service
RUN touch /var/log/message-service/message-service.log
RUN chmod 775 /var/log/message-service/message-service.log
ENV LOG_FILE /var/log/message-service/message-service.log

USER user
CMD ["celery", "worker"]
