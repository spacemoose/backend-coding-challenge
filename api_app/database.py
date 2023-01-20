from sqlalchemy import create_engine
from databases import  Database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///../bookings.db"

database = Database(DATABASE_URL)
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

def get_database() -> Database:
    return database

Base=declarative_base()
