from src.sample import add, minus


def test_add():
    left = 1
    right = 3
    assert add(left, right) == left + right


def test_minus():
    left = 1
    right = 3
    assert minus(left, right) == left - right
