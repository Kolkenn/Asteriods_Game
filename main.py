import pygame
from player import Player
from constants import *

def main():
    pygame.init() # Initialize pygame.
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)
        
        screen.fill("black")
        player.draw(screen) # Render the player on the screen.
        pygame.display.flip() # Update the full display Surface to the screen
        
        
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()