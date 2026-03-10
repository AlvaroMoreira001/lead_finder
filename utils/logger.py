from loguru import logger
from pathlib import Path


LOG_DIR = Path("data/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

logger.add(LOG_FILE, rotation="1 MB", retention="7 days", encoding="utf-8")

__all__ = ["logger"]
