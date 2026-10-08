import logging
from logging.config import dictConfig


def setup_logger(name: str = "rag_app") -> logging.Logger:
    dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": "INFO"
            }
        },
        "root": {
            "handlers": ["console"],
            "level": "INFO"
        }
    })
    return logging.getLogger(name)
