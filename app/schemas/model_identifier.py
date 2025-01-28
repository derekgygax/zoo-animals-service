

from pydantic import BaseModel, Field


class ModelIdentifier(BaseModel):
    id: str = Field(..., title = "ID", description = "Unique identifier of that instance of the Model as a string")
    label: str = Field(..., title = "Label", description = "A human readable label to identify that instance of the Model")