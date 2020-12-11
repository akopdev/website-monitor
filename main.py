import asyncio
from website_monitor import Producer, Site
from random import randint

sites = [
    Site("https://google.com"),
    Site("https://yahoo.com")
]

if __name__ == '__main__':
    producer = Producer()
    loop = asyncio.get_event_loop()
    batch = []
    for site in sites:
        pause = randint(0, 10)
        batch.append(asyncio.ensure_future(producer.track(site, pause=pause)))
        print("Pause {0} for {1} secs".format(site.url, pause))
    loop.run_until_complete(asyncio.wait(batch))