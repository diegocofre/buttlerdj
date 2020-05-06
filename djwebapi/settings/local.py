from __future__ import absolute_import
from .base import *

DEBUG = True

""" LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
       'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'filename': 'C:\\Fuentes\\buttler\\djwebapi\\djwebapi\\log\\debug.log',
            'formatter': 'standard',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
        },
    },
    'loggers': {
       'bot': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'mailer': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
} """

EMAIL_ACCOUNT = {
  'username' : 'your_email@gmail.com',
  'password' : 'verySecret',
  'imap_srv' : "imap.gmail.com",
  'smtp_srv' : "smtp.gmail.com",
   'attachment_dir' :'/home/pycode/stg',
  }

STORAGE = 'C:\\Fuentes\\buttler\\djwebapi\\storage\\'
