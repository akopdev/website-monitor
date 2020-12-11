from website_monitor import Producer

def test_basic():
    producer = Producer()
    result = producer.ping("https://google.com")

    assert hasattr(result, 'status')
    assert result.status is 200