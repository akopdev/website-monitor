import time
from .enums import Status

class Result(object):

    def __init__(self, url: str) -> None:
        self.url = url
        self.status = None
        self.content = None
        self.duration = None
        self.end = None
        self.start = time.time()

    def get_response_duration(self) -> int:
        self.end = time.time()
        self.duration = self.end - self.start
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

