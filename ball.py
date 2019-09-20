import pygame
from colors import *
from pygame.math import Vector2

ball_image = pygame.image.load('Images/ball.png')


def vector2(xy_tuple, scale):
    v = Vector2()
    v[0], v[1] = xy_tuple[0], xy_tuple[1]
    return v * scale


#  Class to hold all of the ball functions
class Ball:
    def __init__(self, x, y, width, height, init_vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1
        self.movex = init_vel[0]
        self.movey = init_vel[1]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))
        surface.blit(ball_image, (self.x, self.y))

    def move(self):
        self.x -= (self.vel * (self.movex / 10))
        self.y -= (self.vel * (self.movey / 10))
        self.rect.topleft = self.x, self.y

    def collide(self, paddles):
        if self.rect.colliderect(paddles[0]) or self.rect.colliderect(paddles[1]):
            self.movex *= -1
            self.vel += 0.2
            collision_sound = pygame.mixer.Sound('Sounds/paddle_hit.wav')
            collision_sound.play()

        if self.rect.colliderect(paddles[2]) or self.rect.colliderect(paddles[3]) or self.rect.colliderect(paddles[4]) \
                or self.rect.colliderect(paddles[5]):
            self.movey *= -1
            self.vel += 0.1
            collision_sound = pygame.mixer.Sound('Sounds/paddle_hit.wav')
            collision_sound.play()

    def reset(self, x, y,  init_vel):
        if self.x < 0 or self.x > 800 or self.y < 0 or self.y > 500:
            scorer_string = ''
            if self.x < 400 and (self.y < 0 or self.y > 500):
                scorer_string = 'player'
            if self.x > 400 and (self.y < 0 or self.y > 500):
                scorer_string = 'computer'
            if self.x < 0:
                scorer_string = 'player'
            elif self.x > 800:
                scorer_string = 'computer'
            self.x = x
            self.y = y
            self.movex = init_vel[0]
            self.movey = init_vel[1]
            self.vel = 1
            return True, scorer_string
        return False, ''

    def get_vel(self):
        return self.movex, self.movey
