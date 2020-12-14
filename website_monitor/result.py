import time
from .enums import Status

class Result(object):

    def __init__(self, url: str, code: int = None, status: Status = None, content: str = None, duration: float = None, time_end: time = None, time_start: time = None) -> None:
        self.url = url
        self.status = status
        self.code = code
        self.content = content
        self.duration = duration
        self.time_end = time_end
        self.time_start = time.time()
        if time_start:
           self.time_start = time_start 

    def get_response_duration(self) -> int:
        self.time_end = time.time()
        self.duration = self.time_end - self.time_start
        return self.duration

    def success(self, content: str, code: int = 200) -> None:
        self.content = content
        self.status = Status.SUCCESS
        self.code = code
        self.get_response_duration()

    def is_success(self):
        return self.status is Status.SUCCESS

    def failed(self, code: int = 500) -> None:
        self.status = Status.FAILED
        self.code = code
        self.get_response_duration()

    def is_failed(self):
        return self.status is Status.FAILED

