import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'prepend_date': {
            'format': '{asctime} {levelname}: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'prepend_date',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

logging.config.dictConfig(LOGGING)
logging.info('foo')
logging.warning('bar')