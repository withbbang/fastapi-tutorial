from typing import List
from fastapi import APIRouter, File, UploadFile
from typing_extensions import Annotated

router = APIRouter(
    prefix="/router",
)

# 파일 관련한 클라이언트 요청은 form-data 형식이어야 한다.
# x-www-form-urlencoded과는 구분해야함
@router.post("/file")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}
@router.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    # contents = await file.read()
    # print(contents)
    return {"filename": file.filename}


# UploadFile이 bytes보다 좋은 점
# https://fastapi.tiangolo.com/ko/tutorial/request-files/#file-uploadfile


# 다중 파일 api
@router.post("/files")
async def create_files(files: List[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}
@router.post("/uploadfiles")
async def create_upload_files(files: List[UploadFile]):
    return {"filenames": [file.filename for file in files]}