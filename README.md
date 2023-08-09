# 파이썬 가상환경 + 깃 레포지 디렉터리 설정 순서

1. git clone repository (아래랑 같은 뎊스에서 실행)
2. python -m venv repository
3. cd repository
4. pip install -r requirements.txt

<br><br><br>

# 로컬 라이브 서버 시작

- uvicorn main:app --reload

1. uvicorn main:app 명령은 다음을 의미<br>
2. main: 파일 main.py (파이썬 "모듈").<br>
3. app: main.py 내부의 app = FastAPI() 줄에서 생성한 오브젝트.<br>
4. --reload: 코드 변경 후 서버 재시작. (개발에만 사용)<br>
