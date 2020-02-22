"""
Test the Task data type.
"""

from collections import namedtuple

Task = namedtuple("Task", ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None, None, False, None)

def test_asdict():
    """
    _asdict() should return a dictionary.
    """
    t_task = Task("run tests", "tester", True, 15)
    t_dict = t_task._asdict()
    expected = {
            "summary": "run tests",
            "owner": "tester",
            "done": True,
            "id": 15
    }
    assert t_dict == expected

def test_replace():
    """
    replace() should change passed-in fields.
    """
    t_before = Task("finish book", "reader", False)
    t_after = t_before._replace(id=10, done=True)
    expected = Task("finish book", "reader", True, 10)
    assert t_after == expected
