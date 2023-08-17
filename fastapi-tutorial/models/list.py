from typing import Union
from pydantic import BaseModel

class Lists(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list = []
    test: str