import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

session = None


class LocalData:
    def __init__(self, static_data_api):
        self.static_data_api = static_data_api


def initialize_db(database_info):
    """
    Only for postgresql for now.
    """
    global session
    db_dialect = 'postgresql+psycopg2://{USER}:{PASSWORD}@/{HOST}:{PORT}'.format(**database_info)
    engine = create_engine(db_dialect, echo=False, client_encoding='utf-8')
    engine.connect()

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

