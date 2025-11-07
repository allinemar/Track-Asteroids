from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dependencies import create_session
from models import Asteroid
from typing import List
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fetch_and_store import fetch_and_store
import os
from fastapi.staticfiles import StaticFiles
from schemas import AsteroidSchema

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

last_update = None

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/frontend", StaticFiles(directory="../frontend", html=True), name="frontend")

@app.get("/asteroids", response_model=List[AsteroidSchema])
def get_asteroids(session: Session = Depends(create_session)):
    global last_update
    now = datetime.now()
    print(last_update)
    # Only update if more than 1 hour passed since last update
    if not last_update or (now - last_update) > timedelta(hours=1):
        fetch_and_store()
        last_update = now
    return session.query(Asteroid).all()
