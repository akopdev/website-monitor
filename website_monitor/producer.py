from .result import Result
import requests
import re

class Producer():
    def __init__(self, timeout: int = 30) -> None:
        self.timeout = timeout
        self.session = requests.Session()
    
    def get_result(self, url: str) -> Result:
        result = Result(url)
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            result.success(response.text)
        except requests.exceptions.ConnectionError:
            result.failed(503)
        except requests.exceptions.Timeout:
            result.failed(408)
        except Exception:
            result.failed()
        return result

    def ping(self, url: str, regexp: str = None) -> Result:
        result = self.get_result(url)
        if regexp and result.content:
            if not re.search(regexp, result.content):
                result.failed(404)
        return result
