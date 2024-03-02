from fastapi import FastAPI

from src.routers import todo, done

app = FastAPI()
app.include_router(todo.router)
app.include_router(done.router)
