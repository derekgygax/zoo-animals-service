from pydantic import BaseModel
from typing import List, Optional

class Metadata(BaseModel):
    name: str
    type: str
    label: str
    values: Optional[List[str]] = None
    maxLength: Optional[int] = None
    required: bool
