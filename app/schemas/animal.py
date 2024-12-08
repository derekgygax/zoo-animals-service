from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime

# local
from app.enums.gender import GENDER
from app.enums.health import HEALTH
from app.enums.specie import SPECIE

class AnimalBase(BaseModel):
	name: str
	specie: SPECIE
	dob: date
	gender: GENDER
	health: HEALTH
	acquisition_date: Optional[date] = None
	litter_id: Optional[UUID] = None
	

class Animal(AnimalBase):
	id: UUID
	created_at: datetime
	updated_at: datetime
	
	class Config:
		from_attributes = True