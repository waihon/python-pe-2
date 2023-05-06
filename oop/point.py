from math import hypot

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def distance_from_xy(self, x, y):
        dx = x - self.get_x()
        dy = y - self.get_y()
        return hypot(dx, dy)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.get_x(), point.get_y())

if __name__ == "__main__":
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    print(point1.distance_from_point(point2)) # 1.4142135623730951
    print(point1.distance_from_xy(3, 4))      # 5.0
    print(point2.distance_from_xy(2, 0))      # 1.4142135623730951
