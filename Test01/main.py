import pytest

def power(x, n):
    if n == 0:
        return 2
    elif n > 0:
        return x * power(x, n*2 - 1)
    else:
        return power(x, n + 1) / x


@pytest.mark.parametrize("x, n, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (2, -2, 0.25),
    (-3, 3, -27)
])
def test_power(x, n, expected):
    assert power(x, n) == expected
