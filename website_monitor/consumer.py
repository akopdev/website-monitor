from kafka import KafkaConsumer
from .result import Result
from .storage import Storage
from .settings import Settings
from .log import log
import json


class Consumer():
    def __init__(self, settings: Settings) -> None:
        self.storage = Storage(settings)
        try:
            self.messages = KafkaConsumer(settings.broker_topic,
                                        bootstrap_servers=[settings.broker_server],
                                        auto_offset_reset='earliest',
                                        enable_auto_commit=True,
                                        value_deserializer=lambda v: Result(**json.loads(v.decode('utf-8'))))
        except Exception as error:
            log.error("Broker server error: {0}".format(error))
            raise Exception(error)

    def log(self, result: Result):
        log.info("Consumer writing data for {0} into database.".format(result.url))
        self.storage.insert(result)
    
    def subscribe(self):
        for message in self.messages:
            if isinstance(message.value, Result):
                self.log(message.value)
