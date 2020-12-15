from .settings import Settings
from .result import Result
from .site import Site
from .log import log
import requests
import re
import asyncio
import json

from kafka import KafkaProducer

class Producer():
    def __init__(self, settings: Settings, timeout: int = 30) -> None:
        self.timeout = timeout
        self.settings = settings
        try:
            self.message = KafkaProducer(bootstrap_servers=[settings.broker_server], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        except Exception as error:
            log.error("Broker server error: {0}".format(error))
            raise Exception(error)
    
    def get_result(self, url: str) -> Result:
        result = Result(url)
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            result.success(response.text)
        except requests.exceptions.ConnectionError:
            result.failed(503)
        except requests.exceptions.Timeout:
            result.failed(408)
        except Exception:
            result.failed()
        return result

    def ping(self, url: str, pattern: str = None) -> Result:
        result = self.get_result(url)
        if pattern and result.content:
            if not re.search(pattern, result.content):
                result.failed(404)
                log.warning("Failed to reg match {0} pattern for {1}".format(pattern, result.url))
        if self.message:
            log.info("Producer is sending {0} data to consumer.".format(result.url))
            self.message.send(self.settings.broker_topic, result.__dict__)
        return result

    async def track(self, site: Site, pause: int = 5) -> None:
        while True:
            self.ping(site.url, pattern=site.pattern)
            await asyncio.sleep(pause)
            