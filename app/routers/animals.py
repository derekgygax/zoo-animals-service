from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# local
from app.schemas.animal import Animal
from app.database import get_db
from app.services.animal import get_all_animals


router = APIRouter(prefix="/api/v1/animals")

@router.get("/", response_model=List[Animal])
async def get_animals(db: Session = Depends(get_db)):
	return get_all_animals(db=db)