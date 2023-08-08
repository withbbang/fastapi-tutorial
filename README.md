# 로컬 라이브 서버 시작

> uvicorn main:app --reload
>
> > uvicorn main:app 명령은 다음을 의미<br>
> > main: 파일 main.py (파이썬 "모듈").<br>
> > app: main.py 내부의 app = FastAPI() 줄에서 생성한 오브젝트.<br>
> > --reload: 코드 변경 후 서버 재시작. (개발에만 사용)<br>
