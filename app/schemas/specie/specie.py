from datetime import datetime

# schema
from app.schemas.specie.specie_base import SpecieBase


class Specie(SpecieBase):
	created_at: datetime
	updated_at: datetime
	
	class Config:
		from_attributes = True