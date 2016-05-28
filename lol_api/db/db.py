from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

session = None

Base = declarative_base()


def initialize_db(database_info):
    """
    Only for postgresql for now.
    """
    global session
    if session is None:
        print('session already created')
        return 0
    db_dialect = 'postgresql+psycopg2://{USER}:{PASSWORD}@/{HOST}:{PORT}'.format(**database_info)
    engine = create_engine(db_dialect, echo=False, client_encoding='utf-8')
    engine.connect()

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()


def create_tables():
    Base.metadata.create_all()
