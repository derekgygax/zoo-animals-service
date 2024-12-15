from pydantic import BaseModel
from typing import List

class EnumResponse(BaseModel):
    type: str
    label: str
    values: List[str]
