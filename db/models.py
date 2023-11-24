# Imports
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(Integer(), nullable=False, default=0)
    username = Column(String(), default="None")
    name = Column(String(), default="None")
    surname = Column(String(), default="None")

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(Integer(), nullable=False, default=0)
    date = Column(DateTime(), default=datetime.now())
    number = Column(Integer())

class BannedUser(Base):
    __tablename__ = 'banned_users'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(Integer(), nullable=False)

