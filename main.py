import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid, Particle
from asteroidfield import AsteroidField

def kill_all(group):
    for item in group:
        item.kill()

def main():

    print("Starting Asteroids!!!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    pygame.font.init()
    regular_font = pygame.font.SysFont("Comic Sans MS", 30)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    particles = pygame.sprite.Group()
    shots = pygame.sprite.Group()
           
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    Particle.containers = (particles, drawable, updatable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    player_score = 0
    player_lives = 3
    time = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        background = pygame.image.load("background.jpg")
        screen.blit(background, (0, 0))
        player_score_surface = regular_font.render(f"Score: {str(player_score)}", False, "white")
        screen.blit(player_score_surface, (0,0))
        time_surface = regular_font.render(f"{str(time)}", False, "white")
        time_size = regular_font.size(f"{str(time)}")
        screen.blit(time_surface, (SCREEN_WIDTH / 2 - time_size[0], 0))
        player_lives_surface = regular_font.render(f"Lives: {str(player_lives)}", False, "white")
        player_lives_size = regular_font.size(f"Lives: {str(player_lives)}")
        screen.blit(player_lives_surface, (SCREEN_WIDTH - player_lives_size[0], 0))
        for object in drawable:
            object.draw(screen)
        updatable.update(dt)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                player_lives -= 1
                kill_all(drawable)
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                if player_lives == 0:
                    print("Game Over!")
                    exit()


        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    is_split = asteroid.check_health(shot)
                    if is_split:
                        player_score += 1

        for object in drawable:
            object.check_collide_edge()

        pygame.display.flip()

        time = pygame.time.get_ticks() // 1000
        time_passed = clock.tick(FPS)
        dt = time_passed / 1000


if __name__ == "__main__":
    main()