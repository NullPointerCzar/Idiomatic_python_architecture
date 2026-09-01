import logging
import logging.config
import sys
from pathlib import Path


def setup_logging(
    log_file: str = "app.log",
    default_level: str = "INFO",
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 3,
) -> None:

    """Configures project-wide logging to both terminal and a rotating log file."""

    log_path = Path(log_file)

    if log_path.parent != Path("."):
        log_path.parent.mkdir(parents=True, exist_ok=True)

    config = {
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "default": {
                "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": sys.stdout,
                "formatter": "default",
            },

            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": str(log_path),
                "maxBytes": max_bytes,
                "backupCount": backup_count,
                "encoding": "utf-8",
                "formatter": "default",
            },
        },

        "root": {
            "level": default_level,
            "handlers": ["console", "file"],
        },
    }

    logging.config.dictConfig(config)


# Application startup
setup_logging(
    log_file="app.log",
    default_level="DEBUG",
)

# Anywhere in your application
logger = logging.getLogger(__name__)

logger.info("Application started")
logger.error("Something went wrong!")