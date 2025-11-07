from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, Date, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import date, datetime
from dotenv import load_dotenv
import os

load_dotenv()

db = create_engine(os.getenv("DB"))
Base = declarative_base()

class Asteroid(Base):
    __tablename__="asteroids"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    date = Column("date", Date)
    is_hazardous = Column("is_hazardous", Boolean)
    diameter_min = Column("diameter_min", Float)
    diameter_max = Column("diameter_max", Float)
    magnitude = Column("magnitude", Float)
    approach_date = Column("approach_date", DateTime)
    miss_distance_km = Column("miss_distance_km", Float)

Base.metadata.create_all(db)







