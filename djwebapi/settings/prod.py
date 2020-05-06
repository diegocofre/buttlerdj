from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1'] #, 'mailerProdDNS'


""" 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mailer',
        'USER': 'user_mailer',
        'PASSWORD': 'm41lEr',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
} 

"""


"""
 LOGGING = {
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
            'level': 'INFO',
            'filename': '/home/pycode/stg/debug.log',
            'formatter': 'standard',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
        },
    },
    'loggers': {
       'bot': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'mailer': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
"""

"""
EMAIL_ACCOUNT = {
  'username' : '',
  'password' : '',
  'imap_srv' : "imap.gmail.com",
  'smtp_srv' : "smtp.gmail.com",
   'attachment_dir' :'/home/pycode/stg',
  }

STORAGE = '/home/pycode/stg/' """
