import asyncio
from website_monitor import Producer, Site, Settings

settings = Settings()

if __name__ == '__main__':
    producer = Producer(settings)
    loop = asyncio.get_event_loop()
    batch = []
    for site in settings.sites:
        batch.append(asyncio.ensure_future(producer.track(Site(site))))
    
    if batch:
        loop.run_until_complete(asyncio.wait(batch))