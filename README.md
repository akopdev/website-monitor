# Simple website monitor
Example application, describes basic concept of distributed website monitoring system.

## Features
- Periodically checks the target websites and sends the check results to a Kafka topic
- Consumer storing the data to an PostgreSQL database
- Collects the HTTP response time, error code returned, as well as optionally checking the returned page contents for a regexp pattern that is expected to be found on the page.
- Ability to define check period per website
- Supports for multi-threding

## Install

If you are going to use `docker`, simply skip this step, otherwise use `pip` to install all requirements.

```shell
$ pip install -r requirements.txt
```

## Run

Recommended way is to run application using `docker-compose`.

```shell
$ docker-compose up -d
```

If you are doing to run it on host machine, be sure you have already installed `Kafka` and `PostgreSQL` on your own. Then:

```shell
$ python3 producer.py
```
and

```shell
$ python3 consumer.py
```
> In this case you have to use different machines, or any other way to demonize a process. I suggest to take a look at [`supervisor`](http://supervisord.org/installing.html) library.


## Using inside your project

You can import and use library as a part of your own application.

At this example we collect website metrics, and send them to consumer.

```python 
from website_monitor import Producer, Settings

settings = Settings(broker_server='localhost:9092', broker_topic='demo_stream')

producer = Producer(settings)
producer.ping("https://google.com")
```


## Tests

Covered by `pytest`

```shell
python -m pytest
```