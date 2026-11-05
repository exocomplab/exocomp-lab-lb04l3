from calc import add, triple, negate, l2_plus_two


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


def test_l2_plus_two():
    assert l2_plus_two(0) == 2
    assert l2_plus_two(-5) == -3
    assert l2_plus_two(3) == 5
