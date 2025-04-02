import pygame
from circleshape import CircleShape
from constants import *
from weapon import *
import math

class Player(CircleShape):

    weapons = [
        Submachine(),
        SniperRifle(),
        Rifle(),
    ]

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.weapon = 0  #default is submachine

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "green", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):

        keys = pygame.key.get_pressed()
        if self.timer > 0:
            self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(self.weapons[self.weapon])
        if keys[pygame.K_f]:
            self.switch_weapon()


        if not (keys[pygame.K_w] or keys[pygame.K_s]):
            if abs(self.velocity.magnitude()) >= 0.2:
                self.velocity *= PLAYER_DECELERATION

        self.position += self.velocity

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        intial_velocity = self.velocity.magnitude()
        if not abs(intial_velocity) > PLAYER_MAX_SPEED:
            self.velocity = forward * (intial_velocity + PLAYER_ACCELERATION * dt)
        else:
            self.velocity = forward * (intial_velocity)
        
    def switch_weapon(self):
        if self.weapon + 1 == 3:
            self.weapon = 0
        else:
            self.weapon += 1

    def shoot(self, weapon):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y, weapon.range, weapon.damage)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = forward * weapon.power
            self.timer = weapon.rate

class Shot(CircleShape):
    def __init__(self, x, y, radius, damage):
        super().__init__(x, y, radius)
        self.damage = damage

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    

    