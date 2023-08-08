from fastapi import FastAPI
from typing import Union

app = FastAPI()


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