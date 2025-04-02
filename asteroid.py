import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, health):
        super().__init__(x, y, radius)
        self.health = health

    def draw(self, screen):
        pygame.draw.circle(screen, "brown", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def check_health(self, shot):
        self.health = self.health - shot.damage
        if self.health <= 0:
            self.split()
            return True
        return False

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20, 50)
            new_raidus = self.radius - ASTEROID_MIN_RADIUS
            new_health = self.health - 50
            asteroid_one = Asteroid(self.position.x, self.position.y, new_raidus, new_health)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_raidus, new_health)
            asteroid_one.velocity = self.velocity.rotate(random_angle) * 1.2
            asteroid_two.velocity = self.velocity.rotate(-random_angle) * 1.2
        else:
            self.explode()
            

    def explode(self):
        for _ in range(360):
            particle = Particle(self.position.x, self.position.y)


class Particle(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PARTICLE_RADIUS)
        self.life_span = .1
        angle = random.uniform(0, 360)
        speed = random.randint(1000, 2000)
        self.velocity = pygame.math.Vector2(0, 1).rotate(angle) * speed

    def draw(self, screen):
        color = random.choice(("red", "orange", "yellow"))
        pygame.draw.circle(screen, color, (self.position.x, self.position.y), self.radius, 1)

    def update(self, dt):
        self.position += self.velocity * dt
        self.check_die(dt)

    def check_die(self, dt):
        self.life_span -= dt
        if self.life_span <= 0:
            self.kill()
            
         