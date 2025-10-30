
import pytest
from src.task import Task, Priority, Status

def test_create_task_defaults():
    task = Task(1, "Test Task")
    assert task.title == "Test Task"
    assert task.priority == Priority.MEDIUM
    assert task.status == Status.PENDING

def test_update_status_valid():
    task = Task(1, "Demo")
    task.update_status(Status.COMPLETED)
    assert task.status == Status.COMPLETED

def test_update_status_invalid():
    task = Task(1, "Invalid")
    with pytest.raises(ValueError):
        task.update_status("Done")  # wrong type

def test_update_priority_valid():
    task = Task(2, "Prio")
    task.update_priority(Priority.HIGH)
    assert task.priority == Priority.HIGH

def test_update_priority_invalid():
    task = Task(2, "Prio")
    with pytest.raises(ValueError):
        task.update_priority("HIGH")  # wrong type
