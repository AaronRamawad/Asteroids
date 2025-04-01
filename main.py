import pygame
from constants import *
from player import Player
from asteroid import Asteroid

def main():

    print("Starting Asteroids!!!")
    print(f"Screen Width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    Asteroid.containers = (asteroids, updatable, drawable)


    while True:

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (125, 0, 255))
        for object in drawable:
            object.draw(screen)
        updatable.update(dt)

        pygame.display.flip()

        time_passed = clock.tick(144)
        dt = time_passed / 1000


if __name__ == "__main__":
    main()