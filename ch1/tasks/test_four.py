"""
Test the Task data type.
"""
import pytest   # for using named markers
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

@pytest.mark.run_this
def test_replace():
    """
    replace() should change passed-in fields.
    """
    print("These strings only print() with -s switch.")
    t_before = Task("finish book", "reader", False)
    print("Defined basis object for change.")
    t_after = t_before._replace(id=10, done=True)
    print("Changed fields in t_before.")
    expected = Task("finish book", "reader", True, 10)
    assert t_after == expected
