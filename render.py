from objects import *
from math import tan, atan, degrees, radians

class Render3D:
    def __init__(self, screen, x_fov, y_fov, x, y, width, height):
        self.screen = screen
        self.x_fov = x_fov
        self.y_fov = y_fov
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, space):
        self.screen.draw_rect(self.x, self.y, self.width, self.height, (0, 0, 0))
        for object in space.objects:
            if type(object) == Point:
                if self.can_be_rendered(space, object.x, object.y, object.z):
                    x, y = self.calculate_pixels(object.x - space.x, object.y - space.y, object.z - space.z)
                    self.screen.draw_circle(x + self.x, y + self.y, 5, object.color)

            elif type(object) == Polyhedron or issubclass(type(object), Polyhedron):
                if object.draw_lines:
                    for line in object.lines:
                        if self.can_be_rendered(space, line[0].x, line[0].y, line[0].z) and self.can_be_rendered(space, line[1].x, line[1].y, line[1].z):
                            x1, y1 = self.calculate_pixels(line[0].x - space.x, line[0].y - space.y, line[0].z - space.z)
                            x2, y2 = self.calculate_pixels(line[1].x - space.x, line[1].y - space.y, line[1].z - space.z)
                            self.screen.draw_line(x1 + self.x, y1 + self.y, x2 + self.x, y2 + self.y, object.color)

                if object.draw_points:
                    for point in object.points:
                        if self.can_be_rendered(space, point.x, point.y, point.z):
                            x, y = self.calculate_pixels(point.x - space.x, point.y - space.y, point.z - space.z)
                            self.screen.draw_circle(x + self.x, y + self.y, 10, object.color)
                
    def calculate_x_pixel(self, x, z):
        if self.x_fov == 0:
            return x
        new_x = self.width / 2 * (1 + degrees(atan(x / (z + (2 * tan(radians(self.x_fov)) / self.width)))) / (2 * self.x_fov))
        return new_x
    
    def calculate_y_pixel(self, y, z):
        if self.y_fov == 0:
            return y
        new_y = self.height / 2 * (1 + degrees(atan(y / (z + (2 * tan(radians(self.y_fov)) / self.height)))) / (2 * self.y_fov))
        return new_y

    def calculate_pixels(self, x, y, z):
        new_x = self.calculate_x_pixel(x, z)
        new_y = self.calculate_y_pixel(y, z)
        return new_x, new_y

    def can_be_rendered(self, space, x, y, z):
        if z <= space.z:
            return False
        return True


class Render2D_TopDown:
    def __init__(self, screen, x_fov, y_fov, x, y, width, height):
        self.screen = screen
        self.x_fov = x_fov
        self.y_fov = y_fov
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, space):
        self.screen.draw_rect(self.x, self.y, self.width, self.height, (100, 100, 100))