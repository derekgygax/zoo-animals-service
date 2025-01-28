from sqlalchemy.orm import load_only
from typing import List
# from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

# models
from app.models.animal import Animal
from app.models.specie import Specie

# schemas
from app.schemas.animal.animal import AnimalBase
from app.schemas.animal.animal_identifier import AnimalIdentifier
from app.schemas.model_identifier import ModelIdentifier
from app.schemas.specie.specie_base import SpecieBase

# TODO CANNOT CHANGE THE specie name because its the primary key
# TODO add a UUID if you think you need to

# Check if a specie exists
def _validate_specie_exists(db: Session, specie_id: str) -> None:
    if not db.query(Specie).filter_by(id=specie_id).first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Specie '{specie_id}' does not exist."
        )
    
def get_all_species(db: Session) -> List[Specie]:
    return db.query(Specie).all()

def get_specie_ids(db: Session) -> List[str]:
    species =  db.query(Specie).options(
        load_only(
            Specie.id
        )
    ).all()
    return [
        specie.id for specie in species
    ]

def get_specie_identifiers(db: Session) -> List[ModelIdentifier]:
    specie_ids = get_specie_ids(db=db)
    return [
        ModelIdentifier(id=str(id), label=str(id)) for id in specie_ids
    ]

def get_all_species_base(db: Session) -> List[SpecieBase]:
    species = db.query(Specie).options(
        load_only(
            Specie.id,
            Specie.description
        )
    ).all()
    return [
        SpecieBase.model_validate(specie) for specie in species
    ]

def get_specie_base_by_id(db: Session, specie_id: str) -> SpecieBase:
    specie = db.query(Specie).filter(Specie.id == specie_id).options(
        load_only(
            Specie.id,
            Specie.description
        )
    ).first()

    if not specie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Specie not found"
        )
    return SpecieBase.model_validate(specie)

def add_specie(db: Session, specie: SpecieBase) -> None:
    db_specie = Specie(**specie.model_dump())
    # Print the stuff in db_post
    # print(vars(db_specie))
    try:
        db.add(db_specie)
        db.commit()
        db.refresh(db_specie)
    except IntegrityError:
        db.rollback()  # Rollback the transaction in case of an error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Specie with ID '{db_specie.id}' already exists."
        )
    return

# TODO specie base should be specie_description
def update_specie(db: Session, specie_id: str, specie: SpecieBase) -> None:

    db_specie = db.query(Specie).filter(Specie.id == specie_id).first()
    if db_specie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Specie not found"
        )

    # Update fields
    db_specie.description = specie.description

    db.commit()
    db.refresh(db_specie)
    return