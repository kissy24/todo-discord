from fastapi import APIRouter

router = APIRouter()


@router.put("/tasks/{task_id}/done")
async def complete_task():
    pass


@router.delete("/tasks/{task_id}/done")
async def cancel_completed_task():
    pass
