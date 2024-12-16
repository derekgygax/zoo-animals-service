from app.enums.gender import GENDER
from app.enums.health_type import HEALTH_TYPE
from app.enums.specie import SPECIE

from app.types.metadata import Metadata
from app.enums.field_type import FORM_FIELD_TYPE

ANIMAL_METADATA = [
    Metadata(
        name="name",
        type=FORM_FIELD_TYPE.TEXT,
        label="Name",
        maxLength=100,
        required=True
    ),
    Metadata(
        name="specie",
        type=FORM_FIELD_TYPE.SELECTOR,
        label="Specie",
        values=[item.value for item in SPECIE],
        required=True
    ),
    Metadata(
        name="gender",
        type=FORM_FIELD_TYPE.SELECTOR,
        label="Gender",
        values=[item.value for item in GENDER],
        required=True
    ),
    Metadata(
        name="health",
        type=FORM_FIELD_TYPE.SELECTOR,
        label="Health Type",
        values=[item.value for item in HEALTH_TYPE],
        required=True
    ),
    Metadata(
        name="dob",
        type=FORM_FIELD_TYPE.DATE,
        label="Date of Birth",
        required=True
    ),
    Metadata(
        name="acquisition_date",
        type=FORM_FIELD_TYPE.DATE,
        label="Acquisition Date",
        required=True
    )
]
