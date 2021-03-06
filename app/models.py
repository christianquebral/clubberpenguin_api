from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Text,
    create_engine,
)
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PlayerDetail(Base):
    __tablename__ = "player_details"
    id = Column(Integer, primary_key=True)
    player_name = Column(Text, nullable=False)
    password_hash = Column(Text, nullable=False)
    created_date = Column(DateTime, nullable=False)

    games = relationship("Game")
    purchases = relationship("Purchase")


class PlayerState(Base):
    __tablename__ = "player_states"
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, nullable=False)
    player_name = Column(Text, nullable=False)
    head_equipped = Column(Text, nullable=False)
    torso_equipped = Column(Text, nullable=False)
    date_modified = Column(DateTime, nullable=True)


class StoreItem(Base):
    __tablename__ = "store_items"
    id = Column(Integer, primary_key=True)
    item_name = Column(Text, nullable=False)
    item_type = Column(Text, nullable=False)
    item_price = Column(Integer, nullable=False)
    created_date = Column(DateTime, nullable=False)

    purchases = relationship("Purchase")


class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("player_details.id"), nullable=False)
    player_score = Column(Integer, nullable=False)
    game_time = Column(Float, nullable=False)
    created_date = Column(DateTime, nullable=False)

    player = relationship("PlayerDetail", back_populates="games")


class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("player_details.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("store_items.id"), nullable=False)
    created_date = Column(DateTime, nullable=False)

    player = relationship("PlayerDetail", back_populates="purchases")
    store_item = relationship("StoreItem", back_populates="purchases")


class APIAuth(Base):
    __tablename__ = "api_auth"
    id = Column(Integer, primary_key=True)
    api_key = Column(Text, nullable=False)
    created_date = Column(DateTime, nullable=False)
    expiration_date = Column(Date, nullable=False)
