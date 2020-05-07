from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1'] #, 'mailerProdDNS'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3hhf7uuqs8urf',
        'USER': 'iurwfyuzlevukw',
        'PASSWORD': 'b284a25be8fd5f9c4d10dd0b854a7dd752ac9be36b2b1fc5d93e8f53466419b6',
        'HOST': 'ec2-34-234-228-127.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'buttler',         # Or path to database file if using sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': 'postgres',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'd3hhf7uuqs8urf',         # Or path to database file if using sqlite3.
        'USER': 'iurwfyuzlevukw',                      # Not used with sqlite3.
        'PASSWORD': 'b284a25be8fd5f9c4d10dd0b854a7dd752ac9be36b2b1fc5d93e8f53466419b6',                  
        'HOST': 'ec2-34-234-228-127.compute-1.amazonaws.com
',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}
Host
ec2-34-234-228-127.compute-1.amazonaws.com
Database
d3hhf7uuqs8urf
User
iurwfyuzlevukw
Port
5432
Password
b284a25be8fd5f9c4d10dd0b854a7dd752ac9be36b2b1fc5d93e8f53466419b6
URI
postgres://iurwfyuzlevukw:b284a25be8fd5f9c4d10dd0b854a7dd752ac9be36b2b1fc5d93e8f53466419b6@ec2-34-234-228-127.compute-1.amazonaws.com:5432/d3hhf7uuqs8urf
Heroku CLI
heroku pg:psql postgresql-cubic-01445 --app buttlerdj
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mysite.sqlite3',         # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
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


'''
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
