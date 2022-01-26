from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, Text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, nullable=False)
    player_score = Column(Integer, nullable=False)
    game_time = Column(Float, nullable=False)


class PlayerDetail(Base):
    __tablename__ = "player_details"
    id = Column(Integer, primary_key=True)
    player_name = Column(Text, nullable=False)
    password_hash = Column(Text, nullable=False)
    created_date = Column(DateTime, nullable=False)


class PlayerState(Base):
    __tablename__ = "player_states"
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, nullable=False)
    player_name = Column(Text, nullable=False)
    head_equipped = Column(Text, nullable=False)


class StoreItem(Base):
    __tablename__ = "store_items"
    id = Column(Integer, primary_key=True)
    item_name = Column(Text, nullable=False)
    item_type = Column(Text, nullable=False)
    item_price = Column(Integer, nullable=False)


class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, nullable=False)
    item_name = Column(Text, nullable=False)
    item_price = Column(Text, nullable=False)
