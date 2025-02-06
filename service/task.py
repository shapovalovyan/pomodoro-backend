from dataclasses import dataclass


from repository import TaskRepository, TaskCache
from schema import TaskSchema


@dataclass
class TaskService:

    task_repository: TaskRepository
    task_cache: TaskCache

    def get_tasks(self) -> list[TaskSchema]:

        cache_tasks = self.task_cache.get_tasks()

        if cache_tasks:
            return cache_tasks
        else:

            tasks = self.task_repository.get_tasks()
            tasks_schema = [TaskSchema.model_validate(task) for task in tasks]

            self.task_cache.set_tasks(tasks_schema)
            return tasks_schema
