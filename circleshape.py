import pygame
from constants import *

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def check_collision(self, circle):
        combined_radius = self.radius + circle.radius
        distance = pygame.math.Vector2.distance_to(self.position, circle.position)
        return distance <= combined_radius
    
    def check_collide_edge(self):
        y_position = self.position.y
        x_position = self.position.x
        print(type(self.velocity.magnitude()))
        y_direction = self.velocity.y
        x_direction = self.velocity.x
        print(y_position, x_position, y_direction, x_direction)
        if self.position.y <= 0 - (self.radius / 2) and self.velocity.magnitude() >= 0:
            self.position.y = self.position.y + SCREEN_HEIGHT
        
