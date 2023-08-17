from typing import Set, Union
from pydantic import BaseModel

class Sets(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()