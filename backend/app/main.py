from fastapi import FastAPI
from .database import engine
from .model import Base
from .endpoints import reservations


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(reservations.router)