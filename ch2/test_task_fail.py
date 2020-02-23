"""
Use the Task type to show test failures.
"""

from tasks import Task

def test_task_equality():
    """
    Different tasks should not be equal.
    """
    t1 = Task("sit there", "sitter")
    t2 = Task("do something", "worker")
    assert t1 == t2

def test_dict_equality():
    """
    Different tasks as dict should also not be equal.
    """
    t1_dict = Task("make sandwich", "user")._asdict()
    t2_dict = Task("make sandwich", "sudo")._asdict()
    assert t1_dict == t2_dict
