from enum import Enum

class Status(str, Enum):
    SUCCESS: str = 'success'
    FAILED: str = 'failed'