from enum import Enum
from typing import List

from app.enums.gender import GENDER
from app.enums.event_type import EVENT_TYPE
from app.enums.health_type import HEALTH_TYPE
from app.enums.specie import SPECIE

class ANIMAL_ENUM(Enum):
    GENDER = ("GENDER", "Gender", [item.value for item in GENDER])
    HEALTH_TYPE = ("HEALTH_TYPE", "Health Type", [item.value for item in HEALTH_TYPE])
    SPECIE = ("SPECIE", "Specie", [item.value for item in SPECIE])
    EVENT_TYPE = ("EVENT_TYPE", "Event Type", [item.value for item in EVENT_TYPE])

    def __init__(self, type_: str, label: str, values: List[str]):
        self.type = type_
        self.label = label
        self.values = values
