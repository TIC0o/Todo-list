
import pytest
from src.task import Task, Priority, Status
from src.task_manager import TaskManager

@pytest.fixture
def manager():
    return TaskManager()

def test_add_task(manager):
    t = Task(1, "Write tests")
    manager.add_task(t)
    assert len(manager.get_all()) == 1

def test_add_task_duplicate_id(manager):
    t1 = Task(1, "A")
    t2 = Task(1, "B")
    manager.add_task(t1)
    with pytest.raises(ValueError):
        manager.add_task(t2)

def test_get_by_status(manager):
    t1 = Task(1, "Pending")
    t2 = Task(2, "Done", status=Status.COMPLETED)
    manager.add_task(t1)
    manager.add_task(t2)
    result = manager.get_by_status(Status.COMPLETED)
    assert len(result) == 1
    assert result[0].title == "Done"

def test_get_by_status_invalid(manager):
    with pytest.raises(ValueError):
        manager.get_by_status("COMPLETED")  # wrong type

def test_update_task_title_and_status(manager):
    t = Task(1, "Old Task")
    manager.add_task(t)
    updated = manager.update_task(1, title="New Title", status=Status.IN_PROGRESS)
    assert updated.title == "New Title"
    assert updated.status == Status.IN_PROGRESS

def test_update_task_not_found(manager):
    with pytest.raises(ValueError):
        manager.update_task(99, title="X")

def test_update_task_invalid_title(manager):
    t = Task(1, "X")
    manager.add_task(t)
    with pytest.raises(ValueError):
        manager.update_task(1, title="   ")
