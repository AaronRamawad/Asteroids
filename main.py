import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():

    print("Starting Asteroids!!!")
    print(f"Screen Width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    pygame.font.init()
    my_font = pygame.font.SysFont("Comic Sans MS", 30)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
           
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    player_score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (125, 0, 255))
        player_score_surface = my_font.render(f"Score: {str(player_score)}", False, "white")
        screen.blit(player_score_surface, (0,0))
        for object in drawable:
            object.draw(screen)
        updatable.update(dt)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over!")
                exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()

        player_score = pygame.time.get_ticks() // 1000
        time_passed = clock.tick(FPS)
        dt = time_passed / 1000


if __name__ == "__main__":
    main()