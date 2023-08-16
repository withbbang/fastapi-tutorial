from fastapi import APIRouter

router = APIRouter(
    prefix="/router",
)


@router.get("/body")
async def body():
    return {"message": "hello"}