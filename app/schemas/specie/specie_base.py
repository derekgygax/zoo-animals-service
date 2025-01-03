from pydantic import BaseModel, Field
from datetime import date

class SpecieBase(BaseModel):
	name: str = Field(..., max_length=100, description="The name of the specie", title="Specie Name")
	description: str = Field(..., max_length=500, description="A short description about the specie", title="Specie Description")
	
	class Config:
		json_encoders = {date: lambda v: v.isoformat()}
		from_attributes = True
	
