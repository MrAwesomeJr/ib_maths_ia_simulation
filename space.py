import pygame

class Space:
    def __init__(self, x_fov, y_fov):
        self.x_fov = x_fov
        self.y_fov = y_fov
        self.x = 0
        self.y = 0
        self.z = 0
        self.objects = []

    def get_input(self):
        key_down_events = pygame.event.get(eventtype=pygame.KEYDOWN)
        key_up_events = pygame.event.get(eventtype=pygame.KEYUP)

        for key_event in key_down_events:
            if key_event.key in (pygame.K_LEFT, pygame.K_a):
                self.x -= 100
            elif key_event.key in (pygame.K_RIGHT, pygame.K_d):
                self.x += 100
            elif key_event.key in (pygame.K_UP, pygame.K_w):
                self.z += 100
            elif key_event.key in (pygame.K_DOWN, pygame.K_s):
                self.z -= 100