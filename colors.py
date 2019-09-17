import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


def get_random_color():
    colorx = random.randint(0, 255)
    colory = random.randint(0, 255)
    colorz = random.randint(0, 255)
    color = [colorx, colory, colorz]
    random.shuffle(color)
    return tuple(color)
