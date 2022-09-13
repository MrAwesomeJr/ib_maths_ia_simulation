class Point:
    def __init__(self, x, y, z, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.z = z
        self.color = color

    def list(self):
        return (self.x, self.y, self.z)

    def __str__(self):
        return str(self.list())


class Polyhedron:
    def __init__(self):
        self.points = []
        self.lines = []
        self.draw_points = True
        self.draw_lines = True


class Cube(Polyhedron):
    def __init__(self, x, y, z, side_length, color=(255, 255, 255)):
        super().__init__()
        self.color = color
        self.draw_points = False

        radius = side_length / 2
        for x_value in (x - radius, x + radius):
            for y_value in (y - radius, y + radius):
                for z_value in (z - radius, z + radius):
                    self.points.append(Point(x_value, y_value, z_value, self.color))

        print(len(self.points))

        # points which share two of the same axes should have a line between them
        for i1, point1 in enumerate(self.points):
            print(point1)
            for i2, point2 in enumerate(self.points):
                if point1.list() != point2.list() and len(set(point1.list()) & set(point2.list())) == 2:
                    if (point2, point1) not in self.lines:
                        self.lines.append((point1, point2))
                        print(i1, i2)

        print(len(self.lines))
