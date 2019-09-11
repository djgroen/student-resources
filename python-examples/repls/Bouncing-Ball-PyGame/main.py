import pygame
import time

pygame.init()
width, height = 800, 600
backgroundColor = 0, 0, 0
screen = pygame.display.set_mode((width, height))
screen.fill(backgroundColor)

e = 0.99   # air resistance coefficient
g = -9.81  # gravity coefficient


class Ball:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx  # x velocity
        self.vy = vy  # y velocity
        self.radius = 10


def step(ball, dt):
    ball.x = ball.x + dt*ball.vx
    ball.y = ball.y + dt*ball.vy
    ball.vy -= dt*g
    ball.vx *= e**dt
    ball.vy *= e**dt
    if ball.y + ball.radius > height:
        ball.vy = -ball.vy
        ball.y = float(height) - ball.radius
    #print(ball.x, ball.y, ball.vx, ball.vy, e**dt)


b = Ball(100.0, 100.0, 5.0, 0.0)

lx = 0  # x coordinate of last circle
ly = 0  # y coordinate of last circle


while True:
    # overwrite old circle with bg color
    #pygame.draw.circle(screen, backgroundColor, (lx,   ly), int(b.radius), 0)

    # draw new circle
    pygame.draw.circle(screen, (255, 255, 0), (int(b.x), int(b.y)), int(b.radius), 0)

    lx = int(b.x)
    ly = int(b.y)

    pygame.display.flip()
    step(b, 0.25)
    time.sleep(25 / 1000)
