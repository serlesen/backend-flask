class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://sergio:my-password@localhost:5432/backenddb"
    LOGGING = {
        "version": 1,
        "filters": {
            "backend_filter": {
                "backend_module": "backend",
            }
        },
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
                "filters": ["backend_filter"],
            },
            "file": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "level": "DEBUG",
                "filename": "backend.log",
                "when": "D",
                "interval": 1,
                "formatter": "standard",
            },
            "http": {
                "class": "logging.handlers.HTTPHandler",
                "host": "localhost:5001",
                "url": "/log",
                "method": "POST",
            },
            "z_buffer": {
                "class": "logging.handlers.MemoryHandler",
                "capacity": 3,
                "target": "http",
            },
        },
        "loggers": {
            "": {"handlers": ["console", "z_buffer"], "level": "DEBUG"},
            "flask": {"level": "WARNING"},
            "sqlalchemy": {"level": "WARNING"},
            "werkzeug": {"level": "WARNING"},
        },
        "disable_existing_loggers": False,
    }
