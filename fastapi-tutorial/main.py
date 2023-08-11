from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}

# /items/foo?q=good&short=True
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    print(item) # {'item_id': 'foo'}
    print(q) # good
    print(short) #True

    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )

    print(item) # {'item_id': 'foo', 'q': 'good'}
    return item

# /users/bread/items/macho?short=1
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}

    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# 필수 쿼리 파라미터
# /items/foo-item -> 404
# /items/foo-item?needy=sooooneedy -> 200
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str): # needy의 타입을 선언할 경우, str 타입의 needy란 변수는 꼭 있어야한다.
    item = {"item_id": item_id, "needy": needy}
    return item


@app.post("/datas/{item_id}")
async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    print(result)
    if q:
        result.update({"q": q})
    return result