import pygame #type: ignore
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    # New instance of the GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        log_state()

        # Checking if user has closed the window, and exit's the game loop if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill screen with a solid "black" color
        screen.fill("black")

        # Refresh screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
