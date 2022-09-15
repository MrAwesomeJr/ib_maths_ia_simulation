import pygame

class Space:
    def __init__(self, x_fov, y_fov):
        self.x_fov = x_fov
        self.y_fov = y_fov
        self.x = 0
        self.y = 0
        self.z = 0
        self.objects = []
        self.sensitivity = 50
        self.bounds = (1000, 1000, 1000)

    def update_space(self):
        self.get_input()
        self.set_bounds()

    def get_input(self):
        key_down_events = pygame.event.get(eventtype=pygame.KEYDOWN)

        for key_event in key_down_events:
            if key_event.key in (pygame.K_LEFT, pygame.K_a):
                self.x -= self.sensitivity
            elif key_event.key in (pygame.K_RIGHT, pygame.K_d):
                self.x += self.sensitivity
            elif key_event.key in (pygame.K_UP, pygame.K_w):
                self.z += self.sensitivity
            elif key_event.key in (pygame.K_DOWN, pygame.K_s):
                self.z -= self.sensitivity
            elif key_event.key == pygame.K_SPACE:
                self.y -= self.sensitivity
            elif key_event.key == pygame.K_LSHIFT:
                self.y += self.sensitivity

    def set_bounds(self):
        if self.x > self.bounds[0]:
            self.x = self.bounds[0]
        elif self.x < -self.bounds[0]:
            self.x = -self.bounds[0]

        if self.y > self.bounds[1]:
            self.y = self.bounds[1]
        elif self.y < -self.bounds[1]:
            self.y = -self.bounds[1]

        if self.z > self.bounds[2]:
            self.z = self.bounds[2]
        elif self.z < -self.bounds[2]:
            self.z = -self.bounds[2]

    def coords(self):
        return (self.x, self.y, self.z)