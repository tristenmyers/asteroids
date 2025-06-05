import pygame
import sys
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
stop_game = 0

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Asteroid.containers = (asteroids, updatable, drawable)
Player.containers = (updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (updatable, drawable, shots)


def main():
    pygame.init()

    Asteroid_Field = AsteroidField()

    font = pygame.font.SysFont("verdana", 30)

    lives = 3
    score = 0

    dt = 0

    frame_rate_clock = pygame.time.Clock()

    player_character = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"Starting Lives: {lives}")
    while stop_game == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, [0,0,0])
        life_counter = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(life_counter, (10, 10))
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            if player_character.collision_check(asteroid):
                if lives < 2:
                    sys.exit(f"Game Over! Score: {score}")
                else:
                    asteroid.split()
                    lives -= 1

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.split()
                    score += 10



        pygame.display.flip()

    

        dt = frame_rate_clock.tick(60)
        dt /= 1000










if __name__ == "__main__":
    main()