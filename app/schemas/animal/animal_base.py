from pydantic import BaseModel, Field
from datetime import date

# local
from app.enums.gender import GENDER
from app.enums.health_type import HEALTH_TYPE
from app.enums.specie import SPECIE


class AnimalBase(BaseModel):
	name: str = Field(..., max_length=100, description="The name of the animal", title="Name")
	specie: SPECIE = Field(..., title="Specie")
	gender: GENDER = Field(..., title="Gender")
	health: HEALTH_TYPE = Field(..., title="Health")
	dob: date = Field(..., title="DOB")
	acquisition_date: date = Field(..., title="Aquisition Date")
	
	class Config:
		json_encoders = {date: lambda v: v.isoformat()}
		from_attributes = True
	
