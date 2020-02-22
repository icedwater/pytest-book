import time

def test_failing():
    time.sleep(0.25)
    assert (1, 2, 3) == (3, 2, 1)
