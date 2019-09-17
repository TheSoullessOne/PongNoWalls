import pygame
import sys
from pygame.locals import *
from colors import *
from ball import Ball
from paddle import VerticalPaddle, HorizontalPaddle


GAME_WIDTH = 800
GAME_HEIGHT = 600
DISPLAY = (GAME_WIDTH, GAME_HEIGHT)
BALL_SPEED = 2
PADDLE_SPEED = 3
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Pong')
surface = pygame.display.set_mode(DISPLAY, 0, 32)
surface.fill(BLACK)
pygame.mixer.music.load('Sounds/background.mp3')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True
bar1_header = 'Computer: '
bar2_header = 'Player: '


def random_ball_vel():
    x = random.randint(-2, 2)
    while x == 0:
        x = random.randint(-2, 2)
    y = random.randint(-2, 2)
    while y == 0:
        y = random.randint(-2, 2)
    return x, y


def play():
    init_velocity = random_ball_vel()
    ball = Ball(400, 250, 15, 15, init_velocity)
    paddles = []
    v_paddle_player = VerticalPaddle(750, 200, 20, 100)
    v_paddle_computer = VerticalPaddle(30, 200, 20, 100)
    paddles.append(v_paddle_player.rect)
    paddles.append(v_paddle_computer.rect)
    line_color = get_random_color()
    font = pygame.font.SysFont("calibri", 40)
    bar1_score = 0
    bar2_score = 0
    header1 = font.render(str(bar1_header), True, (255, 255, 255))
    header2 = font.render(str(bar2_header), True, (255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and v_paddle_player.y > 0:
            v_paddle_player.move_up()
        if keys[pygame.K_DOWN] and v_paddle_player.y < (GAME_HEIGHT - v_paddle_player.height - 100):
            v_paddle_player.move_down()

        #  if keys[pygame.K_LEFT] and v_paddle_player.x > 0:
        #    v_paddle_player.move_left()
        #  if keys[pygame.K_RIGHT] and v_paddle_player.x < (GAME_WIDTH - v_paddle_player.height):
        #    v_paddle_player.move_right()

        surface.fill(BLACK)

        v_paddle_player.draw(surface)
        v_paddle_computer.get_move(ball.rect)
        v_paddle_computer.draw(surface)
        ball.draw(surface)
        ball.move()
        ball.collide(paddles)
        reset = []
        did_reset, scorer = ball.reset(GAME_WIDTH / 2, GAME_HEIGHT / 2, random_ball_vel())
        if did_reset:
            line_color = get_random_color()
            if scorer == 'player':
                bar2_score += 1
                score2 = font.render(str(bar2_score), True, (255, 255, 255))
            elif scorer == 'computer':
                bar1_score += 1
                score1 = font.render(str(bar1_score), True, (255, 255, 255))
        pygame.draw.line(surface, line_color, (GAME_WIDTH / 2, GAME_HEIGHT - 100), (GAME_WIDTH / 2, 0))
        pygame.draw.rect(surface, BLUE, (0, GAME_HEIGHT - 100, GAME_WIDTH, 100))
        score1 = font.render(str(bar1_score), True, (255, 255, 255))
        score2 = font.render(str(bar2_score), True, (255, 255, 255))
        surface.blit(header1, (200, GAME_HEIGHT - 100))
        surface.blit(score1, (350, GAME_HEIGHT - 50))
        surface.blit(header2, (425, GAME_HEIGHT - 100))
        surface.blit(score2, (425, GAME_HEIGHT - 50))
        pygame.display.update()


play()
