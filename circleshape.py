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
        if self.position.y <= 0 - (self.radius / 2) and self.velocity.y < 0:
            self.position.y = self.position.y + SCREEN_HEIGHT + self.radius
        if self.position.y >= SCREEN_HEIGHT + (self.radius / 2) and self.velocity.y > 0:
            self.position.y = self.position.y - SCREEN_HEIGHT - self.radius
        if self.position.x <= 0 - (self.radius / 2) and self.velocity.x < 0:
            self.position.x = self.position.x + SCREEN_WIDTH + self.radius
        if self.position.x >= SCREEN_WIDTH - (self.radius / 2) and self.velocity.x > 0:
            self.position.x = self.position.x - SCREEN_WIDTH - self.radius
        
