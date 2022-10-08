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

class Text:
    def __init__(self, x, y, z, text, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.z = z
        self.text = text
        self.color = color

class Line:
    def __init__(self, coords1, coords2, color=(255, 255, 255)):
        self.color = color
        self.point1 = Point(coords1[0], coords1[1], coords1[2], color)
        self.point2 = Point(coords2[0], coords2[1], coords2[2], color)

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


        # points which share two of the same axes should have a line between them
        for point1 in self.points:
            for point2 in self.points:
                if point1.list() != point2.list():
                    count = 0
                    for index, direction in enumerate(point1.list()):
                        if direction == point2.list()[index]:
                            count += 1

                    if count == 2 and (point2, point1) not in self.lines:
                        self.lines.append((point1, point2))
