from point import Point

class Triangle:
    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        self.__vertices = [vertex1, vertex2, vertex3]
        self.__vertices_tpl = [(0, 1), (1, 2), (2, 0)]

    def perimeter(self):
        perimeter = 0.0
        for tpl in self.__vertices_tpl:
            point1 = self.__vertices[tpl[0]]
            point2 = self.__vertices[tpl[1]]
            perimeter += point1.distance_from_point(point2)
        
        return perimeter

if __name__ == "__main__":
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter()) # 3.414213562373095
