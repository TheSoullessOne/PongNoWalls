import pygame
from colors import *
from pygame.math import Vector2


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

    def move(self):
        self.x -= (self.vel * (self.movex / 10))
        self.y -= (self.vel * (self.movey / 10))
        self.rect.topleft = self.x, self.y

    def collide(self, paddles):
        if self.y > 493 or self.y < 7:
            self.movey *= -1

        if self.rect.colliderect(paddles[0]) or self.rect.colliderect(paddles[1]):
            self.movex *= -1
            self.vel += 0.2

    def reset(self, x, y,  init_vel):
        if self.x < 0 or self.x > 800:
            if self.x < 0:
                scorer_string = 'player'
                print('player scored!')
            elif self.x > 800:
                scorer_string = 'computer'
                print('comp scored :(')
            self.x = x
            self.y = y
            self.movex = init_vel[0]
            self.movey = init_vel[1]
            self.vel = 1
            return True, scorer_string
        return False, ' '

    def get_vel(self):
        return self.movex, self.movey
