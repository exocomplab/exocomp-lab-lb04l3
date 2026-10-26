from calc import add, triple


def test_add():
    assert add(2, 3) == 5

def test_triple():
    assert triple(5) == 15
