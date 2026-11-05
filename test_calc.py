from calc import add, triple, negate, l2_plus_two, l3_delivery_plus_three, l3_checks_plus_four, l3_local_plus_five


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


def test_l3_delivery_plus_three():
    assert l3_delivery_plus_three(1) == 4
    assert l3_delivery_plus_three(0) == 3
    assert l3_delivery_plus_three(-3) == 0


def test_l3_checks_plus_four():
    assert l3_checks_plus_four(0) == 4
    assert l3_checks_plus_four(1) == 5
    assert l3_checks_plus_four(-4) == 0


def test_l3_local_plus_five():
    assert l3_local_plus_five(0) == 5
    assert l3_local_plus_five(3) == 8
    assert l3_local_plus_five(-5) == 0
