from abc import ABC, abstractmethod
from domain.task import Task

class TaskRepository:
    @abstractmethod
    def create(self, task: Task) -> Task:
        pass

    @abstractmethod
    def delete(self, task: Task) -> Task:
        pass