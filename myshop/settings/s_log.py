import os.path

LOGGING_DIR = '/var/log/myshop/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    'formatters': {
        'verbose': {
            'format': (
                'P%(process)d;%(levelname)s;%(asctime)s;%(module)s;%(message)s'
            )
        },
        'simple': {
            'format': '%(levelname)s;%(message)s'
        },
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'django_log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, "django.log"),
            'maxBytes': 16777216,
            'formatter': 'verbose',
        },
    },

    # PyContracts override default logging level settings
    # so we define root logger before PyContracts initialized
    'root': {
        'handlers': ['console'],
        'level': 'WARNING'
    },

    'loggers': {
        'django.request': {
            'handlers': [
                'console', 'mail_admins', 'django_log_file',
            ],
            'level': 'WARNING',
            'propagate': True,
        },

        'djsms.send_message': {
            'handlers': ['console',],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}
