class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://sergio:my-password@localhost:5432/backenddb"
    LOGGING = {
        "version": 1,
        "formatters": {
            "standard": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
            "compact": {"format": "%(asctime)s %(message)s"},
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "level": "DEBUG",
                "filename": "backend.log",
                "when": "D",
                "interval": 1,
                "formatter": "standard",
            },
        },
        "loggers": {
            "": {"handlers": ["console", "file"], "level": "DEBUG"},
            "flask": {"level": "WARNING"},
            "sqlalchemy": {"level": "WARNING"},
            "werkzeug": {"level": "WARNING"},
        },
        "disable_existing_loggers": False,
    }
