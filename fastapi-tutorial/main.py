from fastapi import FastAPI, Path, Query
from typing import Union
from pydantic import BaseModel

from routers import body, cookie, extraDataType, header, responseModel
from routers import body, cookie, extraDataType, header, formField

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

# 쿼리 파라미터는 q가 아닌 alias인 param-query로 전달해야 한다.
# params/123123?q=good -> q is None
# params/123123?param-query=good -> q is good
@app.get("/params/{param_id}")
async def read_items(
    param_id: int = Path(title="The ID of the item to get"),
    q: Union[str, None] = Query(default=None, alias="param-query"),
):
    results = {"param_id": param_id}
    
    if q:
        results.update({"q": q})
    
    print(results)
    
    return results

# 숫자 검증
# gt: greater than
# ge: greate or equal
# lt: less than
# le: less or equal
@app.get("/tests/{test_id}")
async def read_tests(
    *, test_id: int = Path(title="The ID of the item to get", ge=1), q: str
):
    results = {"test_id": test_id}
    if q:
        results.update({"q": q})
    return results

app.include_router(body.router)
app.include_router(extraDataType.router)
app.include_router(cookie.router)
app.include_router(header.router)
app.include_router(responseModel.router)
app.include_router(formField.router)
