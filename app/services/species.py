from sqlalchemy.orm import load_only
from typing import List
# from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

# models
from app.models.animal import Animal
from app.models.specie import Specie

# schemas
from app.schemas.animal.animal import AnimalBase
from app.schemas.animal.animal_identifier import AnimalIdentifier
from app.schemas.specie.specie_base import SpecieBase

# TODO CANNOT CHANGE THE specie name because its the primary key
# TODO add a UUID if you think you need to

# Check if a specie exists
# def _validate_specie_exists(db: Session, specie_name: str) -> None:
#     if not db.query(Specie).filter_by(name=specie_name).first():
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Specie '{specie_name}' does not exist."
#         )

def get_all_species(db: Session) -> List[Specie]:
    return db.query(Specie).all()

def get_all_species_base(db: Session) -> List[SpecieBase]:
    species = db.query(Specie).options(
        load_only(
            Specie.specie,
            Specie.description
        )
    ).all()
    return [
        SpecieBase.model_validate(specie) for specie in species
    ]

def add_specie(db: Session, specie: SpecieBase) -> None:
    db_specie = Specie(**specie.model_dump())
    # Print the stuff in db_post
    # print(vars(db_specie))
    db.add(db_specie)
    db.commit()
    db.refresh(db_specie)
    return

# TODO specie base should be specie_description
def update_specie(db: Session, specie_name: str, specie: SpecieBase) -> None:

    db_specie = db.query(Specie).filter(Specie.name == specie_name).first()
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