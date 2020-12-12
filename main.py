import asyncio
from website_monitor import Producer, Site

sites = [
    Site("https://google.com"),
    Site("https://yahoo.com")
]

if __name__ == '__main__':
    producer = Producer(server='localhost:9092')
    loop = asyncio.get_event_loop()
    batch = []
    for site in sites:
        batch.append(asyncio.ensure_future(producer.track(site)))
    loop.run_until_complete(asyncio.wait(batch))