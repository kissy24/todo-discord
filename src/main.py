from fastapi import FastAPI
from routers import task

from src.routers import done

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)
