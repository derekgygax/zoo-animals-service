from uuid import UUID
from pydantic import BaseModel, Field

# enums
from app.enums.specie import SPECIE

class AnimalIdentifier(BaseModel):
    id: UUID = Field(..., description="The unique identifier for the animal", title="ID")
    name: str = Field(..., max_length=100, description="The name of the animal", title="Name")
    specie: SPECIE = Field(..., title="Specie")

    class Config:
        json_encoders = {UUID: str}
        from_attributes = True
