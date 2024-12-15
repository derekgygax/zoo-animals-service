from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# services
from app.services.enums import get_all_animal_enums_response
from app.types.enums import EnumResponse

# tags Explanation:
# The tags parameter is used in FastAPI to group endpoints in the automatically generated API documentation (Swagger UI and ReDoc).

router = APIRouter(prefix="/api/v1/enums")

@router.get("/", tags=["enums"], response_model=str)
async def get_animal_enums():
	return "Get Enums"

@router.get("/animal", tags=["enums"], response_model=List[EnumResponse])
async def get_animal_enums():
	return get_all_animal_enums_response()
