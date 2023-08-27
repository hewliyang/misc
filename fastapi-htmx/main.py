import requests
import random

from typing import Optional
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
def index(request: Request, hx_request: Optional[str] = Header(None)):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

@app.get("/randomtodo", response_class=HTMLResponse)
def todos(request: Request):
    todo = requests.get(f"https://jsonplaceholder.typicode.com/todos/{random.randint(1,200)}").json()
    context = {"request": request, "todo": todo}
    return templates.TemplateResponse("partials/table.html", context)