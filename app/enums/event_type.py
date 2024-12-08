from enum import Enum

class EVENT_TYPE(str, Enum):
    BIRTH = "BIRTH"
    TRANSFER = "TRANSFER"
    DEATH = "DEATH"
    MEDICAL = "MEDICAL"
    BREEDING = "BREEDING"
    FEEDING = "FEEDING"
    GENERAL_CARE = "GENERAL_CARE"
