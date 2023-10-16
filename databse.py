from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///database.db'

engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():  
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()