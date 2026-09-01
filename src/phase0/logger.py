import logging
import logging.config
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys


def setup_logging(
    log_file: str = "app.log",
    default_level: str = "INFO",
    max_bytes: int = 5 * 1024 * 1024,  # 5 MB per file
    backup_count: int = 3,
) -> None:
 
    # Create the log directory automatically if a path like 'logs/app.log' is passed
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
            # Handler 1: Prints directly to terminal
            "console": {
                "class": "logging.StreamHandler",
                "stream": sys.stdout,
                "formatter": "default",
            },
            # Handler 2: Writes to a size-capped rotating log file
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": str(log_path),
                "maxBytes": max_bytes,
                "backupCount": backup_count,
                "encoding": "utf-8",
                "formatter": "default",
            },
        },
        # Root logger handles any module calling logging.getLogger(__name__)
        "root": {
            "level": default_level,
            "handlers": ["console", "file"],
        },
    }

    logging.config.dictConfig(config)