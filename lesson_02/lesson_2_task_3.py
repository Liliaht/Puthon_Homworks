import math

def square(side):
    area = side * side
    return math.ceil(area)

side_length = 4.3
print(f"Площадь квадрата со стороной {side_length}:", square(side_length))