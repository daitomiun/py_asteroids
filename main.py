import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    max_fps = 60
    clock = pygame.time.Clock()
    dt = 0

    p_x_position = SCREEN_WIDTH / 2
    p_y_position = SCREEN_HEIGHT / 2
    player = Player(p_x_position, p_y_position)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(max_fps) / 1000



if __name__ == "__main__":
    main()
