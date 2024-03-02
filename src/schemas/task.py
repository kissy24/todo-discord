from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: str | None = Field(None, example="Go to shopping")
    done: bool = Field(False, description="Done flag")

class TaskCreate(BaseModel):
    title: str | None = Field(None, example="Go to shopping")

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
