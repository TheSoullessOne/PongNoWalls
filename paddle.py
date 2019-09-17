import pygame
import random
from colors import *


class VerticalPaddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_up(self):
        self.y -= self.vel
        self.rect.y = self.y

    def move_down(self):
        self.y += self.vel
        self.rect.y = self.y

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))

    def get_move(self, ball_rect):
        randint = random.randint(1, 3)
        if randint == 1:
            if ball_rect.x < 400:
                if ball_rect.y > self.rect.centery:
                    difference = ball_rect.y - self.rect.top
                    print(str(ball_rect.y) + ' ' + str(self.rect.top))
                    print(difference)
                    self.y += 1
                    self.rect.y += 1
                elif ball_rect.y < self.rect.centery:
                    difference = self.rect.centery - ball_rect.y
                    print(str(ball_rect.y) + ' ' + str(self.rect.top))
                    print(difference)
                    self.y -= 1
                    self.rect.y -= 1


class HorizontalPaddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_left(self):
        self.y -= self.vel

    def move_right(self):
        self.y += self.vel

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.width, self.height))
