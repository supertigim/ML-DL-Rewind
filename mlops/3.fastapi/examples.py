# -*- coding:utf-8 -*-
from email.policy import default
from time import sleep
from typing import Optional, Dict, List
from uuid import UUID, uuid4

from fastapi import BackgroundTasks, FastAPI, Form, Request, File, UploadFile, APIRouter, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import uvicorn
from pydantic import BaseModel, Field

app = FastAPI()

################################################
#   Background Task 
################################################
class TaskInput(BaseModel):
    id_: UUID = Field(default_factory=uuid4)
    wait_time: int 

task_repo = {}

def cpu_torturing(id_: UUID, wait_time: int):
    sleep(wait_time)
    result = f'task is done after {wait_time}'
    task_repo[id_] = result # 결과를 저장 

# 오래 걸리는 일은 백그라운드에서 돌리고, 결과는 다른 api로 받는다 
@app.post('/task', status_code=202)
async def create_task_in_bg(ti: TaskInput, bgt: BackgroundTasks):
    bgt.add_task(cpu_torturing, id_=ti.id_, wait_time=ti.wait_time)
    return ti.id_

@app.get('/task/{task_id}')
def get_task_result(task_id: int):
    try:
        return task_repo[task_id]
    except KeyError:
        raise None  # 결과가 없을 때 에러 반환

################################################
#   HTTPException
################################################
v_items = {
    1: 'ai',
    2: 'ML',
    3: 'DL'
}

@app.get('/v1/{item_id}')
async def find_by_id(item_id: int):
    try:
        item = v_items[item_id]
    except KeyError:
        raise HTTPException(status_code=404, detail=f'노템 (id: {item_id})')
    return item 


################################################
#   API Router 사용법 - uvicon with reload와 하면 안된다.. 왜??
################################################
order_router = APIRouter(prefix='/orders')
app.include_router(order_router)

@order_router.get('/', tags=['orders'])
def read_orders():
    return [{'order':'Taco'}, {'order':'Burrito'}]


################################################
#   이벤트 처리
################################################
items = {}

@app.on_event('startup')
def startup_event():
    print('Start up event')
    items['foo'] = {'name': 'fighters'}
    items['bar'] = {'name': 'tenders'}

@app.on_event('shutdown')
def shutdown_event():
    print('Shutdown Event!')
    with open('log.txt', mode='a') as log:
        log.write('application shutdown')


################################################
#   파일 처리 - 업로드 / 보여주기 
################################################

@app.post('/files/')
def create_files(files: List[bytes] = File(...)):
    return {'file_size': [len(file) for file in files]}

@app.post('/uploadfiles/')
def create_upload_files(files: List[UploadFile] = File(...)):
    return{'filenames': [file.filename for file in files]}

@app.get('/')
def home():
    content = '''
<body>
    <form action='/files/' enctype='multipart/form-data' method='post'>
    <input name='files' type='file' multiple>
    <input type='submit'>
    </form>
    <form action='/uploadfiles/' enctype='multipart/form-data' method='post'>
    <input name='files' type='file' multiple>
    <input type='submit'>
    </form>
</body>
    '''
    return HTMLResponse(content=content)


################################################
#   일반적인 Get Method
################################################

@app.get('/users/{user_id}')
def get_user(user_id):
    return {'user_id': user_id}

fake_items_db=[
    {'item_name': 'Foo'},
    {'item_name': 'Bar'},
    {'item_name': 'Baz'},
    {'item_name': 'AI'},
    {'item_name': 'ML'},
    {'item_name': 'DL'}
]

# 변수이용: http://localhost:8000/items/?skip=3&limit=6
@app.get('/items/')
def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip+ limit]

# query 사용 하기 
@app.get('/item/{item_id}')
def read_item(item_id: str, q: Optional[str] = None) -> Dict:
    if q:
        # http://localhost:8000/item/5?q=ai_is_cool
        return {'item_id': item_id, 'q':q}
    
    return {'item_id': item_id}


################################################
#   Pydantic 클래스 활용 방법
################################################

class ItemIn(BaseModel):
    name: str
    description: Optional[str] = None
    price: float 
    tax: Optional[float] = None

class ItemOut(BaseModel):
    name: str
    price: float 
    tax: Optional[float] = None

@app.post('/item/', response_model=ItemOut)
def create_item(item: ItemIn):
    return item 


################################################
#   기본적인 로그인 처리방법 & Jinja 템플릿 활용 법
################################################
templates = Jinja2Templates('./static/')

@app.get('/login/')
def get_login_form(request: Request):
    return templates.TemplateResponse('login_form.html', context={'request': request})

@app.post('/login/')
def login(username: str=Form(...), password: str=Form(...)):
    return {'username': username}


################################################

def main():
    app.include_router(order_router)

    # hot reload 를 해주고 싶으면 첫번째 인자를 '파일명:app' 형식으로 해주고 reload=True
    #uvicorn.run(app, host='0.0.0.0', port=8000)
    uvicorn.run('examples:app', host='0.0.0.0', port=8000, reload=True, workers=2)

if __name__ == '__main__':
    main()