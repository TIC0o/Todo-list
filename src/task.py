
from enum import Enum
from dataclasses import dataclass

class Priority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Status(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

@dataclass
class Task:
    id: int
    title: str
    priority: Priority = Priority.MEDIUM
    status: Status = Status.PENDING

    def update_status(self, new_status: Status) -> None:
        if not isinstance(new_status, Status):
            raise ValueError("Invalid status type")
        self.status = new_status

    def update_priority(self, new_priority: Priority) -> None:
        if not isinstance(new_priority, Priority):
            raise ValueError("Invalid priority type")
        self.priority = new_priority
