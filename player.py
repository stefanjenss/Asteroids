import pygame #type: ignore
from constants import LINE_WIDTH, PLAYER_RADIUS
from circleshape import CircleShape

# Define a Player class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0

    # Define the `triangle` method to make the player look like a triangle
    # ~ Note: Even though the player appears as a triangle, their actual hit box is a 
    #       circle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            LINE_WIDTH)
