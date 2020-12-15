from website_monitor import Consumer, Settings

settings = Settings()

if __name__ == '__main__':
    consumer = Consumer(settings)
    consumer.subscribe()