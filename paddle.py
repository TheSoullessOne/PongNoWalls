import pygame
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
        randint = random.randint(1, 5)
        if randint == 1:
            if ball_rect.x < 400:
                if ball_rect.y > self.rect.centery:
                    self.y += 1
                    self.rect.y += 1
                elif ball_rect.y < self.rect.centery:
                    self.y -= 1
                    self.rect.y -= 1

    def reset(self, x, y, surface):
        self.x = self.rect.x = x
        self.y = self.rect.y = y
        self.draw(surface)


class HorizontalPaddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_left(self):
        self.x -= self.vel
        self.rect.x = self.x

    def move_right(self):
        self.x += self.vel
        self.rect.x = self.x

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))

    def get_move(self, ball_rect):
        randint = random.randint(1, 5)
        if randint == 1:
            if ball_rect.x < 380:
                if ball_rect.x > self.rect.centerx:
                    self.x += 1
                    self.rect.x += 1
                elif ball_rect.x < self.rect.centerx:
                    self.x -= 1
                    self.rect.x -= 1

    def reset(self, x, y, surface):
        self.x = self.rect.x = x
        self.y = self.rect.y = y
        self.draw(surface)
