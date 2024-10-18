import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player
from shot import Shot
from constants import *

def main():
    pygame.init() # Initialize pygame.
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable,shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(delta_time)

        for obj in asteroids:
            if player.collides(obj):
                print("Game over!")
                return
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides(asteroid):
                    shot.kill()
                    asteroid.split()
        
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip() # Update the full display Surface to the screen
        
        
        delta_time = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()