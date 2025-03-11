import pygame
from constants import *
from player import Player




screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
stop_game = 0




def main():
    pygame.init


    dt = 0
    frame_rate_clock = pygame.time.Clock()

    player_character = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while stop_game == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, [0,0,0])

        player_character.draw(screen)

        pygame.display.flip()

        


        dt = frame_rate_clock.tick(60)
        dt /= 1000










if __name__ == "__main__":
    main()