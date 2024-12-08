from typing import List
from sqlalchemy.orm import Session

from app.models.animal import Animal

def get_all_animals(db: Session) -> List[Animal]:
    return db.query(Animal).all()