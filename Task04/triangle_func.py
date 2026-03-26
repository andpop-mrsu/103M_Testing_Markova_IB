from typing import Literal, Union

class IncorrectTriangleSides(Exception):
    """Ошибка при неверных параметрах сторон."""
    pass

def get_triangle_type(side_a: Union[int, float], side_b: Union[int, float], side_c: Union[int, float]) -> Literal["equilateral", "isosceles", "nonequilateral"]:
    """
    Определяет категорию треугольника.
    
    Examples:
    >>> get_triangle_type(7, 7, 7)
    'equilateral'
    >>> get_triangle_type(5, 5, 3)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(1, 1, 10)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Невозможно построить треугольник
    """
    # Валидация типов
    for s in (side_a, side_b, side_c):
        if not isinstance(s, (int, float)):
            raise IncorrectTriangleSides("Стороны должны быть числовыми значениями")
    
    # Валидация существования (через сортировку)
    s = sorted([side_a, side_b, side_c])
    if s[0] <= 0 or s[0] + s[1] <= s[2]:
        raise IncorrectTriangleSides("Невозможно построить треугольник")

    # Определение типа
    unique_sides = len({side_a, side_b, side_c})
    if unique_sides == 1:
        return "equilateral"
    if unique_sides == 2:
        return "isosceles"
    return "nonequilateral"

if __name__ == "__main__":
    import doctest
    doctest.testmod()