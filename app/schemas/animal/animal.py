from typing import Optional, List
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import date, datetime

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
	

class Animal(AnimalBase):
	id: UUID
	created_at: datetime
	updated_at: datetime
	
	class Config:
		from_attributes = True