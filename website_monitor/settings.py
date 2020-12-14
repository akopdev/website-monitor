import os


class Settings():
    def __init__(self, broker_server: str = None, broker_topic: str = None, storage_host: str = None, storage_user: str = None, storage_password: str = None, storage_db: str = None) -> None:
        self.broker_server = os.getenv('BROKER_SERVER', broker_server)
        self.broker_topic = os.getenv('BROKER_TOPIC', broker_topic)
        self.storage_user = os.getenv('STORAGE_USER', storage_user)
        self.storage_password = os.getenv('STORAGE_PASSWORD', storage_password)
        self.storage_host = os.getenv('STORAGE_HOST', storage_host)
        self.storage_db = os.getenv('STORAGE_DB', storage_db)