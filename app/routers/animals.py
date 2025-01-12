from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# database
from app.database import get_db

# services
from app.services.animals import (
	get_all_animals,
	get_all_animal_ids, 
	add_animal as add_animal_service, 
	get_animal_base_by_id as get_animal_base_by_id_service, 
	update_animal as update_animal_service
)

# schemas
from app.schemas.animal.animal import Animal
from app.schemas.animal.animal_base import AnimalBase
from app.schemas.animal.animal_identifier import AnimalIdentifier

# tags Explanation:
# The tags parameter is used in FastAPI to group endpoints in the automatically generated API documentation (Swagger UI and ReDoc).

router = APIRouter(prefix="/api/v1/animals")

@router.get("/", tags=["animals"], response_model=List[Animal])
async def get_animals(db: Session = Depends(get_db)):
	return get_all_animals(db=db)

@router.get("/ids", tags=["animals"], response_model=List[AnimalIdentifier])
async def get_animals(db: Session = Depends(get_db)):
	return get_all_animal_ids(db=db)

@router.get("/{animal_id}", tags=["animals"], response_model=AnimalBase)
async def get_animal_base_by_id(animal_id: UUID, db: Session = Depends(get_db)):
	return get_animal_base_by_id_service(db=db, animal_id=animal_id)

# TODO with auth
# @router.post("/", tags=["animal"], status_code=status.HTTP_201_CREATED response_model=None, dependencies=[Depends(check_role([ROLE.ADMIN]))])
@router.post("/", tags=["animal"], status_code=status.HTTP_201_CREATED, response_model=None)
async def add_animal(
	animal: AnimalBase,
	# current_user: JWT = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	add_animal_service(db = db, animal = animal)
	return

@router.put("/{animal_id}", tags=["animal"], status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def update_animal(
	animal_id: UUID,
	animal: AnimalBase,
	# current_user: JWT = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	update_animal_service(db=db, animal_id=animal_id, animal=animal)
	return