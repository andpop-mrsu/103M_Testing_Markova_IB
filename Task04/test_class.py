import pytest
from triangle_class import Triangle, IncorrectTriangleSides

@pytest.mark.parametrize("a, b, c, expected", [
    (5, 5, 5, "equilateral"),
    (5, 5, 3, "isosceles"),
    (3, 4, 5, "nonequilateral")
])
def test_valid_types(a, b, c, expected):
    tr = Triangle(a, b, c)
    assert tr.triangle_type() == expected

def test_perimeter_calc():
    assert Triangle(10, 10, 10).perimeter() == 30

@pytest.mark.parametrize("a, b, c", [
    (0, 4, 5), (-1, 2, 2), (1, 2, 10), ("3", 4, 5)
])
def test_errors(a, b, c):
    with pytest.raises(IncorrectTriangleSides):
        Triangle(a, b, c)