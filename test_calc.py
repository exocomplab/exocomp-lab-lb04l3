from calc import add, triple


def test_add():
    assert add(2, 3) == 5


def test_triple():
    assert triple(3) == 9
    assert triple(0) == 0
    assert triple(-2) == -6
