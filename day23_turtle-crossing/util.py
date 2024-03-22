import random


def generate_random_rgb() -> tuple:
    # To prevent generating light colors, i'v set max number to 240 instead of 255
    r = random.randint(0, 240)
    g = random.randint(0, 240)
    b = random.randint(0, 240)
    return r, g, b
