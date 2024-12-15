from typing import List
from sqlalchemy.orm import Session

# enums
from app.enums.animal_enums import ANIMAL_ENUM

# types
from app.types.enums import EnumResponse


def get_all_animal_enums_response():
    return [
        EnumResponse(
            type=item.type,
            label=item.label,
            values=item.values
        )
        for item in ANIMAL_ENUM
    ]