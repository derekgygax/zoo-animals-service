from uuid import UUID
from pydantic import BaseModel, Field

# enums
from app.enums.specie import SPECIE

class AnimalIdentifier(BaseModel):
    id: UUID = Field(..., description="The unique identifier for the animal", title="ID")
    name: str = Field(..., max_length=100, description="The name of the animal", title="Name")
    specie_name: str = Field(..., max_length=100, description="The name of the specie of the animal", title="Specie Name")

    class Config:
        json_encoders = {UUID: str}
        from_attributes = True
