from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# database
from app.database import get_db

# types
from app.types.metadata import Metadata

# services
from app.services.animal import get_all_animals, get_metadata as get_metadata_service

# schemas
from app.schemas.animal.animal import Animal

# tags Explanation:
# The tags parameter is used in FastAPI to group endpoints in the automatically generated API documentation (Swagger UI and ReDoc).

router = APIRouter(prefix="/api/v1/animals")

@router.get("/", tags=["animals"], response_model=List[Animal])
async def get_animals(db: Session = Depends(get_db)):
	return get_all_animals(db=db)


@router.get("/metadata", tags=["animals", "metadata"], response_model=List[Metadata])
async def get_metadata():
	return get_metadata_service()
