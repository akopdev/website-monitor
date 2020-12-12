from kafka import KafkaConsumer
from .result import Result
import json

class Consumer():
    def __init__(self, server: str = None) -> None:
        self.messages = KafkaConsumer('topic',
                                     bootstrap_servers=[server],
                                     auto_offset_reset='earliest',
                                     enable_auto_commit=True,
                                     value_deserializer=lambda v: Result(**json.loads(v.decode('utf-8'))))

    def log(self, result: Result):
        print(result.url)
    
    def subscribe(self):
        for message in self.messages:
            if isinstance(message.value, Result):
                self.log(message.value)
