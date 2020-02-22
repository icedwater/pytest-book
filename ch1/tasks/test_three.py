"""
Test the Task data type.
"""

from collections import namedtuple

Task = namedtuple("Task", ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    """
    Using no parameters should invoke defaults.
    """
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    """
    Check .field functionality of namedtuple.
    """
    t = Task("make todo list", "meta")
    assert t.summary == "make todo list"
    assert t.owner == "meta"
    assert (t.done, t.id) == (False, None)
