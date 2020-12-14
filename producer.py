import asyncio
from website_monitor import Producer, Site, Settings

sites = [
    Site("https://google.com"),
    Site("https://yahoo.com")
]

settings = Settings(
    broker_server='localhost:9092',
    broker_topic='demo_stream')

if __name__ == '__main__':
    producer = Producer(settings)
    loop = asyncio.get_event_loop()
    batch = []
    for site in sites:
        batch.append(asyncio.ensure_future(producer.track(site)))
    loop.run_until_complete(asyncio.wait(batch))