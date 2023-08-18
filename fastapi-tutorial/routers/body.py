from typing import Union
from fastapi import APIRouter, Body, Path
from typing_extensions import Annotated
from models.item import Item
from models.user import User, BaseUser, UserIn
from models.field import FieldTest
from models.list import Lists
from models.set import Sets
from models.subModel import SubModel
from models.exampleModel import ExampleModel

router = APIRouter(
    prefix="/router",
)

@router.get("/body")
async def body():
    return {"message": "hello"}

# Annotated 사용시, 검증 조건을 쉽게 추가할 수 있다.
@router.post("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})

    if item:
        results.update({"item": item})

    print(results)

    return results

# multi bodies 요청
# {item: {...}, user: {...}} 형태
@router.post("/multi/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

#multi bodies + single body 요청
# {item: {...}, user: {...}, importance: 3} 형태
@router.post("/single/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[Union[int, None], Body(gt=0)] = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

# Field로 유효성 체크
@router.post("/field/{item_id}")
async def update_item(item_id: int, item: FieldTest):
    results = {"item_id": item_id, "item": item}
    return results

# body 내에 list 형태의 파라미터
@router.post("/lists/{item_id}")
async def update_item(item_id: int, lists: Lists):
    results = {"item_id": item_id, "lists": lists}
    return results

# body 내에 특정 타입의 list 형태 파라미터
@router.post("/sets/{item_id}")
async def update_item(item_id: int, sets: Sets):
    results = {"item_id": item_id, "sets": sets}
    return results

# body 내에 특정 타입의 list 형태 파라미터
@router.post("/sub-model/{item_id}")
async def update_item(item_id: int, subModel: SubModel):
    results = {"item_id": item_id, "subModel": subModel}
    return results

# docs에 모델 예시 표시 기능
@router.post("/example-model/{item_id}")
async def update_item(item_id: int, exampleModel: ExampleModel):
    results = {"item_id": item_id, "exampleModel": exampleModel}
    return results

# UserIn은 BaseUser을 상속받은 모델이므로 BaseUser data + password 까지 포함하고 있다.
# 실제로는 UserIn 인스턴스를 반환하지만 fastapi에서 반환 모델을 인지하여, 필터링 후 return 한다.
@router.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user