import pygame #type: ignore
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    # Initialize pygame
    pygame.init()
    
    # New instance of the GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock object and dt variable to contain the delta-time
    clock = pygame.time.Clock()

    # Groups containers to hold and manage muliple game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add the Player class to the `updatable` and `drawable` groups
    Player.containers = (updatable, drawable)

    # Initialize the player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Define the delta-time for the game
    dt = 0

    # Game loop
    while True:
        log_state()

        # Checking if user has closed the window, and exit's the game loop if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update the updatables
        updatable.update(dt)

        # Fill screen with a solid "black" color
        screen.fill("black")

        # Re-render the drawable objects each frame
        for obj in drawable:
            obj.draw(screen)

        # Refresh screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
