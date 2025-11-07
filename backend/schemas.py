from pydantic import BaseModel
from datetime import date, datetime

class AsteroidSchema(BaseModel):
    id: int
    name: str
    date: date
    is_hazardous: bool
    diameter_min: float
    diameter_max: float
    magnitude: float
    approach_date: datetime
    miss_distance_km: float

    class Config:
        from_orm = True
