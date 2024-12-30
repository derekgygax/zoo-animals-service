from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# database
from app.database import get_db

# services
from app.services.animal import get_all_animals, add_animal as add_animal_service

# schemas
from app.schemas.animal.animal import Animal, AnimalBase

# tags Explanation:
# The tags parameter is used in FastAPI to group endpoints in the automatically generated API documentation (Swagger UI and ReDoc).

router = APIRouter(prefix="/api/v1/animals")

@router.get("/", tags=["animals"], response_model=List[Animal])
async def get_animals(db: Session = Depends(get_db)):
	return get_all_animals(db=db)

# TODO with auth
# @router.post("/", tags=["animal"], status_code=status.HTTP_201_CREATED response_model=None, dependencies=[Depends(check_role([ROLE.ADMIN]))])
@router.post("/", tags=["animal"], status_code=status.HTTP_201_CREATED, response_model=None)
async def add_animal(
	animal: AnimalBase,
	# current_user: JWT = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	print(animal)
	add_animal_service(db = db, animal = animal)
	return
