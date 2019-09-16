import pygame
import sys
from pygame.locals import *
from pygame.math import Vector2
import random


GAME_WIDTH = 800
GAME_HEIGHT = 500
BALL_SPEED = 2
PADDLE_SPEED = 3

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Ball:
    def __init__(self, rect, radius=20, bg_color=WHITE, velocity=(1, 1), scale=1):
        self.rect = pygame.Rect(rect)
        self.radius = radius
        self.color = bg_color
        self.velocity = vector2(velocity, scale)

    def __str__(self):
        return 'This is a ball with a radius {:2f}'.format(self.radius)

    def __repr__(self):
        return 'Ball(radius={:2f})'.format(self.radius)

    def get_radius(self):
        return self.radius

    def get_color(self):
        return self.color

    def get_velocity(self):
        return self.velocity

    def get_rect(self):
        return self.rect

    def move_ball(self):
        self.rect.left += self.velocity[0]
        self.rect.top += self.velocity[1]


class Paddle:
    def __init__(self, rect, height=100, width=50):
        self.rect = pygame.Rect(rect)
        self.height = height
        self.width = width

    def __str__(self):
        return 'This is a pong paddle with a height of {:2f} and width of {:2f}'.format(self.height, self.width)

    def __repr__(self):
        return 'Paddle(height={:2f}, width={:2f}'.format(self.height, self.width)

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width


def vector2(xy_tuple, scale):
    v = Vector2()
    v[0], v[1] = xy_tuple[0], xy_tuple[1]
    return v * scale


def get_initial_ball_vel():
    x = random.randint(-2, 2)
    while x == 0:
        x = random.randint(-2, 2)
    y = random.randint(-2, 2)
    while y == 0:
        y = random.randint(-2, 2)
    return x, y


def play():
    pygame.init()
    surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT), 0, 32)
    pygame.display.set_caption('Pong')
    surface.fill(BLACK)

    pygame.mixer.music.load('Sounds/background.mp3')
    pygame.mixer.music.play(-1, 0.0)
    musicPlaying = True

    init_velocity = get_initial_ball_vel()
    ball = Ball(rect=(GAME_WIDTH / 2, GAME_HEIGHT / 2, 40, 40), velocity=init_velocity)
    #  pygame.draw.rect(surface, ball.get_color(), ball.get_rect(), 0)
    ballRect = pygame.draw.circle(surface, ball.get_color(), (int(GAME_WIDTH / 2), int(GAME_HEIGHT / 2)), ball.get_radius(), 0)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        print(ball.get_velocity())
        ballRect.left += ball.get_velocity()[0]
        ballRect.top += ball.get_velocity()[1]
        print(ballRect.left, ballRect.top)
        pygame.display.update()
        ballRect = pygame.draw.circle(surface, ball.get_color(), (int(GAME_WIDTH / 2), int(GAME_HEIGHT / 2)), ball.get_radius(), 0)


play()
