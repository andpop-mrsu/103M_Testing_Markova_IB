import math
from typing import List, Optional, Union

def find_roots(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Optional[List[float]]:
    """Вычисляет корни ax^2 + bx + c = 0."""
    # Обработка линейных и вырожденных случаев
    if a == 0:
        if b == 0:
            return None if c == 0 else []
        return [float(-c / b)]

    # Работа с дискриминантом
    d = b**2 - 4*a*c
    
    if d < 0:
        return []
    
    if d == 0:
        return [-b / (2 * a)]
    
    sqrt_d = math.sqrt(d)
    x1 = (-b - sqrt_d) / (2 * a)
    x2 = (-b + sqrt_d) / (2 * a)
    
    roots = [x1, x2]
    roots.sort()
    return roots