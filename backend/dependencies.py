from fastapi import Depends, HTTPException
from models import Asteroid, db
from sqlalchemy.orm import sessionmaker, Session

def create_session():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()

