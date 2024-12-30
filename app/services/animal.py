from typing import List
from sqlalchemy.orm import Session

# models
from app.models.animal import Animal

# schemas
from app.schemas.animal.animal import AnimalBase

def get_all_animals(db: Session) -> List[Animal]:
    return db.query(Animal).all()

def add_animal(db: Session, animal: AnimalBase) -> None:
    db_animal = Animal(**animal.model_dump())
    # Print the stuff in db_post
    # print(vars(db_animal))
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return