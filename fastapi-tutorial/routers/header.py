from typing import List, Union
from fastapi import APIRouter, Header
from typing_extensions import Annotated

router = APIRouter(
    prefix="/router",
)

# fast api에서는 헤더의 프로퍼티를 대소문자 구분없이 이해한다.
# fast api에서는 하이픈(-)이 있는 프로퍼티 키값을 자동으로 언더스코어(_)로 상호 변환시킨다
# 변환 시킬 필요가 없을 경우 Header(convert_underscores=False) 설정
@router.get("/header")
async def header(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}

# 다중 값을 갖는 헤더
@router.get("/header/list")
async def read_items(accept_language: Union[List[str], None] = Header(default=None)):
    return {"Accept-Language": accept_language}