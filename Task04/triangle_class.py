from typing import Literal, Union

class IncorrectTriangleSides(Exception):
    pass

class Triangle:
    def __init__(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]):
        if not all(isinstance(x, (int, float)) for x in (a, b, c)):
            raise IncorrectTriangleSides("Тип данных не является числом")
        
        sides = sorted([a, b, c])
        if sides[0] <= 0 or sides[0] + sides[1] <= sides[2]:
            raise IncorrectTriangleSides("Нарушены правила построения треугольника")
            
        self._sides = (a, b, c)

    def perimeter(self) -> Union[int, float]:
        return sum(self._sides)

    def triangle_type(self) -> str:
        count = len(set(self._sides))
        mapping = {1: "equilateral", 2: "isosceles", 3: "nonequilateral"}
        return mapping[count]