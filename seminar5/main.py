from fastapi import FastAPI, Request
import logging
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

FORMAT = '{levelname:<8} - {asctime} - >>> {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="./DZ_Flask/seminar5/templates")


class Task(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[bool] = False


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    logger.info('Отработал GET запрос(Главная страница).')
    return templates.TemplateResponse("item.html", {"request": request})


@app.get('/tasks/')
async def all_tasks():
    logger.info('Отработал GET ')
    return {'Конечные точки по условиям задачи'}


@app.get('/tasks/{id_}')
async def returns_task(id_: int):
    logger.info(f'Отработал GET запрос с id = {id_}).')
    return {f'GET_task = {id_}'}


@app.post("/tasks/")
async def create_task(task: Task):
    logger.info('Отработал POST запрос(добавил новую задачу).')
    return {"POST_new_task": task}


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    logger.info(f'Отработал PUT с id = {task_id}).')
    return {"PUT_task_id": task_id, "task": task}


@app.delete('/tasks/{task_id}')
async def delete_item(task_id: int):
    logger.info(f'Отработал DELETE  с id = {task_id}).')
    return {'DELETE_task_id': task_id}



