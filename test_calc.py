from calc import add, triple


def test_add():
    assert add(2, 3) == 5

def test_triple_positive_returns_value_times_three():
    assert triple(4) == 12

def test_triple_zero_returns_zero():
    assert triple(0) == 0

def test_triple_negative_returns_value_times_three():
    assert triple(-3) == -9
