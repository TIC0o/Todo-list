
from typing import List, Optional
from src.task import Task, Priority, Status

class TaskManager:
    def __init__(self) -> None:
        self._tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        if not isinstance(task, Task):
            raise ValueError("Invalid task object")
        if any(t.id == task.id for t in self._tasks):
            raise ValueError("Task id already exists")
        self._tasks.append(task)

    def get_all(self) -> List[Task]:
        return list(self._tasks)

    def get_by_status(self, status: Status) -> List[Task]:
        if not isinstance(status, Status):
            raise ValueError("Invalid status type")
        return [t for t in self._tasks if t.status == status]

    def update_task(self, task_id: int, *, title: Optional[str] = None,
                    priority: Optional[Priority] = None, status: Optional[Status] = None) -> Task:
        task = next((t for t in self._tasks if t.id == task_id), None)
        if task is None:
            raise ValueError("Task not found")
        if title is not None:
            if not isinstance(title, str) or not title.strip():
                raise ValueError("Invalid title")
            task.title = title.strip()
        if priority is not None:
            task.update_priority(priority)
        if status is not None:
            task.update_status(status)
        return task
