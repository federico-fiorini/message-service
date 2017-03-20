import logging
from logging.handlers import RotatingFileHandler
from app.config import LOG_FILE

handler = RotatingFileHandler(LOG_FILE, maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)

logger = logging.getLogger()
logger.addHandler(handler)
