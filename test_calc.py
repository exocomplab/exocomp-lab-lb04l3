from calc import add, triple, negate


def test_add():
    assert add(2, 3) == 5


def test_triple():
    assert triple(3) == 9
    assert triple(0) == 0
    assert triple(-2) == -6


def test_negate():
    assert negate(5) == -5
    assert negate(-3) == 3
    assert negate(0) == 0
