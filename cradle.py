import pygame
import math
import sys

# Ball class
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.line(screen, self.color, (int(self.x), int(self.y)), (int(self.x), 0), 2)

    def update(self, dt):
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

# Cradle class
class Cradle:
    def __init__(self, num_balls, ball_radius, ball_color, screen_width, screen_height):
        self.num_balls = num_balls
        self.ball_radius = ball_radius
        self.balls = []
        self.create_balls(ball_color, screen_width, screen_height)

    def create_balls(self, ball_color, screen_width, screen_height):
        spacing = 2 * self.ball_radius + 10
        start_x = screen_width // 2 - (spacing * (self.num_balls - 1)) // 2
        for i in range(self.num_balls):
            x = start_x + i * spacing
            y = screen_height // 2
            ball = Ball(x, y, self.ball_radius, ball_color)
            self.balls.append(ball)

    def draw(self, screen):
        for ball in self.balls:
            ball.draw(screen)

    def update(self, dt):
        for ball in self.balls:
            ball.update(dt)

    def handle_collisions(self):
        for i in range(self.num_balls - 1):
            for j in range(i + 1, self.num_balls):
                ball1 = self.balls[i]
                ball2 = self.balls[j]
                dist = math.hypot(ball1.x - ball2.x, ball1.y - ball2.y)
                if dist < 2 * self.ball_radius:
                    ball1.vx, ball2.vx = ball2.vx, ball1.vx
                    ball1.vy, ball2.vy = ball2.vy, ball1.vy

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
BALL_COLOR = (0, 0, 255)
BALL_RADIUS = 20
NUM_BALLS = 5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Newton's Cradle")
clock = pygame.time.Clock()

# Create the cradle
cradle = Cradle(NUM_BALLS, BALL_RADIUS, BALL_COLOR, WIDTH, HEIGHT)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.get_time() / 1000  # Delta time in seconds

    # Update and draw the cradle
    screen.fill(BACKGROUND_COLOR)
    cradle.update(dt)
    cradle.handle_collisions()
    cradle.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()
sys.exit()
