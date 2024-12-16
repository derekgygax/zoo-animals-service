from typing import List
from sqlalchemy.orm import Session

from app.models.animal import Animal
from app.schemas.animal.metadata import ANIMAL_METADATA
from app.types.metadata import Metadata

def get_all_animals(db: Session) -> List[Animal]:
    return db.query(Animal).all()


def get_metadata() -> List[Metadata]:
    return ANIMAL_METADATA