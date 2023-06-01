import math
def quad_eq(a, b, c) -> tuple:
    discr = b ** 2 - 4 * a * c
    if a == 0:
        return False
    if discr >= 0:
        x1 = (-b + math.sqrt(discr))/(2 * a)
        x2 = (-b - math.sqrt(discr))/(2 * a)
        roots = x1, x2
        return roots
    else:
        return None

assert quad_eq(1, 2, 3) == None
assert quad_eq(0, 2, 3) == False
assert quad_eq(1, 2, -3) == (1, -3)
