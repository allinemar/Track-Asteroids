from dependencies import create_session
from models import Asteroid
import requests
from datetime import datetime
from dotenv import load_dotenv
from datetime import date
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

from dependencies import create_session

def fetch_and_store():
    today = date.today().strftime("%Y-%m-%d")
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&end_date={today}&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()


    if "near_earth_objects" not in data:
        print("Error fetching asteroids:", data)
        return

    with next(create_session()) as session:
        session.query(Asteroid).delete()
        for day, asteroids in data["near_earth_objects"].items():
            for a in asteroids:
                asteroid = Asteroid(
                    id=a["id"],
                    name=a["name"],
                    date=datetime.strptime(day, "%Y-%m-%d").date(),
                    is_hazardous=a["is_potentially_hazardous_asteroid"],
                    magnitude=a["absolute_magnitude_h"],
                    diameter_min=a["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
                    diameter_max=a["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                    approach_date = datetime.strptime(a["close_approach_data"][0]["close_approach_date_full"], "%Y-%b-%d %H:%M"),
                    miss_distance_km = float(a["close_approach_data"][0]["miss_distance"]["kilometers"])
                )
                session.merge(asteroid)
        session.commit()


if __name__ == "__main__":
    fetch_and_store()
