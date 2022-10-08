import pygame
import sys
from screen import Screen
from space import Space
from render import *
from objects import *

x_fov = 45
y_fov = 45

pygame.init()

screen = Screen((255, 255, 255))
space = Space(x_fov, y_fov)
render2d_topdown = Render2D_TopDown(screen, x_fov, y_fov, 0, 0, 586, 854)
render3d = Render3D(screen, x_fov, y_fov, 586, 0, 854, 854)
# render3d = Render3D(screen, x_fov, y_fov, 0, 0, 1440, 854)

# space.objects.append(Point(0, 0, 500))
space.objects.append(Cube(0, 0, 500, 100))
space.objects.append(Line((0, 0, 400), (0, 0, 600), (0, 0, 255)))
space.objects.append(Line((-100, 0, 500), (100, 0, 500), (255, 0, 0)))
space.objects.append(Line((0, -100, 500), (0, 100, 500), (0, 255, 0)))
space.objects.append(Text(0, 0, 600, "z"))
space.objects.append(Text(100, 0, 500, "x"))
space.objects.append(Text(0, 100, 500, "y"))

while True:
    render2d_topdown.render(space)
    render3d.render(space)
    screen.update_screen()
    space.get_input()

    if len(pygame.event.get(eventtype=pygame.QUIT)) >= 1:
        sys.exit()