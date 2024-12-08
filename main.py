from fastapi import FastAPI
from dotenv import load_dotenv

# DB models
from app.models.animal import Animal
from app.models.event import Event
from app.models.medical_record import MedicalRecord
from app.models.breeding import Breeding
from app.models.litter import Litter

# Other routes
# from routers.posts import router as posts_router
# from routers.comments import router as comments_router

# Load .env variables in the app
load_dotenv()

app = FastAPI()

# Register the other routers
# app.include_router(posts_router)
# app.include_router(comments_router)

@app.get("/")
def root():
	return "Welcome to the Zoo Animals Service API"