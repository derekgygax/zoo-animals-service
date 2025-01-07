from pydantic import BaseModel, Field
from datetime import date


# TODO specie base should be specie_description
# TODO NOT HAVE THE NAME!!!!! that is the primary key!!
class SpecieBase(BaseModel):
	specie: str = Field(..., max_length=100, description="The name of the specie", title="Specie")
	description: str = Field(..., max_length=500, description="A short description about the specie", title="Specie Description")
	
	class Config:
		json_encoders = {date: lambda v: v.isoformat()}
		from_attributes = True
	
