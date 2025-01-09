from sqlalchemy.orm import load_only
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

# models
from app.models.animal import Animal
from app.models.specie import Specie

# schemas
from app.schemas.animal.animal import AnimalBase
from app.schemas.animal.animal_identifier import AnimalIdentifier

# services
from app.services.species import _validate_specie_exists

def get_all_animals(db: Session) -> List[Animal]:
    return db.query(Animal).all()

# Get an identification portion for all the animals
def get_all_animal_ids(db: Session) -> List[AnimalIdentifier]:
    animals = db.query(Animal).options(
        load_only(
            Animal.id,
            Animal.name,
            Animal.specie
        )
    ).all()
    return [
        AnimalIdentifier.model_validate(animal) for animal in animals
    ]

# Get the base information for an animal based on the id
def get_animal_base_by_id(db: Session, animalId: UUID) -> AnimalBase:
    animal = db.query(Animal).filter(Animal.id == animalId).options(
        load_only(
            Animal.name,
            Animal.specie,
            Animal.gender,
            Animal.health,
            Animal.dob,
            Animal.acquisition_date
        )
    ).first()

    if not animal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Animal not found"
        )
    
    return AnimalBase.model_validate(animal)

def add_animal(db: Session, animal: AnimalBase) -> None:
    # Check if the specie exists
    _validate_specie_exists(db, animal.specie)
    
    db_animal = Animal(**animal.model_dump())
    # Print the stuff in db_post
    # print(vars(db_animal))
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return

def update_animal(db: Session, animalId: UUID, animal: AnimalBase) -> None:
    # Check if the specie exists
    _validate_specie_exists(db, animal.specie)

    db_animal = db.query(Animal).filter(Animal.id == animalId).first()
    if db_animal is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Animal not found"
        )

    # Update fields
    db_animal.name = animal.name
    db_animal.specie = animal.specie
    db_animal.gender = animal.gender
    db_animal.health = animal.health
    db_animal.dob = animal.dob
    db_animal.acquisition_date = animal.acquisition_date

    db.commit()
    db.refresh(db_animal)
    return