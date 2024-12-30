from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime

# local
from app.enums.gender import GENDER
from app.enums.health_type import HEALTH_TYPE
from app.enums.specie import SPECIE

class MedicalRecordBase(BaseModel):
	occurred_at: date
	description: str
	

class MedicalRecord(MedicalRecordBase):
	id: UUID
	animal_id: UUID
	vet_id: UUID
	created_at: datetime
	updated_at: datetime
	
	class Config:
		from_attributes = True