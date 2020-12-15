from .settings import Settings
from .result import Result
from .log import log
import psycopg2

class Storage():
    def __init__(self, settings: Settings) -> None:
        try:
            self.connection = psycopg2.connect(host=settings.storage_host, database=settings.storage_db, user=settings.storage_user, password=settings.storage_password)
            self.query = self.connection.cursor()

            self.query.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name=%s)", ('website_log',))
            table = self.query.fetchone()
            if not table[0]:
                try:
                    query = """
                            CREATE TABLE website_log (
                                    id BIGSERIAL PRIMARY KEY,
                                    url VARCHAR(55) NOT NULL,
                                    status VARCHAR(10) NOT NULL,
                                    code INTEGER NOT NULL,
                                    content TEXT,
                                    duration FLOAT(50) DEFAULT NULL,
                                    time_end FLOAT(50) DEFAULT NULL,
                                    time_start FLOAT(50) DEFAULT NULL
                            )
                            """
                    self.query.execute(query)
                    self.connection.commit()
                except (Exception, psycopg2.DatabaseError) as error:
                    log.error(error)
                    raise Exception(error)
        except (Exception) as error:
            log.error(error)
            raise Exception(error)



    def insert(self, result: Result):
        keys = result.__dict__.keys()
        sql = "INSERT INTO website_log({0}) VALUES({1});".format(','.join(keys), ("%s," * (len(keys)-1)) + "%s")
        try:
            self.query.execute(sql, tuple(result.__dict__.values()))
            self.connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            log.error(error)