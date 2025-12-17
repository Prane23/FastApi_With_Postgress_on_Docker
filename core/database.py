# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connection string: adjust user, password, host, port, db name
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/mydatabase"

# Engine: manages connections to the database
engine = create_engine(DATABASE_URL)

# SessionLocal: factory for DB sessions, used in dependency injection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: all models will inherit from this
Base = declarative_base()
