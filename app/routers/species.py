from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# database
from app.database import get_db

# services
from app.schemas.model_identifier import ModelIdentifier
from app.services import species_service

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
	return species_service.get_all_species(db=db)

@router.get("/ids", tags=["species"], response_model=List[str])
async def get_specie_keys(db:Session = Depends(get_db)):
	return species_service.get_specie_ids(db=db)

@router.get("/identifiers", tags=["species"], response_model=List[ModelIdentifier])
async def get_specie_identifiers(db:Session = Depends(get_db)):
	return species_service.get_specie_identifiers(db=db)

@router.get("/bases", tags=["species"], response_model=List[SpecieBase])
async def get_species_bases(db: Session = Depends(get_db)):
	return species_service.get_all_species_base(db=db)

@router.get("/{specie_id}/base", tags=["sepcie"], response_model=SpecieBase)
async def get_species_base(
	specie_id: str,
	db: Session = Depends(get_db)
):
	return species_service.get_specie_base_by_id(db=db, specie_id=specie_id)

# TODO with auth
# @router.post("/", tags=["animal"], status_code=status.HTTP_201_CREATED response_model=None, dependencies=[Depends(check_role([ROLE.ADMIN]))])
@router.post("/", tags=["species"], status_code=status.HTTP_201_CREATED, response_model=None)
async def add_specie(
	specie: SpecieBase,
	# current_user: JWT = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	species_service.add_specie(db = db, specie = specie)
	return

@router.put("/{specie_id}", tags=["animal"], status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def update_specie(
	specie_id: str,
	specie: SpecieBase,
	# current_user: JWT = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	print("YA")
	species_service.update_specie(db=db, specie_id=specie_id, specie=specie)
	return