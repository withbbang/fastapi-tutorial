from typing import Union
from pydantic import BaseModel, Field

# Field로 유효성 체크
class FieldTest(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=3, description="The price must be greater than zero")
    tax: Union[float, None] = None