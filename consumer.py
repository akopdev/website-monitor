import asyncio
from website_monitor import Consumer

if __name__ == '__main__':
    consumer = Consumer(server='localhost:9092')
    consumer.subscribe()