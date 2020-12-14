from website_monitor import Consumer, Settings

settings = Settings(
    broker_server='localhost:9092',
    broker_topic='demo_stream',
    storage_host='localhost',
    storage_user='demo',
    storage_password='demo',
    storage_db='demo')

if __name__ == '__main__':
    consumer = Consumer(settings)
    consumer.subscribe()