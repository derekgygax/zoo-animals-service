from uuid import UUID
from datetime import datetime

# schema
from app.schemas.animal.animal_base import AnimalBase

class Animal(AnimalBase):
	id: UUID
	created_at: datetime
	updated_at: datetime
	
	class Config:
		from_attributes = True