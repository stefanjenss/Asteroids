from player import Player
import pygame #type: ignore
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    # Initial tests
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()
    
    # Create a clock object and dt variable to contain the delta-time
    clock = pygame.time.Clock()
    dt = 0

    # New instance of the GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize the player in the center of the screen
    player = Player(x = SCREEN_WIDTH / 2,
                    y = SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        log_state()

        # Checking if user has closed the window, and exit's the game loop if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill screen with a solid "black" color
        screen.fill("black")

        # Re-render and update the player each frame
        player.draw(screen)
        player.update(dt)

        # Refresh screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
