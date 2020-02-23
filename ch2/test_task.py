"""
Test the Task data type.
"""
from tasks import Task

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
    print("These strings only print() with -s switch.")
    t_before = Task("finish book", "reader", False)
    print("Defined basis object for change.")
    t_after = t_before._replace(id=10, done=True)
    print("Changed fields in t_before.")
    expected = Task("finish book", "reader", True, 10)
    assert t_after == expected

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
