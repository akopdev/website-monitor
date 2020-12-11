from website_monitor import Producer, Site
from faker import Faker

fake = Faker()

def test_website_available():
    producer = Producer()
    result = producer.ping("https://google.com")
    assert result.is_success()

def test_website_not_available():
    producer = Producer()
    result = producer.ping(fake.dga())
    assert result.is_failed()
