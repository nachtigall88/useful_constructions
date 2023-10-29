"""
конструкція для перевірки головного виконавчого файлу
"""
if __name__ == '__main__':
    pass
else:
    raise SystemExit('this is not a library!')

"""
паттерн фабричний метод
https://www.youtube.com/watch?v=FONWO-xdqYo&t=279s
"""
from enum import Enum
from math import sin, cos


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x:{self.x}, y:{self.y}'

    # def __init__(self,a,b, system = CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x= a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.y = a*cos(b)
    #         self.x = a*sin(b)

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


p = Point(1, 2)
p2 = Point.new_polar_point(1, 2)
print(p, p2)
