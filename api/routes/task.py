from fastapi import APIRouter, HTTPException
from domain.task import Task
from database.connection import create_local_connection
from infrastructure.task.mongodb import TaskRepositoryMongoDB

task_routes = APIRouter()
mongo_client = create_local_connection()
db = mongo_client["ScalablePath"]
task_collection = db["task"]

@task_routes.post("/task")
async def create_task(task: Task):
    mongo_repository = TaskRepositoryMongoDB(task_collection)
    try:
        new_task = mongo_repository.create(task)
        return {
            "message": "Task created successfully.",
            "task": new_task
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@task_routes.delete("/task")
async def delete_task(task: Task):
    mongo_repository = TaskRepositoryMongoDB(task_collection)
    try:
        task_deleted = mongo_repository.delete(task)
        return {
            "message": "Task deleted successfully.",
            "task": task_deleted
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))