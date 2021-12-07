import os

import sqlalchemy
from sqlalchemy.orm import sessionmaker


Session = sessionmaker()

db_user = os.environ["MYSQL_USER"]
db_pass = os.environ["MYSQL_PASSWORD"]
db_name = os.environ["MYSQL_DB"]
db_host = os.environ["MYSQL_HOST"]
db_port = os.environ["MYSQL_PORT"]


def get_session():
    engine = sqlalchemy.create_engine(
        # Equivalent URL:
        # mysql+pymysql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
        sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username=db_user,  # e.g. "my-database-user"
            password=db_pass,  # e.g. "my-database-password"
            host=db_host,  # e.g. "127.0.0.1"
            port=db_port,  # e.g. 3306
            database=db_name,  # e.g. "my-database-name"
        ),
        pool_size=5,
        max_overflow=2,
        pool_timeout=30,
        pool_recycle=1800
    )
    session = Session(bind=engine)
    return session
