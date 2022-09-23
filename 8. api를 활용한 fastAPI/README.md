# 8. fastAPI

> 참고 url : https://fastapi.tiangolo.com/ko/  
> 참고 강의 : https://www.youtube.com/watch?v=ktGVFmfGiGM&list=PLKy1qiqTzJteucwpykHuZyCh-HqeZXIG4&index=18  
> 참고 github : https://github.com/riseryan89/notification-api

1. 환경 세팅
    
    ```bash
    $ pip install fastapi
    $ pip install uvicorn
    ```

2. 간단한 예제
    
    ```python
    from fastapi import FastAPI
    
    app = FastAPI()
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: str = None):
        return {"item_id": item_id, "q": q}
    ```

3. 실행
        
   ```bash
        $ uvicorn main:app --reload
   ```

4. 확인  
   http://127.0.0.1:8000/docs 

5. project 실행
    ```bash
    virtualenv venv
   source venv/bin/activate
   pip install -r requirements.txt
    ```


