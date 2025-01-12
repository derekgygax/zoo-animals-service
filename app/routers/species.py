from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# database
from app.database import get_db

# services
from app.services.species import (
    get_all_species,
    add_specie as add_specie_service,
    update_specie as update_specie_service,
    get_all_species_base,
    get_specie_ids as get_specie_ids_service,
)

# schemas
from app.schemas.specie.specie_base import SpecieBase
from app.schemas.specie.specie import Specie
from app.schemas.animal.animal_base import AnimalBase
from app.schemas.animal.animal_identifier import AnimalIdentifier

# tags Explanation:
# The tags parameter is used in FastAPI to group endpoints in the automatically generated API documentation (Swagger UI and ReDoc).

router = APIRouter(prefix="/api/v1/species")

@router.get("/", tags=["species"], response_model=List[Specie])
async def get_species(db: Session = Depends(get_db)):
	return get_all_species(db=db)

@router.get("/ids", tags=["species"], response_model=List[str])
async def get_specie_keys(db:Session = Depends(get_db)):
	return get_specie_ids_service(db=db)

@router.get("/base", tags=["species"], response_model=List[SpecieBase])
async def get_species_base(db: Session = Depends(get_db)):
	return get_all_species_base(db=db)


# TODO with auth
# @router.post("/", tags=["animal"], status_code=status.HTTP_201_CREATED response_model=None, dependencies=[Depends(check_role([ROLE.ADMIN]))])
@router.post("/", tags=["species"], status_code=status.HTTP_201_CREATED, response_model=None)
async def add_specie(
	specie: SpecieBase,
	# current_user: JWT = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	add_specie_service(db = db, specie = specie)
	return

@router.post("/{specie_id}", tags=["animal"], status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def update_animal(
	specie_id: str,
	specie: Specie,
	# current_user: JWT = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	update_specie_service(db=db, specie_id=specie_id, specie=specie)
	return