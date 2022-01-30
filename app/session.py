from decouple import config

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models import Base

Session = sessionmaker()
engine = create_engine(config("URI"))
Session.configure(bind=engine)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
