import pygame
from pygame.sprite import Group
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
import sys

from shot import Shot

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

    updatable = Group()
    drawable = Group()
    asteroids = Group()
    shots = Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    player = Player(p_x_position, p_y_position)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(max_fps) / 1000

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            detect_player = obj.detect_shape(player)
            if detect_player:
                print("Game over!")
                sys.exit()

            for shot in shots:
                detect_shot = obj.detect_shape(shot)
                if detect_shot:
                    obj.split()
                    shot.kill()

            
        pygame.display.flip()


if __name__ == "__main__":
    main()
