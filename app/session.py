from decouple import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

Session = sessionmaker()
engine = create_engine(config("URI"))
Base.metadata.create_all(bind=engine)
Session.configure(bind=engine)

session = Session()
session.commit()
