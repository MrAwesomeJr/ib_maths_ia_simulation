from objects import *
from math import tan, atan, cos, sin, degrees, radians, pi


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
        # self.screen.draw_circle(self.x + self.width / 2, self.y + self.height / 2, 3, (0,0,255))
        for object in space.objects:
            if type(object) == Point:
                if self.can_be_rendered(space, object.x, object.y, object.z):
                    x, y = self.calculate_pixels(space, object.x - space.x, object.y - space.y, object.z - space.z)
                    self.screen.draw_circle(x + self.x + self.width / 2, - y + self.y + self.height / 2, 10, object.color)

            elif type(object) == Text:
                if self.can_be_rendered(space, object.x, object.y, object.z):
                    x, y = self.calculate_pixels(space, object.x - space.x, object.y - space.y, object.z - space.z)
                    self.screen.draw_text(str(object.text), x + self.x + self.width / 2, - y + self.y + self.height / 2, 10, object.color)

            elif type(object) == Line:
                if self.can_be_rendered(space, object.point1.x, object.point1.y, object.point1.z):
                    if self.can_be_rendered(space, object.point2.x, object.point2.y, object.point2.z):
                        x1, y1 = self.calculate_pixels(space, object.point1.x - space.x, object.point1.y - space.y, object.point1.z - space.z)
                        x2, y2 = self.calculate_pixels(space, object.point2.x - space.x, object.point2.y - space.y, object.point2.z - space.z)
                        self.screen.draw_line(x1 + self.x + self.width / 2, - y1 + self.y + self.height / 2, x2 + self.x + self.width / 2, - y2 + self.y + self.height / 2, object.color)

            elif type(object) == Polyhedron or issubclass(type(object), Polyhedron):
                if object.draw_lines:
                    for line in object.lines:
                        if self.can_be_rendered(space, line[0].x, line[0].y, line[0].z) and self.can_be_rendered(space, line[1].x, line[1].y, line[1].z):
                            x1, y1 = self.calculate_pixels(space, line[0].x - space.x, line[0].y - space.y, line[0].z - space.z)
                            x2, y2 = self.calculate_pixels(space, line[1].x - space.x, line[1].y - space.y, line[1].z - space.z)
                            self.screen.draw_line(x1 + self.x + self.width / 2, - y1 + self.y + self.height / 2, x2 + self.x + self.width / 2, - y2 + self.y + self.height / 2, object.color)

                if object.draw_points:
                    for point in object.points:
                        if self.can_be_rendered(space, point.x, point.y, point.z):
                            x, y = self.calculate_pixels(space, point.x - space.x, point.y - space.y, point.z - space.z)
                            self.screen.draw_circle(x + self.x, y + self.y, 5, object.color)
                
    def calculate_x_pixel(self, space, x, z):
        x, z = self.rotate_x(space, x, z)
        if self.x_fov == 0:
            return x
        new_x = self.width * x / (2 * z * tan(radians(self.x_fov)))
        return new_x
    
    def calculate_y_pixel(self, space, y, z):
        y, z = self.rotate_y(space, y, z)
        if self.y_fov == 0:
            return y
        new_y = self.width * y / (2 * z * tan(radians(self.y_fov)))
        return new_y

    def rotate_x(self, space, x, z):
        if space.x_angle == 0:
            return (x, z)
        if x == 0:
            angle = pi / 2 + radians(space.x_angle)
        else:
            angle = atan(z / x) + radians(space.x_angle)
        new_x = (x**2 + z**2)**(1/2) * cos(angle)
        new_z = (z**2 + x**2)**(1/2) * sin(angle)
        return new_x, new_z

    def rotate_y(self, space, y, z):
        if space.y_angle == 0:
            return (y, z)
        if y == 0:
            angle = pi / 2 + radians(space.y_angle)
        else:
            angle = atan(z / y) + radians(space.y_angle)
        new_y = (y**2 + z**2)**(1/2) * cos(angle)
        new_z = (z**2 + y**2)**(1/2) * sin(angle)
        return new_y, new_z


    def calculate_pixels(self, space, x, y, z):
        new_x = self.calculate_x_pixel(space, x, z)
        new_y = self.calculate_y_pixel(space, y, z)
        return new_x, new_y

    def can_be_rendered(self, space, x, y, z):
        if z < space.z:
            return False
        # within the fov cone
        elif abs(self.calculate_x_pixel(space, x - space.x, z - space.z)) > (self.width / 2):
            return False
        elif abs(self.calculate_y_pixel(space, y - space.y, z - space.z)) > (self.height / 2):
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
        # 0, 0 in 3D space is self.width / 2, self.height in 2D space

        # view cone
        self.screen.draw_polygon([(self.x + space.x + self.width / 2, self.y + self.height - space.z),
                                  (self.x + space.x + self.width / 2 - tan(radians(self.x_fov)) * (self.height - space.z), self.y),
                                  (self.x + space.x + self.width / 2 + tan(radians(self.x_fov)) * (self.height - space.z), self.y)],
                                 (50, 150, 50))

        # you
        self.screen.draw_circle(space.x + self.width / 2 + self.x, - space.z + self.height + self.y, 10, (127, 0, 0))

        for object in space.objects:
            if type(object) == Point:
                if self.can_be_rendered(space, object.x, object.y, object.z):
                    self.screen.draw_circle(object.x + self.width / 2 + self.x, - object.z + self.height + self.y, 10, object.color)

            elif type(object) == Line:
                if self.can_be_rendered(space, object.point1.x, object.point1.y, object.point1.z):
                    if self.can_be_rendered(space, object.point2.x, object.point2.y, object.point2.z):
                        self.screen.draw_line(object.point1.x + self.width / 2 + self.x, - object.point1.z + self.height + self.y, object.point2.x + self.width / 2 + self.x, - object.point2.z + self.height + self.y, object.color)

            elif type(object) == Polyhedron or issubclass(type(object), Polyhedron):
                if object.draw_lines:
                    for line in object.lines:
                        if self.can_be_rendered(space, line[0].x, line[0].y, line[0].z) and self.can_be_rendered(space, line[1].x, line[1].y, line[1].z):
                            self.screen.draw_line(line[0].x + self.width / 2 + self.x, - line[0].z + self.height + self.y, line[1].x + self.width / 2 + self.x, - line[1].z + self.height + self.y, object.color)

                if object.draw_points:
                    for point in object.points:
                        if self.can_be_rendered(space, point.x, point.y, point.z):
                            self.screen.draw_circle(point.x + self.width / 2 + self.x, - point.z + self.height + self.y, 5, object.color)

            self.screen.draw_text(str(space.coords()), space.x + self.width / 2 + self.x, - space.z + self.height + self.y, 10, (255, 255, 255))


    def can_be_rendered(self, space, x, y, z):
        if abs(x) > self.width / 2:
            return False
        elif z <= 0 or z >= self.height:
            return False
        return True