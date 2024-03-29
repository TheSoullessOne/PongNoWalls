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
wait_screen = 'First to 5 Wins, Press Enter to play....'
bar1_header = 'Computer: '
bar2_header = 'Player: '
win_end_screen = 'You have won!'
lose_end_screen = 'Aww man, you lost to a computer...'


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
    ball = Ball(400, 250, 25, 25, init_velocity)
    paddles = []
    v_paddle_player = VerticalPaddle(770, 200, 10, 100)
    v_paddle_computer = VerticalPaddle(20, 200, 10, 100)
    ht_paddle_player = HorizontalPaddle(550, 10, 100, 10)
    hb_paddle_player = HorizontalPaddle(550, 480, 100, 10)
    ht_paddle_computer = HorizontalPaddle(250, 10, 100, 10)
    hb_paddle_computer = HorizontalPaddle(250, 480, 100, 10)
    paddles.append(v_paddle_player.rect)
    paddles.append(v_paddle_computer.rect)
    paddles.append(ht_paddle_computer)
    paddles.append(hb_paddle_computer)
    paddles.append(ht_paddle_player)
    paddles.append(hb_paddle_player)
    line_color = get_random_color()
    font = pygame.font.SysFont("calibri", 40)
    bar1_score = 0
    bar2_score = 0
    wait = font.render(str(wait_screen), True, (255, 255, 255))
    header1 = font.render(str(bar1_header), True, (255, 255, 255))
    header2 = font.render(str(bar2_header), True, (255, 255, 255))
    surface.blit(wait, ((GAME_WIDTH - 500) / 2, (GAME_HEIGHT - 200) / 2))

    pygame.draw.line(surface, line_color, (GAME_WIDTH / 2, GAME_HEIGHT - 100), (GAME_WIDTH / 2, 0), 5)
    pygame.draw.rect(surface, BLUE, (0, GAME_HEIGHT - 100, GAME_WIDTH, 100))
    score1 = font.render(str(bar1_score), True, (255, 255, 255))
    score2 = font.render(str(bar2_score), True, (255, 255, 255))
    surface.blit(header1, (200, GAME_HEIGHT - 100))
    surface.blit(score1, (350, GAME_HEIGHT - 50))
    surface.blit(header2, (425, GAME_HEIGHT - 100))
    surface.blit(score2, (425, GAME_HEIGHT - 50))

    v_paddle_player.draw(surface)
    ht_paddle_player.draw(surface)
    hb_paddle_player.draw(surface)
    ht_paddle_computer.draw(surface)
    hb_paddle_computer.draw(surface)
    v_paddle_computer.draw(surface)
    ball.draw(surface)

    pygame.display.update()

    ready = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                ready = True

        if (bar1_score == 5 or bar2_score == 5) and ready:
            ready = False
            if bar1_score == 5:
                surface.fill(BLACK)
                end_screen = font.render(str(lose_end_screen), True, (255, 255, 255))
                surface.blit(end_screen, ((GAME_WIDTH - 500) / 2, (GAME_HEIGHT - 100) / 2))
                pygame.mixer.music.load('Sounds/player_lose.mp3')
                pygame.mixer.music.play(-1, 0.0)
            elif bar2_score == 5:
                surface.fill(BLACK)
                end_screen = font.render(str(win_end_screen), True, (255, 255, 255))
                surface.blit(end_screen, ((GAME_WIDTH - 300) / 2, (GAME_HEIGHT - 100) / 2))
                pygame.mixer.music.load('Sounds/player_win.mp3')
                pygame.mixer.music.play(-1, 0.0)
            pygame.display.update()

        if ready:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and v_paddle_player.y > 0:
                v_paddle_player.move_up()
            if keys[pygame.K_DOWN] and v_paddle_player.y < (GAME_HEIGHT - v_paddle_player.height - 100):
                v_paddle_player.move_down()

            if keys[pygame.K_LEFT] and hb_paddle_player.rect.left > 400:
                ht_paddle_player.move_left()
                hb_paddle_player.move_left()
            if keys[pygame.K_RIGHT] and hb_paddle_player.rect.right < (GAME_WIDTH - 30):
                ht_paddle_player.move_right()
                hb_paddle_player.move_right()

            surface.fill(BLACK)
            v_paddle_player.draw(surface)
            ht_paddle_player.draw(surface)
            hb_paddle_player.draw(surface)
            ht_paddle_computer.get_move(ball.rect)
            hb_paddle_computer.get_move(ball.rect)
            ht_paddle_computer.draw(surface)
            hb_paddle_computer.draw(surface)
            v_paddle_computer.get_move(ball.rect)
            v_paddle_computer.draw(surface)
            ball.draw(surface)
            ball.move()
            ball.collide(paddles)
            did_reset, scorer = ball.reset(GAME_WIDTH / 2, GAME_HEIGHT / 2, random_ball_vel())

            if did_reset:
                line_color = get_random_color()
                if scorer == 'player':
                    bar2_score += 1
                    # score2 = font.render(str(bar2_score), True, (255, 255, 255))
                    score_sound = pygame.mixer.Sound('Sounds/player_score.wav')
                    score_sound.play()
                elif scorer == 'computer':
                    bar1_score += 1
                    # score1 = font.render(str(bar1_score), True, (255, 255, 255))
                    score_sound = pygame.mixer.Sound('Sounds/computer_score.wav')
                    score_sound.play()
                v_paddle_player.reset(770, 200, surface)
                v_paddle_computer.reset(20, 200, surface)
                ht_paddle_computer.reset(250, 10, surface)
                hb_paddle_computer.reset(250, 480, surface)
                ht_paddle_player.reset(550, 10, surface)
                hb_paddle_player.reset(550, 480, surface)
            pygame.draw.line(surface, line_color, (GAME_WIDTH / 2, GAME_HEIGHT - 100), (GAME_WIDTH / 2, 0), 5)
            pygame.draw.rect(surface, BLUE, (0, GAME_HEIGHT - 100, GAME_WIDTH, 100))
            score1 = font.render(str(bar1_score), True, (255, 255, 255))
            score2 = font.render(str(bar2_score), True, (255, 255, 255))
            surface.blit(header1, (200, GAME_HEIGHT - 100))
            surface.blit(score1, (350, GAME_HEIGHT - 50))
            surface.blit(header2, (425, GAME_HEIGHT - 100))
            surface.blit(score2, (425, GAME_HEIGHT - 50))
            pygame.display.update()


play()
