from enum import Enum
import logging
class LoggerInfo(Enum):
    """
    Enum for logger information.
    """
    LOG_LEVEL = logging.INFO
    MAX_BYTES = 5 * 1024 * 1024  # 5 MB
    BACKUP_COUNT = 3
    LOG_FILE = "logs/stock_streaming.log"