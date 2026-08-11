"""Logging configuration for SessionHack."""
import logging
import sys


def setup_logging(level: int = logging.INFO):
    """Configure the root logger."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("sessionhack.log")
        ]
    )


def get_logger(name: str) -> logging.Logger:
    """Get a named logger instance."""
    return logging.getLogger(name)
