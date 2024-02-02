from domain.task import Task
from infrastructure.task.repository import TaskRepository
from pymongo.collection import Collection
from datetime import datetime
from bson import ObjectId

class TaskRepositoryMongoDB(TaskRepository):

    def __init__(self, collection: Collection) -> None:
        self.collection = collection
        super().__init__()

    def create(self, task: Task) -> Task:
        task_id = None

        task.created_at = datetime.now().timestamp()
        
        dict_task = dict(task)
        del dict_task["id"]

        try:
            task_id = self.collection.insert_one(dict_task).inserted_id
        except Exception as e:
            raise ValueError("Error inserting task. " + str(e))

        return Task(
            id=str(task_id),
            name=task.name,
            description=task.description,
            created_at=task.created_at,
            user_id=task.user_id
        )
    
    def delete(self, task: Task) -> Task:
        try:
            self.collection.delete_one({"_id": ObjectId(task._id)})
        except Exception as e:
            raise ValueError("Error deleting the task. " + str(e))
        
        return task